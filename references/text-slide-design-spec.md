# Primary text-slide design spec

The standing design for **text-only** singalong decks: songs where the lyrics carry the slide and there is no illustration. The image-led method (the key-word visual memory test, the song's own cast, the sacred imagery limits) lives in [../INSTRUCTIONS.md](../INSTRUCTIONS.md). This spec governs the other case. Both deck types use the same stage size and export path, so a song can move between them.

Reference implementation: `singalong_deck.py`, where every rule below is a named constant at the top of the file. *The script is not yet committed to this repository; add it to `references/` when available.*

---

## 1. The governing rule

**A child who cannot yet read fluently is tracking the line with their finger and their ear at the same time.** Every decision below follows from that: nothing on the slide competes with the words, the words never move around between slides, and a sung phrase is never cut in half.

## 2. Stage

| | |
|---|---|
| Slide size | 13.333 × 7.5 in (16:9), same as the image decks, so PNG export and the MP4 path work unchanged |
| Background render | 2000 × 1125 PNG, generated in Pillow and placed full-bleed |
| PNG export | LibreOffice headless → PDF → `pdftoppm -png -r 144` = exactly 1920 × 1080 |
| File naming | `NN - <lyric>.png`, so slides sort in order and are identifiable |

## 3. Color

Dark ground, light type. On a chapel projector with the lights half up, a white background washes out and blooms, and dark type on white loses far more contrast than light type on dark.

| Role | Value | Notes |
|---|---|---|
| Background, top | `#1C2E4E` | deep navy |
| Background, bottom | `#0A1120` | near-black |
| Center lift | `#2E4670` | soft elliptical glow behind the text block, centered at 44% height; keeps the type off flat navy without reading as a shape |
| Lyric type | `#FDFAEE` | warm cream, not pure white; pure white on navy vibrates at size |
| Title-slide rule | `#D9B86A` | muted gold, 2.2 in × 2.5 pt |
| Credit line | `#A8B4C8` | recedes without disappearing |
| Title slide, top | `#24385C` → same bottom | one step brighter than lyric slides, so the deck opens and then settles |

No imagery, logos or decoration on lyric slides. The gold rule appears on the title slide only.

## 4. Type

- **Arial Bold**, centered, `#FDFAEE`.
- **One point size for the entire deck.** Type that changes size from slide to slide distracts children who are tracking along. The size is computed, not chosen: the largest size from 28 to 60 pt at which *every* line in the deck fits the usable width. Measure real glyph advances (Liberation Sans Bold is metric-identical to Arial), not character counts.
- **Line spacing 1.35.** Tighter reads as a block; looser breaks the couplet apart.
- **Vertically centered** in a 12.0 × 5.2 in box at y = 1.30 in. Centering (the image decks anchor to the bottom) is right here because there is no picture for the text to sit under.
- **Usable width 11.6 in**, roughly 0.9 in gutters. Deliberately generous: chapel projectors overscan, and the edge of the frame is the first thing lost.
- **Title 52 pt** (shrunk to fit if the title is long), **credit 16 pt** regular.
- Typographic apostrophes (’) throughout, matching the hymnbook.

## 5. Line breaks

**The music leader's line breaks are authoritative.** They mark where the phrase breathes; a script does not know that. So:

1. Lines are taken exactly as given (a JSON list, or `" / "` inside a string).
2. The deck size is computed from those lines as given.
3. **Only if** that size falls below **44 pt**, too small to read from the back row, are the offending lines broken, and only the lines that actually overflow.
4. An automatic break lands at a phrase boundary, in this order: after `; : ,` or a clause-joining conjunction → before a preposition or relative pronoun (`of`, `in`, `to`, `with`, `that`, `who`, `around` …) → the nearest space, as a last resort. Never break on a conjunction joining two words rather than two clauses ("heart and / mind" is wrong).
5. Within the best available tier, the break goes as **late** as possible while the first line still fits and the second is not a widow. That fills line one and keeps a trailing phrase intact: `I belong to The Church of Jesus Christ / of Latter-day Saints.`, not `I belong to The Church / of Jesus Christ of Latter-day Saints.`

Never break mid-phrase, and never break a line only to make the type bigger. Smaller type costs less than a severed phrase.

## 6. Grouping lyrics onto slides

- **One singable unit per slide**: a couplet, or a three-line group that resolves. A child should be able to hold the unit in their head from the moment it appears until it is sung.
- **Four lines is the ceiling** for text-only decks (illustrated decks stop at two; see INSTRUCTIONS.md). The builder warns past four. If a group needs five, it is two slides.
- Slides break where the *music* breathes, not wherever the punctuation falls.
- A chorus is written once and repeated by reference (`repeat_of`), so a lyric fix lands everywhere.

## 7. Title slide

Title, gold rule, credit. Included by default; set `"title_slide": false` to drop it.

The credit line carries author and source: `Words and music: <author>  ·  <songbook, number>`. Verify the number and the wording against Gospel Library before building (see the hymnbook note under Lyrics in INSTRUCTIONS.md).

## 8. Rights and labeling

Unchanged from the image method. Copyright permission for these songs generally covers incidental, noncommercial Church or home use. A public upload goes beyond that, so unlisted is the safer choice, and nothing is monetized or presented as an official Church publication. Text-only decks carry no AI-generated imagery, so the AI-illustration disclosure does not apply to them.

---

## Using the builder

```bash
python3 singalong_deck.py song.json -o "Song Title - singalong.pptx" --png
```

`song.json`:

```json
{
  "title": "Song title",
  "credit": "Words and music: <author>  ·  Hymns—For Home and Church, <number>",
  "title_slide": true,
  "sections": [
    { "name": "verse 1", "slides": ["line one / line two", ["line three", "line four"]] },
    { "name": "chorus", "slides": ["..."] },
    { "name": "chorus (repeat)", "repeat_of": "chorus" }
  ]
}
```

A slide is a string (with `" / "` for explicit breaks) or a list of lines. `--png` writes 1920 × 1080 exports next to the deck. In a public repository, keep `song.json` (which contains full lyrics) in the local song folder, not in the repo.

To restyle the whole system (a different ground color for a Christmas song, larger type for a big room), change the constants in the **DESIGN SPEC** block at the top of the script. Nothing below that block needs editing.
