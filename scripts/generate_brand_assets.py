from __future__ import annotations

from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import math

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "brand"
OUT.mkdir(parents=True, exist_ok=True)

INK = "#070A12"
PANEL = "#101528"
WHITE = "#F7F9FF"
MUTED = "#A9B5D0"
CYAN = "#37E6FF"
VIOLET = "#8D6BFF"
MINT = "#63FFD1"
FONT_BOLD = "C:/Windows/Fonts/seguisb.ttf"
FONT_REG = "C:/Windows/Fonts/segoeui.ttf"


def font(size: int, bold: bool = False):
    return ImageFont.truetype(FONT_BOLD if bold else FONT_REG, size)


def gradient(size, left=(7, 10, 18), right=(17, 22, 47)):
    w, h = size
    im = Image.new("RGB", size)
    p = im.load()
    for x in range(w):
        t = x / max(1, w - 1)
        c = tuple(round(left[i] * (1 - t) + right[i] * t) for i in range(3))
        for y in range(h):
            p[x, y] = c
    return im


def field_mark(size: int, variant: str = "contours", transparent: bool = False):
    scale = 3
    s = size * scale
    base = Image.new("RGBA", (s, s), (0, 0, 0, 0) if transparent else (7, 10, 18, 255))
    glow = Image.new("RGBA", (s, s), (0, 0, 0, 0))
    gd = ImageDraw.Draw(glow)
    cx = cy = s / 2
    if variant == "contours":
        for i in range(7):
            r = s * (0.105 + i * 0.047)
            shift = math.sin(i * 0.8) * s * 0.010
            color = (55, 230, 255, 130) if i % 2 == 0 else (141, 107, 255, 125)
            box = (cx-r*1.12+shift, cy-r, cx+r*1.12+shift, cy+r)
            width=max(2, int(s*0.009))
            gd.arc(box, 12, 168, fill=color, width=width)
            gd.arc(box, 192, 348, fill=color, width=width)
        gd.ellipse((cx-s*.055, cy-s*.055, cx+s*.055, cy+s*.055), fill=(247,249,255,255))
        gd.ellipse((cx-s*.025, cy-s*.025, cx+s*.025, cy+s*.025), fill=(55,230,255,255))
    elif variant == "nodes":
        pts=[]
        for row in range(-2,3):
            for col in range(-2,3):
                x=cx+col*s*.11+(row%2)*s*.025
                y=cy+row*s*.11
                pts.append((x,y))
        for x,y in pts:
            for x2,y2 in pts:
                d=((x-x2)**2+(y-y2)**2)**.5
                if s*.08 < d < s*.15:
                    gd.line((x,y,x2,y2),fill=(141,107,255,70),width=max(2,int(s*.005)))
        for x,y in pts:
            rr=s*(.022 if abs(x-cx)+abs(y-cy)>1 else .05)
            gd.ellipse((x-rr,y-rr,x+rr,y+rr),fill=(55,230,255,220))
    else:
        for k in range(-4,5):
            points=[]
            for x in range(int(s*.13),int(s*.87),6):
                y=cy+k*s*.055+math.sin((x/s)*math.pi*4+k*.5)*s*.025*(1-abs(k)/6)
                points.append((x,y))
            gd.line(points,fill=(55,230,255,160) if k%2==0 else (141,107,255,145),width=max(2,int(s*.008)))
        gd.ellipse((cx-s*.045,cy-s*.045,cx+s*.045,cy+s*.045),fill=(247,249,255,255))
    blurred = glow.filter(ImageFilter.GaussianBlur(max(2, int(s*.025))))
    base.alpha_composite(blurred)
    base.alpha_composite(glow)
    if not transparent:
        mask = Image.new("L", (s,s), 0)
        ImageDraw.Draw(mask).rounded_rectangle((s*.035,s*.035,s*.965,s*.965),radius=s*.20,fill=255)
        clean=Image.new("RGBA",(s,s),(0,0,0,0)); clean.paste(base,(0,0),mask)
        base=clean
    return base.resize((size,size),Image.Resampling.LANCZOS)


def save_candidates():
    names=[("a-contours","contours"),("b-nodes","nodes"),("c-waves","waves")]
    cards=[]
    for name,var in names:
        im=field_mark(1024,var)
        im.save(OUT/f"logo-{name}-1024.png",optimize=True)
        thumb=im.resize((360,360),Image.Resampling.LANCZOS)
        cards.append((name,thumb))
    board=Image.new("RGB",(1200,520),(7,10,18)); d=ImageDraw.Draw(board)
    for i,(name,thumb) in enumerate(cards):
        x=30+i*390
        board.paste(thumb,(x,30),thumb)
        label=name.split('-',1)[1].title()
        d.text((x+180,420),label,font=font(34,True),fill=WHITE,anchor="mm")
    d.text((600,482),"BosonField Open — mark studies",font=font(26),fill=MUTED,anchor="mm")
    board.save(OUT/"logo-candidates.png",optimize=True)


def save_selected():
    mark=field_mark(1024,"contours")
    mark.save(OUT/"avatar-1024.png",optimize=True)
    mark.resize((512,512),Image.Resampling.LANCZOS).save(OUT/"avatar-512.png",optimize=True)
    mark.resize((400,400),Image.Resampling.LANCZOS).save(OUT/"avatar-400.png",optimize=True)
    transparent=field_mark(1024,"contours",transparent=True)
    transparent.save(OUT/"mark-transparent-1024.png",optimize=True)

    # X / general banner. The lower-left corner stays clear for X's profile-photo overlay.
    im=gradient((1500,500)); d=ImageDraw.Draw(im)
    glow=field_mark(340,"contours",transparent=True)
    im.paste(glow,(225,80),glow)
    d.text((610,130),"BosonField",font=font(88,True),fill=WHITE)
    d.text((612,232),"OPEN",font=font(28,True),fill=CYAN,stroke_width=1)
    d.text((610,300),"Open-source AI video, made usable.",font=font(36),fill=MUTED)
    im.save(OUT/"banner-1500x500.png",optimize=True)

    # YouTube banner. Every key item fits the 1546 x 423 center safe area:
    # x=507..2053 and y=508..931 on a 2560 x 1440 canvas.
    yt=gradient((2560,1440)); d=ImageDraw.Draw(yt)
    glow=field_mark(370,"contours",transparent=True)
    yt.paste(glow,(610,532),glow)
    d.text((1040,555),"BosonField",font=font(102,True),fill=WHITE)
    d.text((1044,670),"OPEN",font=font(31,True),fill=CYAN)
    d.text((1040,742),"Free tools. Clear lessons. Shared workflows.",font=font(38),fill=MUTED)
    d.rounded_rectangle((1040,825,1575,892),radius=28,outline=CYAN,width=3)
    d.text((1307,858),"BUILD WITH US",font=font(28,True),fill=WHITE,anchor="mm")
    yt.save(OUT/"youtube-banner-2560x1440.png",optimize=True)

    # Launch post template.
    sq=gradient((1080,1080)); d=ImageDraw.Draw(sq)
    m=field_mark(300,"contours",transparent=True)
    sq.paste(m,(70,65),m)
    d.text((80,410),"Make AI video\nwith free,\nopen tools.",font=font(78,True),fill=WHITE,spacing=10)
    d.text((82,735),"BosonField Open",font=font(36,True),fill=CYAN)
    d.text((82,800),"Free beginner lessons. Shared workflows.\nReal local hardware tests.",font=font(39),fill=MUTED,spacing=12)
    d.text((82,1000),"@bosonfieldopen",font=font(30,True),fill=WHITE)
    sq.save(OUT/"launch-card-1080.png",optimize=True)


if __name__ == "__main__":
    save_candidates()
    save_selected()
    print(f"generated={len(list(OUT.glob('*.png')))} output={OUT}")
