from pathlib import Path
import json
import numpy as np
from PIL import Image, ImageDraw, ImageFilter
from scipy import ndimage

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / 'design-preference/pixlor-assets'
OUTPUT = ROOT / 'public/images/official/desktop'
FILES = list(SOURCE.rglob('*.png'))
manifest = []


def source(folder, prefix):
    return next(p for p in FILES if p.parent.name == folder and p.name.startswith(prefix))


def extract(name, folder, prefix, bounds=None, treatment='checker'):
    path = source(folder, prefix)
    image = Image.open(path)
    if bounds:
        image = image.crop(bounds)
    image = image.convert('RGBA')
    data = np.array(image)
    if treatment == 'checker':
        rgb = data[:, :, :3].astype(np.int16)
        tolerance = 16 if name.startswith('characters/') or name.endswith('bunny') else 45
        neutral = (rgb.max(2) - rgb.min(2) < tolerance) & (rgb.min(2) > 165)
        if name.startswith('confirm/') and name != 'confirm/panel':
            neutral |= (rgb[:, :, 0] > 220) & (rgb[:, :, 1] > 190) & (rgb[:, :, 2] > 130)
        edge = np.zeros(neutral.shape, dtype=bool)
        edge[0] = neutral[0]
        edge[-1] = neutral[-1]
        edge[:, 0] = neutral[:, 0]
        edge[:, -1] = neutral[:, -1]
        outside = ndimage.binary_propagation(edge, mask=neutral)
        foreground = ndimage.binary_fill_holes(~outside)
        if name == 'characters/store':
            protection = Image.new('L', image.size)
            ImageDraw.Draw(protection).polygon([(600, 111), (610, 88), (640, 65), (670, 59), (690, 60), (708, 53), (720, 63), (739, 65), (753, 83), (771, 88), (785, 111), (795, 141), (796, 198), (760, 235), (702, 246), (638, 229), (598, 196)], fill=255)
            foreground |= np.array(protection) > 0
        labels, _ = ndimage.label(foreground)
        sizes = np.bincount(labels.ravel())
        foreground &= sizes[labels] > 150
        image.putalpha(Image.fromarray((foreground * 255).astype('uint8')).filter(ImageFilter.GaussianBlur(.3)))
        if name in ('confirm/panel', 'success/panel'):
            protected = Image.new('L', image.size)
            draw = ImageDraw.Draw(protected)
            draw.rounded_rectangle((40, 55, image.width - 40, image.height - 20), radius=20, fill=255)
            for x, y in [(45, image.height - 40), (image.width - 45, image.height - 40)]:
                draw.ellipse((x - 25, y - 25, x + 25, y + 25), fill=255)
            draw.ellipse((image.width // 2 - 55, 8, image.width // 2 + 55, 80), fill=255)
            alpha = np.array(image.getchannel('A'))
            lilac = (rgb[:, :, 0] > 175) & (rgb[:, :, 1] > 120) & (rgb[:, :, 2] > 180) & (rgb.max(2) - rgb.min(2) < 110)
            alpha[(neutral | lilac) & (np.array(protected) == 0)] = 0
            crystals = Image.new('L', image.size)
            crystal_draw = ImageDraw.Draw(crystals)
            for points in ([(45, 20), (72, 43), (65, 66), (43, 66), (35, 47)], [(image.width - 45, 20), (image.width - 72, 43), (image.width - 65, 66), (image.width - 43, 66), (image.width - 35, 47)]):
                crystal_draw.polygon(points, fill=255)
            alpha[np.array(crystals) > 0] = 255
            image.putalpha(Image.fromarray(alpha))
    elif treatment == 'alpha':
        data[:, :, 3] = np.where(data[:, :, 3] > 200, 255, np.where(data[:, :, 3] < 20, 0, data[:, :, 3]))
        image = Image.fromarray(data)
    elif treatment == 'card':
        mask = Image.new('L', image.size)
        ImageDraw.Draw(mask).rounded_rectangle((1, 1, image.width - 2, image.height - 2), radius=30, fill=255)
        image.putalpha(mask)
    else:
        image = image.convert('RGB')
    if name == 'auth/panel':
        ImageDraw.Draw(image).rounded_rectangle((85, 153, 574, 590), radius=32, fill=(255, 232, 207, 255))
    if name == 'auth/register':
        data = np.array(image)
        for row in range(15, 65):
            data[row, 78:329, :3] = np.median(data[row, 335:345, :3], axis=0)
        image = Image.fromarray(data)
    clear = {
        'branding/main': [(250, 243, 440, 275)],
        'auth/panel': [(0, 0, 220, 43), (445, 0, 658, 43), (640, 90, 658, 620)],
        'upload/panel': [(0, 0, 115, 65), (0, 414, 350, 475)],
    }
    for bounds_to_clear in clear.get(name, []):
        ImageDraw.Draw(image).rectangle(bounds_to_clear, fill=(0, 0, 0, 0))
    if name == 'upload/panel':
        wood = image.crop((350, 414, 440, 435))
        for x in range(35, 350, 90):
            image.paste(wood.crop((0, 0, min(90, 350 - x), 21)), (x, 414))
    if name == 'upload/submit':
        mask = Image.new('L', image.size)
        ImageDraw.Draw(mask).rounded_rectangle((8, 10, 616, 112), radius=51, fill=255)
        image.putalpha(mask)
    target = OUTPUT / f'{name}.webp'
    target.parent.mkdir(parents=True, exist_ok=True)
    image.save(target, 'WEBP', lossless=True)
    manifest.append({'asset': str(target.relative_to(ROOT)).replace('\\', '/'), 'source': str(path.relative_to(ROOT)).replace('\\', '/'), 'crop': bounds, 'treatment': treatment, 'width': image.width, 'height': image.height})


extract('backgrounds/auth', 'Horizontal 1', 'Reino', treatment='opaque')
extract('backgrounds/upload', 'Horizontal 1', 'Reino', treatment='opaque')
extract('backgrounds/store', 'Horizontal 4', 'Islas', treatment='opaque')
extract('backgrounds/menu', 'Horizontal 1', 'Reino', treatment='opaque')
extract('branding/main', 'Horizontal 1', 'Kit', (15, 5, 681, 280), 'alpha')
extract('characters/auth', 'Horizontal 1', 'Kit', (690, 0, 1536, 413), 'alpha')
extract('auth/panel', 'Horizontal 1', 'Kit', (18, 248, 676, 902), 'alpha')
extract('auth/login', 'Horizontal 1', 'Kit', (665, 412, 1060, 488), 'alpha')
extract('auth/register', 'Horizontal 1', 'Kit', (665, 412, 1060, 488), 'alpha')
extract('upload/bunny', 'horizontal 2', 'Kit', (0, 265, 339, 608))
extract('characters/upload', 'horizontal 2', 'Kit', (337, 309, 940, 620))
extract('upload/title', 'horizontal 2', 'Kit', (611, 22, 1121, 217))
extract('upload/panel', 'horizontal 2', 'Kit', (943, 223, 1536, 698))
extract('upload/options', 'horizontal 2', 'Kit', (50, 628, 596, 785))
extract('upload/submit', 'horizontal 2', 'Kit', (626, 628, 1250, 745))
extract('branding/upload', 'horizontal 2', 'Kit', (13, 20, 611, 263))
extract('branding/store', 'Horizontal 3', 'Hoja', (14, 20, 590, 259))
extract('characters/store', 'Horizontal 3', 'Hoja', (583, 10, 1468, 301))
extract('store/banner', 'Horizontal 3', 'Hoja', (13, 263, 586, 445))
for name, bounds in zip(['pen', 'notebook', 'keychain', 'stickers', 'cap', 'shirt'], [(27, 452, 269, 715), (280, 452, 522, 715), (534, 452, 762, 715), (773, 452, 1010, 715), (1021, 452, 1263, 715), (1273, 452, 1513, 715)]):
    extract(f'store/{name}', 'Horizontal 3', 'Hoja', bounds, 'card')
extract('confirm/panel', 'Horizontal 5', 'Hoja', (545, 339, 1114, 646))
extract('confirm/accept', 'Horizontal 5', 'Hoja', (606, 510, 835, 604))
extract('confirm/cancel', 'Horizontal 5', 'Hoja', (836, 510, 1065, 604))
extract('success/panel', 'horizontal 6', 'Hoja', (620, 351, 1230, 638))
extract('success/bunny', 'horizontal 6', 'Hoja', (1231, 357, 1517, 621))
extract('success/whatsapp', 'horizontal 6', 'Hoja', (788, 704, 1253, 826))
extract('success/return', 'horizontal 6', 'Hoja', (795, 874, 1247, 950))
(OUTPUT / 'manifest.json').write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding='utf-8')
print(f'Extracted {len(manifest)} desktop assets.')
