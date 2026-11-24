// "The World Today — 23 November 2026" (make.fun news-image-20261123).
// A deterministic program (Node 22, standard library only): it copies the
// pre-rendered front page at assets/entry.png to /output/entry.png.
// No network, no randomness: every run writes the same bytes. The image is
// rendered in code by scripts/render.py, so the entry is reproducible from
// this repository alone.
//
// Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
//   mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts

import { copyFileSync } from 'node:fs';
import { join } from 'node:path';

copyFileSync(
  new URL('./assets/entry.png', import.meta.url),
  join(process.env.MAKEFUN_OUTPUT_DIR ?? '/output', 'entry.png'),
);
