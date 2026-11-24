# Dossier — make.fun bounty "Sum up 23 November's world news in one image"

## Bounty (verified 24 Nov 2026, ~07:55 WIB)

- Bounty: **Sum up 23 November's world news in one image** — https://make.fun/bounty/news-image-20261123
- Slug: `news-image-20261123` · Prize: **$100, 50 places paid** (1st $20, 2nd $12, 3rd $6, 4th–10th $2 each, 11th–50th $1.20 each), USDC on Solana. (Note: this edition's prize is $100, as on the 21–22 Nov editions — the task body's $250 figure is from the earlier 19–20 Nov editions.)
- Deadline: **Wednesday 25 Nov 2026, 07:00 WIB** (2026-11-25T00:00:00Z).
- Judging: an AI judge that can see images compares entries two at a time; the image itself must show the day's news (the judge has no news feed).
- Same format as the accepted 19, 20, 21 and 22 Nov entries (world-today-20261119/20/21/22). This build was written fresh in-session (render pipeline reimplemented from the task specification, not copied from an earlier entry folder).

## The image — five stories (checked 24 Nov against OneTurn's 23 Nov brief, Just Security Early Edition 23 Nov, Reuters via Devdiscourse, Daily Brief 23 Nov — all dated 23 Nov 2026)

1. **UKRAINE · LIBYA — Ukraine sinks Russian warship off Libya.** President Zelenskyy said Ukrainian naval drones sank the Russian corvette Merkury at a naval base in Benghazi, Libya, about 1,500 miles from the front line.
2. **MARKETS — Nvidia brings back Huang; shares soar 33%.** Nvidia reinstated Jensen Huang as chief executive 11 days after he resigned; shares jumped about 33% and the S&P 500 rose 4.82% after last week's sharp sell-off.
3. **UKRAINE — Russian strike on flats near Kyiv kills 11.** A Russian drone strike on a residential building in Dymer, north of Kyiv, killed at least 11 people; at least 15 were killed in Russian strikes on the Kyiv region.
4. **MEXICO — "El Chapo Isidro" captured in Sinaloa.** Mexican special forces captured Fausto Isidro Meza Flores, known as Chapo Isidro, in Sinaloa with US intelligence help; 16 suspected cartel members were killed in the operation.
5. **INDONESIA — Factory fire in Banten kills 24.** A fire at a candy factory in Cikande, Banten province, killed at least 24 people, with about 30 others still missing.

Design: newspaper front-page style — navy masthead "THE WORLD TODAY / MONDAY · 23 NOVEMBER 2026", five numbered colour-tagged rows, footer citing the news outlets. Rendered in code with Python/PIL (`scripts/render.py`) — no AI image generator.

## Program

`main.ts` copies `assets/entry.png` to `/output/entry.png` — deterministic, no network. Verified locally: two runs byte-identical and equal to the source asset (sha256 c4c16be6…5921, 1024x1024, 129,392 bytes).
