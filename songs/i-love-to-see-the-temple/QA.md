# Final QA — I Love to See the Temple

Date: 2026-10-24 (America/Denver). Edited original presentation, not a replacement.

## Result
Title slide 62 retained, native ID h220c9fa8d8ee0741_0_299. Eight lyric slides 63–70. Four complete four-line blocks, A–D; two image slides per block. First image highlights lines 1–2; second highlights lines 3–4. Both verses remain complete, eight authorized lyric lines per verse. No extra repetitions or omitted passages. Total program slides: 119 (was 115). Following Truth from Elijah title is now 71; all other songs retain content and relative order.

Presentation: https://docs.google.com/presentation/d/1yrM3unhoBufmYEWsc3nrxIvcX62edf5IPmOoGlx1p4Q/edit#slide=id.h220c9fa8d8ee0741_0_299

## Actual inspections
- Inspected pixels of all four original lyric slides: text-only cream backgrounds, no existing artwork to retain. Speaker notes were empty.
- Inspected completed live examples from Think a Sacred Song (54), Truth from Elijah (68 before insertion), I Will Shine (80 before insertion), and Holding Hands Around the World (90 before insertion).
- Reviewed official Fort Collins temple photograph before generating recognizable architecture. Verified one central tower, dark pointed steeple, actual Moroni, cream masonry, arched openings, fountain and landscaped public grounds. No readable generated inscriptions.
- Reviewed plain cast sheet, every generated illustration, and the matched set. Fresh fictional cast throughout. All eight accepted illustrations are 1672×941 pixels; cast sheet 1536×1024. Tiny aspect-ratio difference safely removed through centered proportional slide cropping, without stretching.
- PDF export attempted and failed HTTP 403. Used native LARGE Google Slides thumbnails (1600×900) for the title and every final lyric slide. Inspected all nine at full size and at 400×225 per slide in a room-view contact sheet.
- Full-size first review found the boy's lower face overlapped by cyan text on slide 65. Reframed image 03 higher, replaced it, fetched and inspected a fresh LARGE native thumbnail. Repaired face is fully clear. Rebuilt and inspected final room-view contact sheet.
- Image 08 was reframed before final QA to keep the family album above lyrics. The final rendered album and faces remain visible.
- Text: all deliberate lines remain single lines; no wrapping, clipping, overlap between lyric lines or loss of punctuation. Entire block visible on every slide; highlights match the active natural phrase and change only with a distinct illustration.
- Readability: same centered Arial Bold 35 pt everywhere, white inactive / #40E5F2 active; text x=12 y=219 w=696 h=175 pt, lineSpacing 100, zero paragraph spacing. Longest line measured 673.2 pt at 35 pt; at 36 pt it measures 692.0 pt and exceeds the 688.8 pt interior width after text insets. Four lines fit vertically. Room-view review passes; no physical projector test was performed.
- Coverage: full-slide #05080A overlay alpha 0.42, all four edges covered; no baked blank strips. Re-read intrinsic image size after insertions and both replacements. Equal horizontal/vertical scale 218.756 over native 41800×23525 EMU base; centered y=-1367.225 EMU covers 9144000×5143500 EMU slide, safely trimming approximately half a source pixel vertically.
- Transitions: title → anticipation → home prayer → temple/gardens → everyday service → temple approach → learning/obedience → family together → family memories → following song title. No duplicate-image highlight-only states. Cast, clothing and style stay consistent.
- Sacred imagery: no AI Deity or visible Holy Ghost, no ordinance, ceremonial clothing, restricted interior, invented temple room or sacred gesture. Covenant and sealing lyrics are supported through public family scenes and everyday preparation, not depicted as ceremonies.

## Memory-cue scores (lyrics mentally covered)

| Art / slide | Cue | Score | Finding |
|---|---|---|---|
| 01 / 63 | See / someday | 5 | Child points eagerly at clearly visible temple |
| 02 / 64 | Listen / pray | 5 | Attentive listening followed by ordinary home prayer |
| 03 / 65 | House / love / beauty | 4 | Verified temple exterior, loving embrace and garden flowers; repaired faces clear |
| 04 / 66 | Prepare / duty | 4 | Young children actively serving grandmother; preparation needs song context |
| 05 / 67 | Go inside someday | 4 | Family moving toward temple exterior; future timing supplied by lyric |
| 06 / 68 | Promise / obey | 4 | Learning from scriptures then following through with useful action; no covenant ceremony |
| 07 / 69 | Holy place / together | 4 | Family united on public temple grounds; no sealing depiction |
| 08 / 70 | Child / family forever | 4 | Three generations sharing family memories; eternal duration requires lyric context |

## Structural verification
Fresh final native presentation read revision v-MwEdQYoTCU0Q; verify.py passed. All eight lyric texts equal original wording after removing VERSE labels; font, highlight ranges, geometry and proportional image coverage verified. Compared all 111 slides outside the four replaced original lyric slides, including unchanged title: their normalized native content and relative order are identical. Only volatile image contentUrl values were excluded. No changes to surrounding songs.

Local issue checker: zero errors, seven warnings for existing empty text placeholders on program title cards (including retained temple title). Preserved intentional existing title structure.

## Provenance and saved evidence
Accepted images and cast sheet: images/. Final native thumbnail renders: previews/62.png through previews/70.png; final reduced contact sheet: previews/room-view.png. Final slide IDs and mapping: slide-map.json. Assembly requests, crop/notes requests and final image replacements are saved separately. Assembly requests describe the original baseline-to-section build and are not an idempotent rerun recipe. verify.py requires local before/after snapshots in workspace work/; complete program snapshots are not published to this song folder.

Lyrics © 1980 Janice Kapp Perry, permitted for incidental noncommercial church/home use. Official reference photograph © Intellectual Reserve, Inc.; used to verify architecture and not redistributed here. All scene artwork is AI-generated, not official Church artwork or an official Church publication. Official source links and rights notices are in lyrics.md, storyboard.md and each lyric slide's speaker notes.

