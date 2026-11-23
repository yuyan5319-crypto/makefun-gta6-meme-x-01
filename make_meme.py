#!/usr/bin/env python3
"""Compose the gta6-meme-x-01 meme: Vice City scene + make.fun's ghost
worked into the street scene + meme captions.

Inputs : assets/scene.png (AI-made Vice City boulevard, no text)
         assets/makefun-mark.png (make.fun's official ghost mark, press kit)
Output : meme.png (the post's first picture)
"""
from PIL import Image, ImageDraw, ImageFont, ImageFilter

W = 1600
FONT = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"

scene = Image.open("assets/scene.png").convert("RGBA").resize((W, W))

# --- the ghost, standing on the right-hand sidewalk -------------------------
ghost = Image.open("assets/makefun-mark.png").convert("RGBA")
gw = 470
gh = int(ghost.height * gw / ghost.width)
ghost = ghost.resize((gw, gh), Image.LANCZOS)
gx, gy = W - gw - 90, 1000  # feet on the pavement, beside the palm tree

shadow = Image.new("RGBA", (W, W), (0, 0, 0, 0))
sd = ImageDraw.Draw(shadow)
sd.ellipse([gx + 40, gy + gh - 46, gx + gw - 30, gy + gh + 6], fill=(30, 8, 40, 130))
scene.alpha_composite(shadow.filter(ImageFilter.GaussianBlur(10)))
scene.alpha_composite(ghost, (gx, gy))

# --- captions ---------------------------------------------------------------
draw = ImageDraw.Draw(scene)


def caption(text, y, size):
    font = ImageFont.truetype(FONT, size)
    box = draw.textbbox((0, 0), text, font=font, stroke_width=10)
    tw = box[2] - box[0]
    draw.text(((W - tw) / 2 - box[0], y), text, font=font, fill="white",
              stroke_width=10, stroke_fill="black")


caption("WAITED 13 YEARS FOR GTA 6", 36, 96)
caption("MY AI AGENT GOT PAID FIRST", 1330, 92)
caption("real USDC bounties on make.fun", 1448, 72)

scene.convert("RGB").save("meme.png")
print("wrote meme.png")
