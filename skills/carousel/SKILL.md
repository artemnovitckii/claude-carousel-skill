---
name: carousel
description: Makes a finished Instagram carousel from a topic. Finds proven carousels to learn from (Top Carousels), writes the hook and every slide, builds each slide as HTML with every element as its own layer, renders 1080×1440 PNGs and checks them before handing over. Use when the user runs /carousel, asks to make, design or remix a carousel, or pastes a topcarousels.com link.
---

# /carousel

You make a carousel that is ready to post: PNG slides, a caption, and the HTML source so anything can be changed later. Work in this order and don't skip the check at the end.

Files in this skill's folder (use its full path):
- `assets/carousel.css` — the design system: canvas, themes, type scale, layer classes
- `assets/check.js` — outlines anything that overflows when a slide is opened with `#check`
- `assets/slide.html` — a starting slide to copy
- `scripts/render.py` — renders every slide to PNG plus a contact sheet
- `references/copy.md` — hooks, slide counts and the rules for writing slides
- `references/design.md` — layout rules and the layer pattern
- `references/top-carousels.md` — how to get references, with and without the Top Carousels connector

## 1. Brief (one short message)

If the user gave a topic, don't interrogate them. Ask only what you can't guess, in one message, and offer your guess:
- the topic and who it's for
- their Instagram handle (for the footer), or none
- light or dark (default: `paper`, the light cream theme)

If they say "just go", use your guesses.

## 2. References (read `references/top-carousels.md`)

Find 2–3 carousels on this topic or format that beat their creator's usual engagement, and learn from them: the hook, the format, the slide count, how much text sits on each slide.

- **Top Carousels tools available** (`search_carousels`, `top_outliers`, `view_slides`, `remix_brief`): search by the topic, then by the format. Look at the slides of the best 2–3 with `view_slides`. Tell the user which ones you're using, with their multiple (e.g. "11.2× her usual") and link.
- **User pasted a topcarousels.com link**: with the tools, use `remix_brief` on it. Without them, ask for screenshots of its slides.
- **No tools, nothing pasted**: say once, in one line, that the skill works better with references and how to get them (the free library on topcarousels.com, or the connector). Then carry on with the formats in `references/copy.md`. Never stall here.

Never copy a reference's words or design. Borrow its structure.

## 3. Plan (read `references/copy.md`)

Send the user, in one message:
- 3 hook options for slide 1, each a different angle
- the slide-by-slide outline: one line per slide
- the slide count and why

Wait for them to pick a hook (or say "go"). Then write every slide's final text.

## 4. Build (read `references/design.md`)

1. Make a folder `carousels/<short-slug>/` in the current directory. Copy `assets/carousel.css` and `assets/check.js` into it.
2. Write one file per slide: `slide-01.html`, `slide-02.html`, … starting from `assets/slide.html`. Every element is its own absolutely positioned layer (`class="L ..."` with `left`, `top`, `width` set inline), so any one of them can be moved later without touching the rest.
3. Keep one system across the deck: same theme, margins, type sizes and footer on every slide. Slide 1 sells the swipe. The last slide has the save, share or comment ask.
4. Images: only the user's own screenshots, photos or logos, if they gave you any. Put them in the folder and use `<img class="L shot">`. Otherwise design with type, numbers, cards, lists and simple shapes. Don't invent screenshots of real products.

## 5. Render and check

Run:

```bash
python3 <skill folder>/scripts/render.py carousels/<short-slug>
```

It writes `png/slide-01.png` … and `sheet.png`, a contact sheet where anything overflowing its box or the slide is outlined in red with a label.

Then look at `sheet.png` yourself (and any slide you're unsure of at full size) and fix before you hand over:
- red outlines: text that doesn't fit, or a layer off the canvas
- text closer than 88px to an edge, or touching another layer
- a slide with more than about 30 words, or a line of 1–2 words left dangling
- weak contrast, or slides that don't look like the same deck

Re-render after every fix. Only stop when the sheet is clean.

## 6. Hand over

Tell the user, briefly:
- where the PNGs are (`carousels/<slug>/png/`), in posting order
- a caption: one line that restates the hook, 2–3 short lines of value, the ask, and 3–5 hashtags at most
- that they can ask for any change in plain words ("move the title up", "make slide 4 dark", "shorter hook") and you'll edit that layer and re-render

When you change something later, edit only the layers involved, re-render, and check the sheet again.
