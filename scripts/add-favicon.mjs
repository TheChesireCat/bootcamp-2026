// Injects an emoji favicon into each built HTML deck's <head>.
// Marp CLI owns the HTML template and has no favicon option, so we post-process
// the dist/*.html files. Uses an inline SVG data URI (no image file needed).
import { readFileSync, writeFileSync, readdirSync } from 'node:fs';
import { join } from 'node:path';

const dist = 'dist';

// 🤖 rendered as an SVG favicon. %22 = the encoded double-quotes inside the data URI.
const favicon =
  '<link rel="icon" href="data:image/svg+xml,' +
  '<svg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 100 100%22>' +
  '<text y=%22.9em%22 font-size=%2290%22>🤖</text></svg>">';

for (const file of readdirSync(dist).filter((f) => f.endsWith('.html'))) {
  const path = join(dist, file);
  let html = readFileSync(path, 'utf8');
  if (html.includes('rel="icon"')) continue; // already has one
  html = html.replace('</head>', favicon + '</head>');
  writeFileSync(path, html);
  console.log(`favicon ▸ ${path}`);
}
