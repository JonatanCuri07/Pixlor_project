from pathlib import Path
import json
import numpy as np
from PIL import Image, ImageFilter, ImageDraw
from scipy import ndimage

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / 'design-preference' / 'pixlor-assets'
OUTPUT = ROOT / 'public' / 'images' / 'official'
SHEETS = {index: next((SOURCE / f'{index} vertical').glob('*.png')) for index in range(1, 7)}
ASSETS = [
    ('backgrounds/auth', 1, (18, 20, 458, 951), 'opaque'),
    ('backgrounds/upload', 2, (33, 78, 473, 965), 'opaque'),
    ('backgrounds/menu', 3, (10, 10, 509, 954), 'opaque'),
    ('backgrounds/store', 4, (10, 13, 464, 964), 'opaque'),
    ('backgrounds/confirm', 5, (11, 10, 491, 951), 'opaque'),
    ('backgrounds/success', 6, (17, 20, 463, 942), 'opaque'),
    ('branding/main', 3, (516, 45, 992, 253), 'alpha'),
    ('branding/upload', 2, (486, 31, 1043, 268), 'alpha'),
    ('branding/store', 4, (473, 7, 963, 240), 'checker'),
    ('branding/confirm', 5, (510, 15, 973, 199), 'checker'),
    ('branding/success', 6, (487, 29, 994, 221), 'alpha'),
    ('characters/auth', 1, (478, 24, 1075, 354), 'checker'),
    ('characters/upload', 2, (474, 273, 1136, 508), 'alpha'),
    ('characters/menu', 3, (979, 8, 1536, 318), 'alpha'),
    ('characters/store', 4, (948, 18, 1525, 247), 'checker'),
    ('characters/confirm', 5, (910, 48, 1528, 284), 'checker'),
    ('characters/success', 6, (961, 40, 1535, 305), 'alpha'),
    ('auth/panel', 1, (482, 426, 1058, 896), 'checker'),
    ('auth/email', 1, (1096, 108, 1509, 193), 'checker'),
    ('auth/password', 1, (1096, 210, 1509, 297), 'checker'),
    ('auth/login', 1, (1083, 475, 1527, 584), 'checker'),
    ('auth/google', 1, (1098, 706, 1509, 790), 'checker'),
    ('auth/facebook', 1, (1098, 792, 1509, 879), 'checker'),
    ('menu/panel', 3, (514, 327, 1025, 895), 'alpha'),
    ('menu/profile', 3, (1042, 383, 1524, 501), 'alpha'),
    ('menu/store', 3, (1044, 573, 1525, 688), 'alpha'),
    ('menu/logout', 3, (1044, 763, 1525, 887), 'alpha'),
    ('upload/title', 2, (1044, 82, 1529, 294), 'alpha'),
    ('upload/counter', 2, (1218, 381, 1466, 483), 'alpha'),
    ('upload/panel', 2, (486, 511, 1080, 862), 'alpha'),
    ('upload/options', 2, (1078, 578, 1528, 762), 'alpha'),
    ('upload/submit', 2, (506, 865, 1072, 974), 'alpha'),
    ('upload/note', 2, (1096, 880, 1511, 946), 'alpha'),
    ('store/banner', 4, (477, 254, 1070, 448), 'checker'),
    ('store/counter', 4, (1085, 317, 1314, 416), 'checker'),
    ('navigation/back', 4, (1377, 314, 1480, 416), 'checker'),
    ('store/stripe', 4, (488, 475, 1281, 534), 'checker'),
    ('store/pen', 4, (479, 576, 645, 803), 'card'),
    ('store/notebook', 4, (652, 576, 818, 803), 'card'),
    ('store/keychain', 4, (826, 576, 993, 803), 'card'),
    ('store/stickers', 4, (1001, 576, 1167, 803), 'card'),
    ('store/cap', 4, (1175, 576, 1342, 803), 'card'),
    ('store/shirt', 4, (1351, 576, 1520, 803), 'card'),
    ('store/help', 4, (520, 857, 1176, 959), 'checker'),
    ('confirm/banner', 5, (564, 267, 1174, 464), 'checker'),
    ('confirm/panel', 5, (569, 480, 1278, 779), 'checker'),
    ('confirm/accept', 5, (585, 827, 964, 955), 'checker'),
    ('confirm/cancel', 5, (1013, 826, 1408, 955), 'checker'),
    ('success/banner', 6, (484, 296, 1086, 474), 'alpha'),
    ('success/panel', 6, (483, 525, 1120, 940), 'alpha'),
    ('success/whatsapp', 6, (1127, 576, 1513, 698), 'alpha'),
    ('success/return', 6, (1131, 777, 1522, 860), 'alpha'),
]


def remove_checker(image, name):
    data = np.asarray(image.convert('RGB')).astype(np.int16)
    tolerance = 8 if name.startswith('characters/') else 35
    neutral = (data.max(axis=2) - data.min(axis=2) < tolerance) & (data.min(axis=2) > 165)
    edge = np.zeros(neutral.shape, dtype=bool)
    edge[0, :] = neutral[0, :]
    edge[-1, :] = neutral[-1, :]
    edge[:, 0] = neutral[:, 0]
    edge[:, -1] = neutral[:, -1]
    outside = ndimage.binary_propagation(edge, mask=neutral)
    foreground = ndimage.binary_fill_holes(~outside)
    protection = Image.new('L', image.size)
    panda_regions = {
        'characters/confirm': ((390, 12), [(12, 99), (30, 73), (49, 54), (77, 44), (98, 43), (108, 34), (122, 34), (133, 47), (143, 57), (153, 75), (159, 103), (159, 132), (148, 150), (129, 168), (101, 176), (68, 174), (36, 162), (16, 142), (6, 122)]),
    }
    if name in panda_regions:
        (offset_x, offset_y), points = panda_regions[name]
        ImageDraw.Draw(protection).polygon([(x + offset_x, y + offset_y) for x, y in points], fill=255)
    foreground |= ndimage.binary_erosion(np.array(protection) > 0, iterations=3)
    foreground = ndimage.binary_fill_holes(foreground)
    foreground = ndimage.binary_closing(foreground, iterations=1, border_value=1)
    regions, count = ndimage.label(foreground)
    sizes = np.bincount(regions.ravel())
    foreground &= sizes[regions] > 130
    alpha = Image.fromarray((foreground * 255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(.35))
    result = image.convert('RGBA')
    result.putalpha(alpha)
    return result


def isolate_card(image):
    mask = Image.new('L', image.size)
    ImageDraw.Draw(mask).rounded_rectangle((2, 2, image.width - 2, image.height - 2), radius=24, fill=255)
    result = image.convert('RGBA')
    result.putalpha(mask)
    return result


manifest = []
for name, sheet, bounds, treatment in ASSETS:
    image = Image.open(SHEETS[sheet]).crop(bounds)
    if treatment == 'opaque':
        image = image.convert('RGB')
    elif treatment == 'checker':
        image = remove_checker(image, name)
    elif treatment == 'card':
        image = isolate_card(image)
    else:
        data = np.array(image)
        data[:, :, 3] = np.where(data[:, :, 3] > 200, 255, np.where(data[:, :, 3] < 20, 0, data[:, :, 3]))
        image = Image.fromarray(data)
    if name in ('auth/email', 'auth/password', 'auth/google', 'auth/facebook', 'store/help', 'store/counter', 'store/stripe', 'navigation/back'):
        mask = Image.new('L', image.size)
        draw = ImageDraw.Draw(mask)
        if name == 'navigation/back':
            draw.ellipse((9, 7, image.width - 4, image.height - 6), fill=255)
        else:
            bottom_inset = 14 if name in ('auth/password', 'auth/facebook') else 8
            side_inset = 8 if name == 'store/counter' else 5
            draw.rounded_rectangle((side_inset, 5, image.width - side_inset, image.height - bottom_inset), radius=(image.height - bottom_inset - 5) // 2, fill=255)
        image.putalpha(mask)
    if name in ('auth/email', 'auth/password'):
        data = np.array(image)
        for row in range(15, image.height - 15):
            data[row, 85:341, :3] = np.median(data[row, 74:84, :3], axis=0)
        image = Image.fromarray(data)
    clear_regions = {
        'branding/store': [(110, 191, 389, 233), (477, 0, 490, 233)],
        'branding/main': [(460, 130, 476, 208)],
        'branding/confirm': [(110, 166, 365, 184), (437, 160, 463, 184)],
        'branding/success': [(479, 140, 507, 192)],
        'characters/store': [(0, 200, 56, 229)],
        'characters/confirm': [(0, 0, 54, 128)],
        'characters/upload': [(555, 0, 662, 32)],
        'characters/success': [(0, 0, 23, 100)],
        'store/banner': [(100, 174, 480, 194)],
        'confirm/banner': [(145, 170, 501, 197), (425, 0, 610, 20)],
    }
    if name in clear_regions:
        data = np.array(image)
        for x1, y1, x2, y2 in clear_regions[name]:
            data[y1:y2, x1:x2, 3] = 0
        image = Image.fromarray(data)
    if name.startswith('branding/'):
        data = np.array(image)
        labels, count = ndimage.label(data[:, :, 3] > 100)
        sizes = np.bincount(labels.ravel())
        data[:, :, 3] = np.where(sizes[labels] > 1500, data[:, :, 3], 0)
        image = Image.fromarray(data)
    if name.startswith('characters/'):
        data = np.array(image)
        labels, count = ndimage.label(data[:, :, 3] > 100)
        sizes = np.bincount(labels.ravel())
        data[:, :, 3] = np.where(sizes[labels] > 200, data[:, :, 3], 0)
        image = Image.fromarray(data)
    target = OUTPUT / f'{name}.webp'
    target.parent.mkdir(parents=True, exist_ok=True)
    image.save(target, 'WEBP', lossless=True)
    manifest.append({'asset': str(target.relative_to(ROOT)).replace('\\', '/'), 'source': str(SHEETS[sheet].relative_to(ROOT)).replace('\\', '/'), 'crop': bounds, 'treatment': treatment, 'width': image.width, 'height': image.height})

source_menu = Image.open(SOURCE / 'menu mobile.png')
source_menu.save(OUTPUT / 'navigation' / 'menu.png')
manifest.append({'asset': 'public/images/official/navigation/menu.png', 'source': str((SOURCE / 'menu mobile.png').relative_to(ROOT)).replace('\\', '/'), 'treatment': 'original-alpha', 'width': source_menu.width, 'height': source_menu.height})
login = Image.open(OUTPUT / 'auth' / 'login.webp')
data = np.array(login)
for row in range(20, 92):
    data[row, 90:355, :3] = np.median(data[row, 365:380, :3], axis=0)
Image.fromarray(data).save(OUTPUT / 'auth' / 'register.webp', 'WEBP', lossless=True)
manifest.append({'asset': 'public/images/official/auth/register.webp', 'source': 'public/images/official/auth/login.webp', 'treatment': 'label-removed', 'width': login.width, 'height': login.height})
(OUTPUT / 'manifest.json').write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding='utf-8')
print(f'Extracted {len(ASSETS) + 2} assets from {len(SHEETS)} sheets and the menu icon.')
