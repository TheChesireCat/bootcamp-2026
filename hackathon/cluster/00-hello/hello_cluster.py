import os

print("Hello from the cluster!")
print("Hostname:", os.uname().nodename)   # which compute node ran this
print("1 + 1 =", 1 + 1)
