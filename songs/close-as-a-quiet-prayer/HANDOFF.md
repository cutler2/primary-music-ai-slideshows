# Handoff — Close as a Quiet Prayer

Read this first. Update it before you stop. `storyboard.md` is authoritative for cast, style and slide plan; this file tracks where the work is.

## Next up

- **Owner:** Image tool (ChatGPT)
- **Action:** **Deadline: Sunday 2026-09-27 (tomorrow).** Generate 00 (cast sheet) and commit it as `images/cast-sheet.png`. Then, using it as the reference, generate **01–11** in order and commit each as `images/NN.png`. Mark each row `generated` with its pixel dimensions. Regenerate anything that isn't 16:9 before committing. Don't stop between images unless the cast sheet looks wrong.
- **Then:** Claude reviews and scores, writes redo prompts if needed, and builds the deck (`build_deck.py`).
- **Needs:** prompts.md → 00–11.
- **Target Sunday:** 2026-09-27

## Status

Deck type: illustrated

| # | Key word | Prompt | Image | Score | Notes |
|---|---|---|---|---|---|
| 00 | cast sheet | ready | — | — | glance before scenes |
| 01 | NIGHT OR DAY | ready | — | — | split-frame risk |
| 02 | WHISPER | ready | — | — | must differ from 03 |
| 03 | QUIET PRAYER | ready | — | — | refrain, used 4× |
| 04 | THANKFUL | ready | — | — | |
| 05 | PRAISES / SMILES | revised | — | — | Dad smiles at singing Sione |
| 06 | ALONE | ready | — | — | |
| 07 | ANYWHERE | ready | — | — | three panels |
| 08 | KNEELING | ready | — | — | |
| 09 | SILENT HEART | ready | — | — | |
| 10 | ENFOLD | revised | — | — | Dad hug + quilt |
| 11 | title | ready | — | — | title slide art |

Prompt: `drafting` → `ready` → `revised`. Image: `—` → `generated` → `accepted` / `redo`. Score is the 1–5 memory-cue score with lyrics covered; anything under 4 is `redo`.

## Open questions

- None blocking. Cast approved; lyrics confirmed; title slide yes; Dad as a stand-in for Heavenly Father's love on 05 and 10.

## Log

Newest first.

- 2026-09-26 · Claude · Title slide (11) added; 05 and 10 revised to use Dad per music leader; lyrics confirmed; target set to 2026-09-27; build_deck.py added with text-only fallback.
- 2026-09-26 · Claude · Created lyrics.md, storyboard.md (new cast and style, 13 positions from 10 images), and prompts.md (00–10 ready). Decisions recorded in storyboard.md.
