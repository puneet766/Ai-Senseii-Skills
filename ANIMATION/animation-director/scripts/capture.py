#!/usr/bin/env python3
"""Records a one-file HTML animation frame by frame, so Claude can look at every picture it made.

A normal screen recording drops frames. This tool replaces the page's clock with a fake one and moves
it forward one exact step at a time, so every frame is perfect, however slow the computer is.

  python capture.py doctor
  python capture.py stills page.html --times 1,3,5,7 --size 1080x1920 --out stills
  python capture.py video  page.html --seconds 8 --size 1080x1920 --fps 30 --out out.mp4
  python capture.py sheet  out.mp4 --every 0.5 --out sheet.jpg
  python capture.py frame  out.mp4 --time 3.2 --out look.png
  python capture.py palette example.mp4 --out palette.png     (also works on a picture)

Needs: pip install playwright imageio-ffmpeg pillow   then   python -m playwright install chromium
"""
import argparse
import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

CLOCK = r"""
(() => {
  let now = 0, id = 1;
  const timers = new Map(), rafs = new Map(), t0 = 1700000000000, RealDate = Date;
  window.Date = class extends RealDate {
    constructor(...a) { if (a.length) super(...a); else super(t0 + now); }
    static now() { return t0 + now; }
  };
  performance.now = () => now;
  window.setTimeout = (f, d = 0, ...a) => { timers.set(id, {at: now + d, f, a}); return id++; };
  window.clearTimeout = i => timers.delete(i);
  window.setInterval = (f, d = 0, ...a) => { const me = id++; timers.set(me, {at: now + d, f, a, every: Math.max(1, d)}); return me; };
  window.clearInterval = i => timers.delete(i);
  window.requestAnimationFrame = f => { rafs.set(id, f); return id++; };
  window.cancelAnimationFrame = i => rafs.delete(i);
  window.__step = ms => {
    now += ms;
    for (const [i, x] of [...timers]) if (x.at <= now) {
      if (x.every) x.at += x.every; else timers.delete(i);
      try { x.f(...x.a); } catch (e) { console.error(e); }
    }
    const cur = [...rafs]; rafs.clear();
    for (const [, f] of cur) { try { f(now); } catch (e) { console.error(e); } }
    for (const a of document.getAnimations()) { try { a.pause(); a.currentTime = now; } catch (e) {} }
    for (const v of document.querySelectorAll('video')) { try { v.pause(); v.currentTime = now / 1000; } catch (e) {} }
    for (const s of document.querySelectorAll('svg')) { try { s.pauseAnimations(); s.setCurrentTime(now / 1000); } catch (e) {} }
  };
})();
"""


def fail(msg):
    print("PROBLEM: " + msg)
    sys.exit(1)


def find_ffmpeg():
    try:
        import imageio_ffmpeg
        return imageio_ffmpeg.get_ffmpeg_exe()
    except Exception:
        return shutil.which("ffmpeg")


def need_ffmpeg():
    exe = find_ffmpeg()
    if not exe:
        fail("ffmpeg is missing. Run: python -m pip install imageio-ffmpeg")
    return exe


def parse_size(text):
    try:
        w, h = text.lower().split("x")
        return int(w), int(h)
    except ValueError:
        fail("--size must look like 1080x1920")


def open_page(p, html, size):
    args = ["--enable-webgl", "--ignore-gpu-blocklist", "--enable-unsafe-swiftshader",
            "--autoplay-policy=no-user-gesture-required"]
    if sys.platform == "win32":
        args.append("--use-angle=d3d11")
    browser = p.chromium.launch(headless=True, args=args)
    page = browser.new_page(viewport={"width": size[0], "height": size[1]})
    errors = []
    page.on("pageerror", lambda e: errors.append(str(e)))
    page.on("console", lambda m: errors.append(m.text) if m.type == "error" else None)
    page.add_init_script(CLOCK)
    page.goto(Path(html).resolve().as_uri(), timeout=120000)
    page.evaluate("document.fonts ? document.fonts.ready : null")
    return browser, page, errors


def playwright_or_fail():
    try:
        from playwright.sync_api import sync_playwright
        return sync_playwright
    except ImportError:
        fail("Playwright is missing. Run: python -m pip install playwright imageio-ffmpeg "
             "then: python -m playwright install chromium")


def report_errors(errors):
    if errors:
        print(f"PAGE ERRORS: {len(errors)}. The first ones:")
        for e in errors[:5]:
            print("  " + e[:300])
    else:
        print("Page errors: none")


def looks_blank(path):
    """True when a picture is one flat colour, which nearly always means nothing was drawn."""
    try:
        from PIL import Image, ImageStat
    except ImportError:
        return False
    with Image.open(path) as im:
        return ImageStat.Stat(im.convert("L").resize((48, 48))).stddev[0] < 1.5


def cmd_doctor(_):
    ok = True
    try:
        from playwright.sync_api import sync_playwright
        with sync_playwright() as p:
            b = p.chromium.launch(headless=True)
            b.close()
        print("Browser: ready")
    except Exception as e:
        ok = False
        print("Browser: NOT ready. " + str(e).splitlines()[0][:160])
        print("  Fix: python -m pip install playwright imageio-ffmpeg pillow")
        print("       python -m playwright install chromium")
    ffmpeg = find_ffmpeg()
    print("Video maker: " + ("ready" if ffmpeg else "NOT ready. Fix: python -m pip install imageio-ffmpeg"))
    print("ALL READY" if ok and ffmpeg else "NOT READY")
    sys.exit(0 if ok and ffmpeg else 1)


def cmd_stills(a):
    sync_playwright = playwright_or_fail()
    size = parse_size(a.size)
    times = sorted(float(t) for t in a.times.split(","))
    out = Path(a.out)
    out.mkdir(parents=True, exist_ok=True)
    step = 1000 / a.fps
    with sync_playwright() as p:
        browser, page, errors = open_page(p, a.html, size)
        now = 0.0
        for i, t in enumerate(times, 1):
            while now < t * 1000 - step / 2:
                page.evaluate(f"window.__step({step})")
                now += step
            path = out / f"still-{i}-{t:.1f}s.png"
            page.screenshot(path=str(path))
            print(f"Saved {path}" + ("   WARNING: this picture looks blank" if looks_blank(path) else ""))
        browser.close()
    report_errors(errors)


def cmd_video(a):
    sync_playwright = playwright_or_fail()
    ffmpeg = need_ffmpeg()
    size = parse_size(a.size)
    total = int(round(a.seconds * a.fps))
    step = 1000 / a.fps
    with tempfile.TemporaryDirectory(prefix="animation-frames-") as tmp:
        with sync_playwright() as p:
            browser, page, errors = open_page(p, a.html, size)
            for i in range(total):
                page.evaluate(f"window.__step({step})")
                page.screenshot(path=os.path.join(tmp, f"{i:05d}.jpg"), type="jpeg", quality=95)
                if (i + 1) % max(1, total // 10) == 0:
                    print(f"Recorded {i + 1} of {total} frames", flush=True)
            browser.close()
        out = Path(a.out)
        out.parent.mkdir(parents=True, exist_ok=True)
        subprocess.run([ffmpeg, "-v", "error", "-y", "-framerate", str(a.fps), "-i",
                        os.path.join(tmp, "%05d.jpg"), "-c:v", "libx264", "-crf", "16",
                        "-pix_fmt", "yuv420p", "-movflags", "+faststart", str(out)], check=True)
    print(f"Saved {out}: {total} frames, {a.seconds} seconds, no sound")
    report_errors(errors)


def cmd_sheet(a):
    ffmpeg = need_ffmpeg()
    out = Path(a.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    vf = (f"fps=1/{a.every},scale={a.width}:-2,"
          f"drawtext=text='%{{pts\\:hms}}':x=6:y=6:fontsize=20:fontcolor=white:box=1:boxcolor=black@0.6,"
          f"tile={a.columns}x{a.rows}:padding=4")
    r = subprocess.run([ffmpeg, "-v", "error", "-y", "-i", a.video, "-vf", vf, "-q:v", "3", "-update", "1",
                        "-frames:v", "1", str(out)], capture_output=True, text=True)
    if r.returncode:  # some ffmpeg builds have no drawtext
        vf = f"fps=1/{a.every},scale={a.width}:-2,tile={a.columns}x{a.rows}:padding=4"
        subprocess.run([ffmpeg, "-v", "error", "-y", "-i", a.video, "-vf", vf, "-q:v", "3", "-update", "1",
                        "-frames:v", "1", str(out)], check=True)
        print("Note: this sheet has no time labels. Pictures run left to right, top to bottom.")
    print(f"Saved {out}: one picture every {a.every} seconds")


def cmd_frame(a):
    ffmpeg = need_ffmpeg()
    out = Path(a.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    subprocess.run([ffmpeg, "-v", "error", "-y", "-ss", str(a.time), "-i", a.video, "-frames:v", "1",
                    "-update", "1", str(out)], check=True)
    print(f"Saved {out}")


def cmd_palette(a):
    """Prints the main colours of a picture or a video as hex codes, biggest area first, and saves a swatch picture."""
    try:
        from PIL import Image, ImageDraw
    except ImportError:
        fail("Pillow is missing. Run: python -m pip install pillow")
    src = Path(a.source)
    if not src.exists():
        fail(f"can't find {src}")
    tiles = []
    if src.suffix.lower() in (".png", ".jpg", ".jpeg", ".webp", ".bmp", ".gif"):
        with Image.open(src) as im:
            tiles.append(im.convert("RGB").resize((160, 160)))
    else:
        ffmpeg = need_ffmpeg()
        with tempfile.TemporaryDirectory(prefix="animation-palette-") as tmp:
            subprocess.run([ffmpeg, "-v", "error", "-y", "-i", str(src), "-vf", "fps=1,scale=160:160", "-frames:v", "24",
                            os.path.join(tmp, "%03d.png")], check=True)
            for f in sorted(Path(tmp).glob("*.png")):
                with Image.open(f) as im:
                    tiles.append(im.convert("RGB").copy())
        if not tiles:
            fail("couldn't read any picture from that file")
    strip = Image.new("RGB", (160 * len(tiles), 160))
    for i, t in enumerate(tiles):
        strip.paste(t, (i * 160, 0))
    # 48 fine clusters first, so thin lines and small bright things keep their own colour
    q = strip.quantize(colors=48, method=Image.Quantize.FASTOCTREE)
    pal = q.getpalette()
    counts = q.getcolors()
    total = sum(c for c, _ in counts)
    cols = [(c / total, tuple(pal[i * 3:i * 3 + 3])) for c, i in counts]

    def far(rgb, chosen, gap):
        return all(sum((x - y) ** 2 for x, y in zip(rgb, o)) > gap * gap for _, o in chosen)

    def strength(rgb):  # how vivid a colour is: saturation times brightness
        mx, mn = max(rgb), min(rgb)
        return ((mx - mn) / mx if mx else 0) * (mx / 255)

    areas = []
    for share, rgb in sorted(cols, reverse=True):
        if far(rgb, areas, 40):
            areas.append((share, rgb))
        if len(areas) >= a.colours:
            break
    accents = []
    for share, rgb in sorted(cols, key=lambda x: strength(x[1]), reverse=True):
        if share >= 0.002 and strength(rgb) > 0.25 and far(rgb, accents, 60) and far(rgb, areas[:3], 60):
            accents.append((share, rgb))
        if len(accents) >= 5:
            break
    hx = lambda rgb: "#%02X%02X%02X" % rgb
    out = Path(a.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    rows = [("area", x) for x in areas] + [("accent", x) for x in accents]
    sw = Image.new("RGB", (150 * len(rows), 200), "white")
    d = ImageDraw.Draw(sw)
    for i, (kind, (share, rgb)) in enumerate(rows):
        d.rectangle([i * 150, 0, i * 150 + 149, 150], fill=rgb)
        d.text((i * 150 + 6, 156), f"{hx(rgb)} {share:.0%}", fill="black")
        d.text((i * 150 + 6, 174), kind, fill="black")
    sw.save(out)
    print("Biggest areas (the ground and the main shapes):")
    for share, rgb in areas:
        print(f"  {hx(rgb)}  {share:.0%}")
    print("Strongest accents (small, vivid things: lines, glows, highlights):")
    for share, rgb in accents:
        print(f"  {hx(rgb)}  {share:.1%}")
    if not accents:
        print("  none found: this picture has no vivid colour")
    print(f"Saved {out}")
    print("Note: very thin lines still read a little duller than they look. Compare with the picture.")


def main():
    ap = argparse.ArgumentParser(description="Record a one-file HTML animation and check its frames.")
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("doctor", help="check that everything is installed").set_defaults(fn=cmd_doctor)

    s = sub.add_parser("stills", help="save single pictures at chosen seconds")
    s.add_argument("html"); s.add_argument("--times", required=True)
    s.add_argument("--size", default="1080x1920"); s.add_argument("--fps", type=int, default=30)
    s.add_argument("--out", default="stills"); s.set_defaults(fn=cmd_stills)

    v = sub.add_parser("video", help="record the whole animation to MP4")
    v.add_argument("html"); v.add_argument("--seconds", type=float, required=True)
    v.add_argument("--size", default="1080x1920"); v.add_argument("--fps", type=int, default=30)
    v.add_argument("--out", default="out.mp4"); v.set_defaults(fn=cmd_video)

    h = sub.add_parser("sheet", help="make one image holding many frames, for checking")
    h.add_argument("video"); h.add_argument("--every", type=float, default=0.5)
    h.add_argument("--width", type=int, default=270); h.add_argument("--columns", type=int, default=6)
    h.add_argument("--rows", type=int, default=4); h.add_argument("--out", default="sheet.jpg")
    h.set_defaults(fn=cmd_sheet)

    f = sub.add_parser("frame", help="save one full-size frame from the video")
    f.add_argument("video"); f.add_argument("--time", type=float, required=True)
    f.add_argument("--out", default="look.png"); f.set_defaults(fn=cmd_frame)

    c = sub.add_parser("palette", help="list the main colours of a picture or a video")
    c.add_argument("source"); c.add_argument("--colours", type=int, default=8)
    c.add_argument("--out", default="palette.png"); c.set_defaults(fn=cmd_palette)

    a = ap.parse_args()
    a.fn(a)


if __name__ == "__main__":
    main()
