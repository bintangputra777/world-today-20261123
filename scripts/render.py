#!/usr/bin/env python3
"""Render the front page for 'The World Today - Monday 23 November 2026'.

A newspaper-style single image (1024x1024) summing up the five biggest
world-news stories of Monday 23 November 2026. Pure Python/PIL, no network,
fully deterministic: the same input always produces the same PNG bytes.
"""

from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
BG = (251, 250, 247)          # warm paper white
NAVY = (15, 42, 74)           # masthead band
GOLD = (232, 184, 75)         # masthead date line
INK = (20, 20, 20)            # headline ink
GREY = (70, 70, 70)           # summary ink
RULE = (200, 196, 188)        # hairline rules

SERIF_B = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SANS_B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"

DATE_LINE = "MONDAY \u00b7 23 NOVEMBER 2026"

# (tag, badge colour, headline, summary)
STORIES = [
    (
        "UKRAINE \u00b7 LIBYA",
        (15, 42, 74),
        "Ukraine sinks Russian warship off Libya",
        "Naval drones sank the corvette Merkury at Benghazi port, Kyiv says \u2014 "
        "the war now reaches 1,500 miles from the front line.",
    ),
    (
        "MARKETS",
        (14, 116, 144),
        "Nvidia brings back Huang; shares soar 33%",
        "Jensen Huang returns as chief executive 11 days after resigning, and the "
        "S&P 500 jumps 4.8% as the AI sell-off reverses.",
    ),
    (
        "UKRAINE",
        (185, 28, 28),
        "Russian strike on flats near Kyiv kills 11",
        "A drone strike on a block in Dymer leaves at least 11 dead as rescuers "
        "search the rubble; 15 are killed across the Kyiv region.",
    ),
    (
        "MEXICO",
        (180, 83, 9),
        "\u201cEl Chapo Isidro\u201d captured in Sinaloa",
        "Mexican special forces seize cartel boss Fausto Isidro Meza Flores with US "
        "intelligence help; 16 suspected cartel members are killed.",
    ),
    (
        "INDONESIA",
        (109, 40, 217),
        "Factory fire in Banten kills 24",
        "A blaze at a candy factory in Cikande leaves at least 24 dead and about "
        "30 missing, police say, as the search resumes.",
    ),
]

FOOTER = "Sources: OneTurn \u00b7 Just Security \u00b7 Reuters \u00b7 Daily Brief \u2014 23 November 2026"


def font(path, size):
    return ImageFont.truetype(path, size)


def fit_one_line(draw, text, path, start, max_w):
    """Largest font size (<= start) that fits `text` on one line within max_w."""
    size = start
    while size > 10:
        f = font(path, size)
        if draw.textlength(text, font=f) <= max_w:
            return f
        size -= 1
    return font(path, size)


def wrap_two_lines(draw, text, f, max_w):
    """Wrap text to at most two lines, truncating the second with an ellipsis."""
    words = text.split()
    lines, cur = [], ""
    for w in words:
        trial = f"{cur} {w}".strip()
        if draw.textlength(trial, font=f) <= max_w:
            cur = trial
        else:
            lines.append(cur)
            cur = w
            if len(lines) == 2:
                break
    if len(lines) < 2 and cur:
        lines.append(cur)
    if len(lines) == 2 and cur and cur != lines[1]:
        # text remains: ellipsize the second line
        second = lines[1]
        while second and draw.textlength(second + "\u2026", font=f) > max_w:
            second = second.rsplit(" ", 1)[0]
        lines[1] = second + "\u2026"
    return lines


def main():
    img = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(img)

    # --- masthead -------------------------------------------------------
    d.rectangle([0, 0, W, 178], fill=NAVY)
    title_f = font(SERIF_B, 66)
    title = "THE WORLD TODAY"
    d.text(((W - d.textlength(title, font=title_f)) / 2, 34), title,
           font=title_f, fill=(255, 255, 255))
    date_f = font(SANS_B, 27)
    d.text(((W - d.textlength(DATE_LINE, font=date_f)) / 2, 122), DATE_LINE,
           font=date_f, fill=GOLD)
    d.rectangle([0, 178, W, 184], fill=GOLD)

    # --- story rows ------------------------------------------------------
    row_top, row_h, gap = 204, 140, 8
    x_text = 116
    max_w = W - x_text - 28
    for i, (tag, colour, headline, summary) in enumerate(STORIES):
        y = row_top + i * (row_h + gap)
        # number badge
        d.ellipse([28, y + 8, 92, y + 72], fill=colour)
        num_f = font(SANS_B, 34)
        num = str(i + 1)
        d.text((60 - d.textlength(num, font=num_f) / 2, y + 18), num,
               font=num_f, fill=(255, 255, 255))
        # tag line
        tag_f = font(SANS_B, 21)
        d.text((x_text, y + 2), tag, font=tag_f, fill=colour)
        # headline: exactly one line
        head_f = fit_one_line(d, headline, SANS_B, 35, max_w)
        d.text((x_text, y + 30), headline, font=head_f, fill=INK)
        # summary: at most two lines
        sum_f = font(SANS, 23)
        lines = wrap_two_lines(d, summary, sum_f, max_w)
        for j, line in enumerate(lines):
            d.text((x_text, y + 74 + j * 30), line, font=sum_f, fill=GREY)
        # hairline between rows (not after the last)
        if i < len(STORIES) - 1:
            d.line([28, y + row_h + 2, W - 28, y + row_h + 2], fill=RULE, width=1)

    # --- footer ----------------------------------------------------------
    d.line([28, 948, W - 28, 948], fill=RULE, width=1)
    foot_f = font(SANS, 20)
    d.text(((W - d.textlength(FOOTER, font=foot_f)) / 2, 962), FOOTER,
           font=foot_f, fill=GREY)

    img.save("assets/entry.png", optimize=True)
    print("wrote assets/entry.png")


if __name__ == "__main__":
    main()
