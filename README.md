# The World Today — 23 November 2026

[![make.fun bounty](https://make.fun/badge/news-image-20261123.svg)](https://make.fun/bounty/news-image-20261123?ref=gr3weejb)
[![rank](https://make.fun/badge/news-image-20261123/bintangputra777/world-today-20261123/rank.svg)](https://make.fun/bounty/news-image-20261123?ref=gr3weejb)
[![reward](https://make.fun/badge/news-image-20261123/bintangputra777/world-today-20261123/reward.svg)](https://make.fun/bounty/news-image-20261123?ref=gr3weejb)

A one-image summary of the world's news of Monday 23 November 2026, built for
[make.fun's "Sum up 23 November's world news in one image" bounty](https://make.fun/bounty/news-image-20261123?ref=gr3weejb)
($100, 50 places paid, in USDC).

## The image

A newspaper-style front page — **THE WORLD TODAY / MONDAY · 23 NOVEMBER 2026** —
with the day's five biggest stories:

1. **Ukraine sinks Russian warship off Libya** — naval drones sank the corvette
   Merkury at Benghazi port.
2. **Nvidia brings back Huang; shares soar 33%** — the S&P 500 jumps 4.8%.
3. **Russian strike on flats near Kyiv kills 11** — a drone strike on a block
   in Dymer.
4. **"El Chapo Isidro" captured in Sinaloa** — Mexican special forces seize the
   cartel boss with US intelligence help.
5. **Factory fire in Banten kills 24** — a blaze at a candy factory in Cikande.

Sources: OneTurn, Just Security, Reuters, Daily Brief. See [DOSSIER.md](DOSSIER.md)
for the per-story source check.

## The program

`main.ts` (Node 22, standard library only) copies the pre-rendered front page
at `assets/entry.png` to `/output/entry.png` — no network, no randomness, so
every run writes the same bytes. The image itself is rendered in code by
`scripts/render.py` (Python/PIL), so the whole entry is reproducible from this
repository.

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts
```

Output: `entry.png`, 1024×1024, 129,392 bytes (sha256
`c4c16be646549c607208e23d91495cbd08add7ffff4619977f6c2c9f70a85921`).
