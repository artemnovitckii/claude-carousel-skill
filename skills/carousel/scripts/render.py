#!/usr/bin/env python3
"""Renders every slide-*.html in a carousel folder to PNG, plus a contact sheet that flags problems.

usage: python3 render.py carousels/<slug> [--size 1080x1440]

Writes <folder>/png/slide-01.png ... and <folder>/sheet.png. On the sheet, any layer that runs off
the slide or whose text overflows its box is outlined in red (see check.js). Needs Google Chrome,
Chromium or Microsoft Edge. No Python packages.
"""
import argparse, glob, os, platform, shutil, subprocess, sys, tempfile

CANDIDATES = {
    "Darwin": ["/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
               "/Applications/Chromium.app/Contents/MacOS/Chromium",
               "/Applications/Microsoft Edge.app/Contents/MacOS/Microsoft Edge",
               "/Applications/Brave Browser.app/Contents/MacOS/Brave Browser"],
    "Linux": ["google-chrome", "google-chrome-stable", "chromium", "chromium-browser", "microsoft-edge"],
    "Windows": [r"C:\Program Files\Google\Chrome\Application\chrome.exe",
                r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
                r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"],
}


def find_chrome():
    if os.environ.get("CHROME"):
        return os.environ["CHROME"]
    for c in CANDIDATES.get(platform.system(), []):
        p = c if os.path.isabs(c) else shutil.which(c)
        if p and os.path.exists(p):
            return p
    sys.exit("Couldn't find Chrome, Chromium or Edge. Install Google Chrome, or set CHROME=/path/to/chrome.")


def shoot(chrome, url, out, w, h):
    with tempfile.TemporaryDirectory() as profile:
        subprocess.run([chrome, "--headless=new", "--disable-gpu", "--hide-scrollbars", "--no-first-run",
                        f"--user-data-dir={profile}", "--force-device-scale-factor=1", f"--window-size={w},{h}",
                        "--virtual-time-budget=10000", "--allow-file-access-from-files", "--run-all-compositor-stages-before-draw",
                        f"--screenshot={out}", url], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=120)
    if not os.path.exists(out):
        sys.exit(f"Chrome didn't write {out}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("folder")
    ap.add_argument("--size", default="1080x1440")
    a = ap.parse_args()
    w, h = (int(v) for v in a.size.lower().split("x"))
    folder = os.path.abspath(a.folder)
    slides = sorted(glob.glob(os.path.join(folder, "slide-*.html")))
    if not slides:
        sys.exit(f"No slide-*.html files in {folder}")
    chrome = find_chrome()
    os.makedirs(os.path.join(folder, "png"), exist_ok=True)
    for s in slides:
        out = os.path.join(folder, "png", os.path.basename(s)[:-5] + ".png")
        shoot(chrome, "file://" + s, out, w, h)
        print("rendered", os.path.relpath(out))

    # contact sheet: every slide in #check mode, scaled down in a grid
    cols = 4 if len(slides) > 6 else min(len(slides), 3)
    rows = -(-len(slides) // cols)
    tw = 360; th = round(tw * h / w); gap = 28; lab = 34
    sw = cols * tw + (cols + 1) * gap; sh = rows * (th + lab) + (rows + 1) * gap
    cells = "".join(
        f'<div class="c"><div class="t"><iframe src="file://{s}#check" width="{w}" height="{h}" scrolling="no"></iframe></div>'
        f'<div class="n">{i + 1}. {os.path.basename(s)}</div></div>' for i, s in enumerate(slides))
    sheet = os.path.join(folder, ".sheet.html")
    with open(sheet, "w") as f:
        f.write(f"""<!doctype html><meta charset="utf-8"><style>
body{{margin:0;background:#1b1b1b;font:500 20px/1 -apple-system,system-ui,sans-serif;color:#bbb}}
.g{{display:grid;grid-template-columns:repeat({cols},{tw}px);gap:{gap}px;padding:{gap}px}}
.t{{width:{tw}px;height:{th}px;overflow:hidden;border-radius:6px}}
iframe{{border:0;transform:scale({tw / w});transform-origin:0 0;pointer-events:none}}
.n{{height:{lab}px;padding-top:10px}}</style><div class="g">{cells}</div>""")
    out = os.path.join(folder, "sheet.png")
    shoot(chrome, "file://" + sheet, out, sw, sh)
    os.remove(sheet)
    print("contact sheet", os.path.relpath(out), "(red outlines = something doesn't fit)")


if __name__ == "__main__":
    main()
