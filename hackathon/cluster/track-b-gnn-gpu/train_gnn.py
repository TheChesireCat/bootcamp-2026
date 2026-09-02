"""
Track B, GNN node classification (a 2-layer GCN).

Runs on GPU or CPU. The point is to see a real training loop on the cluster and
watch which GPU you actually landed on.

Examples:
    python3 train_gnn.py --dataset Cora --device auto --epochs 200
    python3 train_gnn.py --dataset KarateClub --device cpu   # tiny, no GPU needed
"""

import argparse
import time

import torch
import torch.nn.functional as F
from torch_geometric.nn import GCNConv


def get_dataset(name):
    """Cora (default) for a real run, KarateClub for a tiny CPU-friendly one."""
    if name.lower() in ("karate", "karateclub"):
        from torch_geometric.datasets import KarateClub
        return KarateClub()
    from torch_geometric.datasets import Planetoid
    return Planetoid(root="data/Planetoid", name=name)  # Cora / Citeseer / Pubmed


class GCN(torch.nn.Module):
    def __init__(self, in_dim, hidden, out_dim):
        super().__init__()
        self.conv1 = GCNConv(in_dim, hidden)
        self.conv2 = GCNConv(hidden, out_dim)

    def forward(self, x, edge_index):
        x = F.relu(self.conv1(x, edge_index))
        x = F.dropout(x, p=0.5, training=self.training)
        return self.conv2(x, edge_index)


def resolve_device(choice):
    if choice == "auto":
        choice = "cuda" if torch.cuda.is_available() else "cpu"
    device = torch.device(choice)
    print(f"device: {device}")
    if device.type == "cuda":
        # This is where the "old GPU" story shows up: name + compute capability.
        print(f"  GPU: {torch.cuda.get_device_name(0)}")
        cc = torch.cuda.get_device_capability(0)
        print(f"  compute capability: {cc[0]}.{cc[1]}")
    return device


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dataset", default="Cora")
    ap.add_argument("--device", default="auto", choices=["auto", "cuda", "cpu"])
    ap.add_argument("--epochs", type=int, default=200)
    ap.add_argument("--hidden", type=int, default=16)
    args = ap.parse_args()

    device = resolve_device(args.device)

    dataset = get_dataset(args.dataset)
    data = dataset[0].to(device)
    print(f"dataset: {args.dataset}  nodes={data.num_nodes}  "
          f"features={dataset.num_features}  classes={dataset.num_classes}")

    # Some datasets ship a test_mask; KarateClub does not, so fall back to all nodes.
    test_mask = getattr(data, "test_mask", None)
    if test_mask is None:
        test_mask = torch.ones(data.num_nodes, dtype=torch.bool, device=device)

    model = GCN(dataset.num_features, args.hidden, dataset.num_classes).to(device)
    opt = torch.optim.Adam(model.parameters(), lr=0.01, weight_decay=5e-4)

    t0 = time.time()
    for epoch in range(1, args.epochs + 1):
        model.train()
        opt.zero_grad()
        out = model(data.x, data.edge_index)
        loss = F.cross_entropy(out[data.train_mask], data.y[data.train_mask])
        loss.backward()
        opt.step()
        if epoch % 20 == 0 or epoch == 1:
            print(f"epoch {epoch:3d}  loss {loss.item():.4f}")
    train_time = time.time() - t0

    model.eval()
    pred = model(data.x, data.edge_index).argmax(dim=1)
    acc = (pred[test_mask] == data.y[test_mask]).float().mean().item()
    print(f"test accuracy: {acc:.3f}")
    print(f"trained {args.epochs} epochs in {train_time:.2f}s on {device.type}")


if __name__ == "__main__":
    main()
