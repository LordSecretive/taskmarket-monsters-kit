#!/usr/bin/env python3
"""Render your Taskmarket Monsters card to the set's video: a 6 s loop that joins up exactly, 1080 x 1512, 30 fps, H.264 MP4, plus a
PNG still taken mid-sweep (1.3 s), so it shows the foil. It draws card.html exactly as the browser does, one frame at a time.

  python3 render.py                 render the card in card.js to out/
  python3 render.py --check         also check the loop closes (the frame at 6 s against frame 0)

Needs: Python 3 with Playwright and Pillow (pip install playwright pillow, then playwright install chromium) and
ffmpeg. Render one card at a time."""
import argparse, pathlib, shutil, subprocess, sys, tempfile
try:
    from playwright.sync_api import sync_playwright
except ImportError:
    sys.exit('STOP: render.py needs Playwright: pip install playwright pillow, then playwright install chromium')
if not shutil.which('ffmpeg'):
    sys.exit('STOP: render.py needs ffmpeg on your PATH (on a Mac: brew install ffmpeg)')

HERE = pathlib.Path(__file__).resolve().parent
W, H, FPS, T = 1080, 1512, 30, 6


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--out', default=str(HERE / 'out'))
    ap.add_argument('--check', action='store_true')
    ap.add_argument('--example', action='store_true', help=argparse.SUPPRESS)   # our own re-renders of the example cards
    a = ap.parse_args()
    if a.check:
        try:
            from PIL import Image, ImageChops  # noqa: F401
        except ImportError:
            sys.exit('STOP: --check needs Pillow: pip install pillow')
    out = pathlib.Path(a.out); out.mkdir(parents=True, exist_ok=True)
    tmp = pathlib.Path(tempfile.mkdtemp(prefix='monster-'))
    with sync_playwright() as p:
        try:
            b = p.chromium.launch(args=['--allow-file-access-from-files', '--force-color-profile=srgb'])
        except Exception:
            b = p.chromium.launch(channel='chrome', args=['--allow-file-access-from-files', '--force-color-profile=srgb'])
        pg = b.new_page(viewport={'width': W, 'height': H}, device_scale_factor=1)
        warn = []
        pg.on('console', lambda m: warn.append(m.text) if m.type in ('warning', 'error') else None)
        pg.on('pageerror', lambda e: warn.append(str(e)))
        pg.goto((HERE / 'card.html').as_uri() + '?render=1' + ('&example=1' if a.example else ''))
        try:
            pg.wait_for_function('window.__ready === true', timeout=30000)
        except Exception:
            sys.exit('STOP: the card did not load. ' + (' | '.join(warn) or 'Check card.js and your monster file.'))
        if warn:
            sys.exit('STOP: ' + ' | '.join(warn))
        cv = pg.locator('#card')
        stem = pg.evaluate("`taskmarket-monster-${String(CARD.number).padStart(2,'0')}-${CARD.name.toLowerCase().replace(/[^a-z0-9]+/g,'-')}`")
        for i in range(FPS * T + (1 if a.check else 0)):
            pg.evaluate(f'window.__seek({i / FPS})')
            cv.screenshot(path=str(tmp / f'{i:04d}.png'))
            if i % 30 == 0:
                print(f'{i}/{FPS * T}', flush=True)
        b.close()
    shutil.copy(tmp / f'{round(1.3 * FPS):04d}.png', out / f'{stem}.png')   # the still: mid-sweep, so it shows the foil
    mp4 = out / f'{stem}.mp4'
    subprocess.run(['ffmpeg', '-v', 'error', '-y', '-framerate', str(FPS), '-i', str(tmp / '%04d.png'), '-frames:v', str(FPS * T),
                    '-c:v', 'libx264', '-preset', 'slow', '-crf', '18', '-pix_fmt', 'yuv420p', '-profile:v', 'high',
                    '-vf', 'scale=out_color_matrix=bt709:out_range=tv', '-colorspace', 'bt709', '-color_primaries', 'bt709',
                    '-color_trc', 'bt709', '-x264-params', 'colorprim=bt709:transfer=bt709:colormatrix=bt709', '-movflags', '+faststart', str(mp4)], check=True)
    if a.check:
        from PIL import Image, ImageChops
        d = ImageChops.difference(Image.open(tmp / '0000.png').convert('RGB'), Image.open(tmp / f'{FPS * T:04d}.png').convert('RGB'))
        print('loop check: largest pixel difference between 6 s and 0 s is', max(x for band in d.getextrema() for x in band), '(0 is a perfect loop)')
    shutil.rmtree(tmp)
    print(mp4, f'{mp4.stat().st_size / 1e6:.1f} MB')


if __name__ == '__main__':
    main()
