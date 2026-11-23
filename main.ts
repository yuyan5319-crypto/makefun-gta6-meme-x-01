// gta6-meme-x-01 entry program (Node 22, standard library only).
//
// The entry itself is a post on X: a GTA 6 meme whose picture carries
// make.fun's ghost and whose text carries the bounty link and my play
// code. This program's only job is to hand the post's address to the
// grader: it copies POST.json from the repository root into the output
// directory, where the gate reads it.
//
// Local run:
//   mkdir -p out && MAKEFUN_BOT_DIR=. MAKEFUN_OUTPUT_DIR=out node main.ts

import { copyFileSync, mkdirSync } from 'node:fs';
import { join } from 'node:path';

const botDir = process.env.MAKEFUN_BOT_DIR ?? '/bot';
const outDir = process.env.MAKEFUN_OUTPUT_DIR ?? '/output';

mkdirSync(outDir, { recursive: true });

try {
  copyFileSync(join(botDir, 'POST.json'), join(outDir, 'POST.json'));
  console.log(`POST.json copied from ${botDir} to ${outDir}`);
} catch (err) {
  console.error(`could not copy POST.json: ${(err as Error).message}`);
  process.exit(1);
}
