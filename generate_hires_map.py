from PIL import Image, ImageFilter

import os
from glob import glob
from math import log2, ceil, sqrt
from shutil import rmtree

start_z = 10
image_size = 256
quality = 85

map_dir = '_map'
try: rmtree(map_dir)
except: pass

files = sorted(glob("data/hires/*.jpg", recursive=True))
try: os.mkdir(map_dir)
except: pass

# Гильберт
# Поиск ближайшего кводрата со стороной 2^n
l = len(files)
n = 2**ceil(log2(sqrt(l)))
def d2xy(d): 
    t = d
    x = y = 0
    s = 1
    while s < n:
        rx = 1 & (t//2)
        ry = 1 & (t ^ rx)
        # rot(s, x, y, rx, ry)
        if ry == 0:
            if rx == 1:
                x = s-1 - x
                y = s-1 - y
            x, y = y, x
        x += s * rx
        y += s * ry
        t = t//4
        s = s<<1
    return (x,y)


def imop(n, size=256):
    size = (size, size)
    print(n)
    try: img = Image.open(n).resize(size)
    except: img = Image.new("RGB", size)
    return img

def generate_base_zoom():
    z = start_z
    # s = ceil(sqrt(len(files)))
    s = 126
    #for i, f in enumerate(files):
    i = 0
    for a in range(0,2560):
        for b in range(1,7):
            # x,y = d2xy(i)
            x = i%s
            y = i//s
            f = f"data/hires/channel-{a}-{b}.jpg"
            im = imop(f, size=1024)
            w, h = im.size

            ww = w//256
            hh = h//256
            x = x*ww
            y = y*hh
            
            for k in range(0, ww):
                for l in range(0, hh):
                    bb = (k*256, l*256, (k+1)*256, (l+1)*256)
                    im.crop(bb).convert('RGB').save(f"{map_dir}/{z}-{y+l}-{x+k}.jpg", quality=quality)

            i = i+1

def generate_zoom_out():
    x = 0
    y = 0
    for z in range(start_z,1,-1):
        while True:
            while True:
                out = Image.new("RGB", (256,256))
                im00 = imop(f"{map_dir}/{z}-{x+0}-{y+0}.jpg", image_size//2)
                im01 = imop(f"{map_dir}/{z}-{x+1}-{y+0}.jpg", image_size//2)
                im10 = imop(f"{map_dir}/{z}-{x+0}-{y+1}.jpg", image_size//2)
                im11 = imop(f"{map_dir}/{z}-{x+1}-{y+1}.jpg", image_size//2)
                out.paste(im00, (  0,   0))
                out.paste(im10, (128,   0))
                out.paste(im01, (  0, 128))
                out.paste(im11, (128, 128))
                tile = f"{map_dir}/{z-1}-{x//2}-{y//2}.jpg"
                # out.save(tile, quality=quality)
                out.filter(ImageFilter.DETAIL).save(tile, quality=quality)
                x+=2
                if not os.path.isfile(f'{map_dir}/{z}-{x}-{y}.jpg'):
                    break;
            x=0
            y+=2
            if not os.path.isfile(f'{map_dir}/{z}-{x}-{y}.jpg'):
                break;
        y=0
        
generate_base_zoom()
generate_zoom_out()
