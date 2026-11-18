// Open a slide with #check (the contact sheet does) to outline in red anything that doesn't fit:
// a layer past the edge of the slide, or text that overflows its own box.
(function () {
  if (location.hash !== '#check') return;
  const run = () => {
    const slide = document.querySelector('.slide');
    if (!slide) return;
    const S = slide.getBoundingClientRect(), bad = [];
    slide.querySelectorAll('.L').forEach(el => {
      const r = el.getBoundingClientRect();
      const off = r.left < S.left - 1 || r.top < S.top - 1 || r.right > S.right + 1 || r.bottom > S.bottom + 1;
      // tight serif line-heights make glyphs poke out a little, so only a box with a set height is checked vertically
      const spill = el.scrollWidth > el.clientWidth + 2 || (el.style.height && el.scrollHeight > el.clientHeight + 4);
      if (off || spill) bad.push([el, off ? 'off the slide' : 'text overflows']);
    });
    for (const [el, why] of bad) {
      el.style.outline = '6px solid #FF2D2D'; el.style.outlineOffset = '4px';
      const tag = document.createElement('div');
      tag.textContent = why;
      Object.assign(tag.style, { position: 'absolute', zIndex: 9999, background: '#FF2D2D', color: '#fff', font: '700 26px/1 Inter, sans-serif', padding: '8px 12px', borderRadius: '6px',
        left: Math.max(0, el.offsetLeft) + 'px', top: Math.max(0, el.offsetTop - 44) + 'px' });
      slide.appendChild(tag);
    }
    document.documentElement.dataset.problems = String(bad.length);
  };
  (document.fonts ? document.fonts.ready : Promise.resolve()).then(() => setTimeout(run, 50));
})();
