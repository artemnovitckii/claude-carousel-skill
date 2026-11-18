# Designing the slides

## The canvas

1080×1440 (3:4, the tallest Instagram carousel size). For 4:5 run the render with `--size 1080x1350` and set `--h: 1350px` on `.slide`.

## Every element is a layer

Each element sits on the slide as its own absolutely positioned block:

```html
<div class="L h1" style="left:88px; top:300px; width:904px">The heading</div>
```

- `left`, `top` and `width` inline. Let height come from the text, or set it for images and cards.
- One element per layer: the heading, the body, a card, a number, an image. Don't wrap everything in one big flex box.
- That way "move the heading up 40px" or "make the card wider" is one edit to one line.

## Layout rules

- Margins: 88px on every side (`--pad`). Nothing important past that.
- The footer (handle and slide number) sits at the bottom on every slide, in the same place.
- A clear order on each slide: one thing is biggest. Usually the heading, sometimes a number or an image.
- Line up left edges. Most slides look best left-aligned on the 88px margin.
- Leave space. If a slide feels full, split it.
- Slide 1 gets the biggest type of the deck. The rest share one heading size.

## The design system (`carousel.css`)

Themes on `.slide` with `data-theme`:
- `paper`: warm cream, near-black text, orange accent (default)
- `ink`: near-black, cream text
- `bold`: bright yellow, black text, for hot takes

Type classes:
- `hook`: slide 1 headline, big serif
- `h1`: slide headings, serif
- `h2`: bold sans headings, for lists and steps
- `body`: body text
- `small`: captions and labels, muted
- `kicker`: small uppercase label above a heading, accent colour
- `num`: a huge accent number for list items and stats

Blocks: `card` (rounded surface with a shadow), `pill` (rounded label), `shot` (an image with rounded corners and a shadow), `rule` (a thin line), `foot` (the footer row).

Inline highlights: `<em class="hl">word</em>` for an accent italic word in a heading. Use it for one or two words, not whole lines.

You can add your own classes in a `<style>` tag on a slide, or in `carousel.css` for the whole deck. Keep the deck consistent.

## Fonts

Instrument Serif and Inter load from Google Fonts. If the user has brand fonts, swap `--serif` and `--sans` in `carousel.css` and load them there.
