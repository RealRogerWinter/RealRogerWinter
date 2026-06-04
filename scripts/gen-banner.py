#!/usr/bin/env python3
"""Render the profile banner PNGs (dark + light) with Pillow.

Transparent background so the banner blends into GitHub's canvas in both
themes (no visible rectangle seam). Brand-aligned OFL fonts are fetched at
runtime from the google/fonts mirror, with a graceful fallback so the build
never hard-fails. Run from anywhere: it writes to ../assets relative to this file.
"""

import os
import sys
import urllib.request
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
ASSETS = os.path.normpath(os.path.join(HERE, "..", "assets"))
FONTS = os.path.join(HERE, ".fonts")
os.makedirs(ASSETS, exist_ok=True)
os.makedirs(FONTS, exist_ok=True)

# Brand
ACCENT = (91, 140, 255, 255)        # #5b8cff
DARK_NAME = (215, 224, 218, 255)    # #d7e0da  (light text for dark mode)
DARK_TAG = (126, 138, 131, 255)     # #7e8a83  (dim)
LIGHT_NAME = (26, 32, 28, 255)      # #1a201c  (dark ink for light mode)
LIGHT_TAG = (91, 107, 98, 255)      # #5b6b62  (dim)

W, H = 1200, 320
PAD = 64

# Variable OFL fonts (wght axis). google/fonts mirror.
FONT_SOURCES = {
    "display": "https://raw.githubusercontent.com/google/fonts/main/ofl/spacegrotesk/SpaceGrotesk%5Bwght%5D.ttf",
    "mono": "https://raw.githubusercontent.com/google/fonts/main/ofl/jetbrainsmono/JetBrainsMono%5Bwght%5D.ttf",
}

# Common system fallbacks if the fetch fails.
FALLBACKS = [
    "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
    "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
]


def fetch_font(kind):
    dest = os.path.join(FONTS, f"{kind}.ttf")
    if os.path.exists(dest) and os.path.getsize(dest) > 0:
        return dest
    try:
        req = urllib.request.Request(FONT_SOURCES[kind], headers={"User-Agent": "banner-gen"})
        with urllib.request.urlopen(req, timeout=20) as r:
            data = r.read()
        if len(data) < 1000:
            raise ValueError("font too small, likely an error page")
        with open(dest, "wb") as f:
            f.write(data)
        print(f"  fetched {kind} font ({len(data)} bytes)")
        return dest
    except Exception as e:
        print(f"  WARN: could not fetch {kind} font ({e}); using fallback")
        return None


def load_font(kind, size, weight=None):
    path = fetch_font(kind)
    if path is None:
        for fb in FALLBACKS:
            if os.path.exists(fb):
                return ImageFont.truetype(fb, size)
        return ImageFont.load_default()
    font = ImageFont.truetype(path, size)
    if weight is not None:
        try:
            font.set_variation_by_axes([weight])
        except Exception:
            pass  # not a variable font / axis unavailable
    return font


def render(out_path, name_color, tag_color):
    img = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    name_font = load_font("display", 84, weight=600)
    tag_font = load_font("mono", 30, weight=500)

    # Kicker accent rule (echoes the site's kicker leading-line).
    rule_y = 96
    draw.rectangle([PAD, rule_y, PAD + 60, rule_y + 5], fill=ACCENT)

    # Name
    name = "Roger Winter"
    name_y = rule_y + 24
    draw.text((PAD, name_y), name, font=name_font, fill=name_color)
    nb = draw.textbbox((PAD, name_y), name, font=name_font)

    # Tagline
    tagline = "AI-native developer"
    draw.text((PAD, nb[3] + 16), tagline, font=tag_font, fill=tag_color)

    img.save(out_path)
    print(f"  wrote {out_path}")


def main():
    print("Rendering banners...")
    render(os.path.join(ASSETS, "banner-dark.png"), DARK_NAME, DARK_TAG)
    render(os.path.join(ASSETS, "banner-light.png"), LIGHT_NAME, LIGHT_TAG)
    print("Done.")


if __name__ == "__main__":
    sys.exit(main())
