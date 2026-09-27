---
name: create-primary-music-slideshows
description: Create or revise illustrated LDS Primary singing-time slideshows with accurate lyrics, memorable visual cues, a consistent cast, and reverent imagery. Use for Primary song storyboards, illustrations, and finished slide decks.
---

# Create Primary music slideshows

## Governing guidance

Read the workspace's root INSTRUCTIONS.md before planning or editing a slideshow. It is the authoritative project guidance. When used outside this repository and no project INSTRUCTIONS.md exists, read [the bundled project instructions](references/primary-music-project-instructions.md). Do not read both copies unnecessarily. Explicit user instructions take precedence.

## Start or resume a song

Inspect existing files in songs/ before asking for information or recreating work. Ask for the song title when missing: a literal [song] is an unfilled placeholder, not a song selection. Resolve consequential ambiguities about version and verses. Use existing lyrics and preferences when supplied. Obtain and verify the complete authorized wording before illustration; do not invent or paraphrase lyrics. Respect applicable content-use restrictions and request user-supplied lyrics when needed.

Use songs/<song-slug>/ for each song, with:

- lyrics.md: selected verses, exact usable lyrics, source and version.
- storyboard.md: the ordered slide plan, cast, visual specification, verified sources, image prompts and progress.
- images/: retained illustrations with stable slide-number filenames.
- slideshow.pptx: the completed deck.

Create those artifacts as work reaches each stage, not as empty deliverables. Retain assembly source and rendered previews in the song folder when useful for revisions. Use root references/ for shared research and reusable reference assets. Preserve passing slides and user edits when continuing work.

## Plan before illustrating

Follow the full Required Creation Workflow in the governing instructions. Present the complete slide sequence and visual concept before generating images. This is a planning step, not an automatic approval gate; continue authorized work unless the user requested approval or an unresolved choice materially affects the result.

For each slide, record its lyric segment, one key memory word or phrase, central visual cue, scene type (literal, historical, scriptural, contemporary, or symbolic), and facts requiring verification. Group natural phrases into at most two displayed lyric lines per slide; split a pair when the cue becomes overloaded. Use one memorable idea per scene rather than automatically one slide per printed line. For abstract lyrics, try a grounded two- or three-part visual progression with a clear reading order when a single symbolic scene becomes surreal.

Design a fresh cast and visual world for each new song unless cross-song reuse was explicitly requested. Establish continuity within that song. Make a plain cast sheet for recurring characters, then use it as a reference in later prompts when supported. Keep the reference sheet free of decorative song motifs. Define and repeat a concise style specification to control drift, and do not import locations or a cast from another song by default.

If creating a singing-time lesson as well, establish the intended Sunday (default to the upcoming Sunday) and consult the applicable official Come, Follow Me manual. Explain a meaningful connection simply; do not force a weak connection or assume the bundled 2026 manual applies to another year.

## Illustrate, assemble, and verify

Use available image-generation and presentation capabilities and their applicable instructions. Preserve consistent characters, clothing, style, and historical context. Resolve sacred imagery before generating anything: the governing instructions prohibit AI depictions of Heavenly Father or Jesus Christ, visible portrayals of the Holy Ghost, synthetic likenesses of living Church leaders, and restricted temple imagery. Follow the complete reference for permitted alternatives and official imagery.

Generate illustrations without lyrics embedded in the art. Check every image's actual aspect ratio and dimensions before acceptance. Keep the intended lyric band, usually the lower third, calm and clear of key action. Assemble editable, large, high-contrast lyrics separately in a 16:9 deck unless requested otherwise, with line breaks at phrase boundaries. Review the matched image set before assembly and render the actual completed deck afterward.

Inspect every slide at full size and room-viewing distance for lyric accuracy, continuity, cropping, readability, historical and doctrinal accuracy. With lyrics mentally covered, score the image's memory cue from 1 to 5; check whether another object, symbol, or dramatic setting hijacks the intended cue. Record scores in storyboard.md and revise every slide below 4, preserving slides that already pass. Complete the governing final review checklist before delivery. Never claim rendering, inspection, or a successful file-open check that was not performed.

Deliver a link to the finished slideshow and disclose any limitation that affects classroom use. Keep build notes out of children's slides. When sharing beyond the local classroom, identify AI illustrations and clarify that the deck is not an official Church publication.

## Maintenance

Root INSTRUCTIONS.md is the source of truth in this repository. When it changes, refresh references/primary-music-project-instructions.md in this skill as an exact copy so the skill remains portable. The .agents/skills entry point routes here; keep substantive workflow instructions in this file.
