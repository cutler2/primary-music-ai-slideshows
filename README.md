# Primary Music AI Slideshows

A practical method for creating image-led LDS Primary song slideshows that help children **learn and recall lyrics**, not merely look at attractive pictures.

The central test is simple:

> If the lyric text were covered, could a four- or five-year-old use the picture to remember the key word or phrase?

Each slide should earn at least **4 out of 5** on that test before the deck is finished.

## What this method emphasizes

- One clear visual memory cue for each important lyric phrase
- A specific key word or phrase assigned to every slide
- A fresh cast and visual world for each song, with character and style continuity within that song
- Natural lyric grouping, up to two displayed lines per slide
- Historically believable people, clothing, settings, and demographics
- Reverent, doctrinally responsible treatment of sacred subjects
- Large, accurate lyrics readable from across a Primary room
- Rendering and inspecting the completed deck before delivery
- Revising only the slides whose image-to-lyric connection is weaker than 4/5

## Use this workspace in Codex

Open this repository folder in Codex and give the actual song title:

```text
Use INSTRUCTIONS.md as the governing instructions for this project.
Help me create a Primary singing-time slideshow for [song].
```

Replace `[song]` with the title and include the verses you want. Existing song
files are reused, so you do not need to upload the same material each time.
The root [AGENTS.md](AGENTS.md) routes future project work to the instructions
and the reusable skill.

The full skill lives in
[.codex/skills/create-primary-music-slideshows/SKILL.md](.codex/skills/create-primary-music-slideshows/SKILL.md).
A small entry point in `.agents/skills` enables automatic repository discovery,
following [current Codex skill guidance](https://learn.chatgpt.com/docs/build-skills).
If it does not appear in the skill picker, restart Codex. You can also explicitly
ask Codex to read the full skill path above.

For personal use outside this repository, copy the complete
`.codex/skills/create-primary-music-slideshows` folder into your user skill
directory (currently `~/.agents/skills` in the linked documentation). Copy the
full skill, not the repository entry point, whose relative link depends on this
repository. No personal installation is required to use this workspace.

## Retained song files

```text
Primary/
├── AGENTS.md
├── README.md
├── INSTRUCTIONS.md
├── .agents/skills/create-primary-music-slideshows/SKILL.md
├── .codex/skills/create-primary-music-slideshows/
│   ├── SKILL.md
│   ├── references/primary-music-project-instructions.md
│   └── templates/ (HANDOFF.md, prompts.md)
├── songs/
│   └── song-name/
│       ├── HANDOFF.md      ← read first, update last
│       ├── lyrics.md
│       ├── storyboard.md
│       ├── prompts.md
│       ├── images/
│       └── slideshow.pptx
└── references/
    └── text-slide-design-spec.md
```

Each song folder is created when work on that song begins. Storyboards retain
the cast, visual style, sources, prompts, and review progress. Assembly files and
previews can also be retained for later revisions. Local storage saves repeated
uploads and reconstruction; it does not inherently reduce model reasoning or
image-generation usage.

`INSTRUCTIONS.md` remains authoritative. Its bundled skill reference is an exact
copy for portability and must be refreshed whenever the root instructions change.

## Working across tools

Different tools can share one song folder, for example Claude for planning and assembly and ChatGPT for images. `songs/<song>/HANDOFF.md` says where the work stands, what's next, and who has it; `storyboard.md` holds every decision. Each session reads HANDOFF.md first and updates it last. A tool that can't write to the repo prints the lines to add.

To keep image sessions small, give the image tool only the cast sheet and the prompts it needs:

```text
Generate images for my Primary song. Read songs/<song-slug>/prompts.md in
github.com/cutler2/primary-music-ai-slideshows. Use the attached cast sheet as
the character reference. Generate prompts <NN>–<NN>, 16:9, no text in images.
Tell me each image's pixel dimensions.
```

This repository is public, so full lyric text stays in the local song folder; `lyrics.md` records source, number, and verification. [songs/holding-hands-around-the-world](songs/holding-hands-around-the-world/) is a finished example.

## Quick-start prompt without the local skill

Copy this prompt, add your song lyrics, and provide the detailed instructions in [INSTRUCTIONS.md](INSTRUCTIONS.md) as project or system guidance:

```text
Create an image-led slideshow to help young Primary children learn the song below. Break the lyrics into clear, memorable visual moments. Group natural phrases into no more than two displayed lyric lines per slide, rather than forcing each printed line onto one slide.

Follow the Primary slideshow instructions, especially the requirements for a fresh cast and visual world for this song (unless I request cross-song reuse), a consistent cast and style within this deck, historical and doctrinal accuracy, historically plausible demographics, believable clothing and physical conditions, and reverent sacred imagery.

First propose the slide sequence and visual concept for each slide. For every slide, identify the lyric's key memory word or phrase and make it unmistakably visible through the image's central action, object, gesture, or composition. A young child should be able to use the picture to recall that word without reading the text.

Then create the illustrations as a matched set and assemble the slideshow. Keep the lyrics large and readable from across a Primary room. Render and inspect the completed slides together. With the lyric text mentally covered, score each image-to-lyric connection from 1 to 5 and revise every slide below 4/5. Also correct inconsistent characters, mismatched actions, historical problems, anachronisms, inappropriate sacred imagery, or overly glamorous portrayals before delivering the final deck.

Song lyrics:
[PASTE THE AUTHORIZED LYRICS HERE]
```

## The 4/5 visual-memory test

| Score | What the picture communicates |
|---|---|
| 5 | The key lyric is unmistakable without text. |
| 4 | The intended phrase is clear with only a small amount of context. |
| 3 | The picture fits the general idea, but several lyrics could use the same image. |
| 2 | The connection depends mostly on explanation or printed words. |
| 1 | The image is mismatched, confusing, or misleading. |

A beautiful illustration can still score poorly. Repeated pictures of a child praying may fit a song's mood, but they do not necessarily distinguish **kneel**, **speak**, **thank**, **ask**, **faith**, or **Amen**. Each phrase needs its own visual vocabulary.

## Recommended workflow

1. Verify the authorized lyrics and identify the doctrine and emotional progression.
2. Divide the song into memorable visual moments.
3. Assign one key memory word or phrase to every slide.
4. Define this song's fresh cast, plain cast reference sheet, and visual specification.
5. Verify historical, architectural, scriptural, and doctrinal details.
6. Resolve sacred-imagery concerns before generating art.
7. Create the illustrations as one matched set.
8. Compare all illustrations for continuity, accurate 16:9 dimensions, and a distinct memory cue.
9. Assemble the deck with large, high-contrast lyrics.
10. Render the actual slides and inspect cropping and readability at full size and room-viewing distance.
11. Hide the lyrics mentally, score every image connection, and revise anything below 4/5.
12. Deliver only after the final deck passes both the visual-memory and technical checks.

## Important notice

This is an independent teaching-aid method and is **not an official publication of The Church of Jesus Christ of Latter-day Saints**. AI-generated illustrations should be identified as such when shared beyond a local classroom and should never be presented as official Church artwork, authentic historical photographs, or eyewitness records.

See [INSTRUCTIONS.md](INSTRUCTIONS.md) for the complete planning, illustration, sacred-imagery, historical-accuracy, assembly, and review guidance.
