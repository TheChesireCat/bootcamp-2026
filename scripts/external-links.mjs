// Make external links in the built HTML decks open in a new tab.
// Marp renders plain <a href="..."> with no target, so we post-process dist/*.html
// (same approach as add-favicon.mjs). Only touches http(s) links; adds rel for safety.
import { readFileSync, writeFileSync, readdirSync } from 'node:fs';
import { join } from 'node:path';

const dist = 'dist';

for (const file of readdirSync(dist).filter((f) => f.endsWith('.html'))) {
  const path = join(dist, file);
  const html = readFileSync(path, 'utf8');
  // Add target/rel to external <a href="http..."> that don't already have a target.
  const out = html.replace(
    /<a href="(https?:\/\/[^"]*)"(?![^>]*\btarget=)/g,
    '<a href="$1" target="_blank" rel="noopener noreferrer"'
  );
  if (out !== html) {
    writeFileSync(path, out);
    console.log(`links open in new tab ▸ ${path}`);
  }
}
