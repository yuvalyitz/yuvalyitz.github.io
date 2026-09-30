#!/usr/bin/env python3
"""Export web photographs and a Jekyll gallery manifest.

Requires ImageMagick, ExifTool, FFmpeg, and PyYAML. Originals are backed up
under local/pre-cleanup before their first export; that folder is never published.
Run from the repository root. Repeated runs always use the preserved originals.
"""
from pathlib import Path
from urllib.parse import quote
import shutil
import subprocess
import yaml

ROOT = Path(__file__).resolve().parent.parent
BACKUP = ROOT / 'local/pre-cleanup'
ALBUMS = [
    ('construction', 'Concrete Work at Elwood, Melbourne'),
    ('alps', 'Pointe Helbronner, Mont Blanc'), ('elma', 'Elma'),
    ('ramon', 'Mitzpe Ramon, Timna Park'), ('rajasthan', 'Rajasthan'),
    ('amos', 'Concrete Formwork in Tel-Aviv'), ('lanzarote', 'Lanzarote'),
    ('nz', 'New Zealand'), ('fiji', 'Fiji'), ('berlin', 'Berlin'),
]


def run(*args):
    subprocess.run([str(a) for a in args], check=True, stdout=subprocess.DEVNULL)


def preserve(path):
    original = BACKUP / path.relative_to(ROOT)
    original.parent.mkdir(parents=True, exist_ok=True)
    if not original.exists():
        shutil.copy2(path, original)
    return original


def dimensions(path):
    output = subprocess.check_output(['magick', 'identify', '-format', '%w %h', str(path) + '[0]'], text=True)
    return [int(n) for n in output.split()]


def main():
    albums = []
    for slug, title in ALBUMS:
        directory = ROOT / 'images/photography' / slug
        images = []
        for path in sorted(directory.iterdir()):
            if path.suffix.lower() not in {'.jpg', '.jpeg', '.png', '.gif', '.webp'}:
                continue
            if path.name.endswith('.export.webp') or (path.suffix.lower() == '.webp' and path.with_suffix('.gif').exists()):
                continue
            original = preserve(path)
            if path.suffix.lower() == '.gif':
                target = path.with_suffix('.webp')
                temporary = target.with_name(target.stem + '.export.webp')
                run('ffmpeg', '-v', 'error', '-y', '-i', original,
                    '-vf', "scale='min(1400,iw)':-2:flags=lanczos", '-c:v', 'libwebp_anim',
                    '-quality', '78', '-loop', '0', '-map_metadata', '-1', temporary)
                temporary.replace(target)
                path.unlink()
                path = target
            elif path.suffix.lower() != '.webp':
                run('magick', original, '-auto-orient', '-resize', '2400x2400>',
                    '-strip', '-quality', '85', path)
            # Animated WebP is retained intact on subsequent exports.
            thumb = ROOT / 'images/thumbnails' / slug / (path.name + '.webp')
            thumb.parent.mkdir(parents=True, exist_ok=True)
            run('magick', str(path) + '[0]', '-resize', '640x640>', '-strip', '-quality', '80', thumb)
            width, height = dimensions(path)
            images.append({
                'src': '/' + quote(path.relative_to(ROOT).as_posix()),
                'thumbnail': '/' + quote(thumb.relative_to(ROOT).as_posix()),
                'width': width, 'height': height,
                'alt': f'{title} — photograph {len(images) + 1}',
            })
        albums.append({'slug': slug, 'title': title, 'images': images})
        print(f'{slug}: {len(images)} photographs', flush=True)
    (ROOT / '_data/albums.yml').write_text(yaml.safe_dump(albums, allow_unicode=True, sort_keys=False))
    # Losslessly remove metadata from non-gallery assets, preserving ICC color profiles.
    paths = [p for p in (ROOT / 'images').rglob('*')
             if p.suffix.lower() in {'.jpg', '.jpeg', '.png', '.webp', '.gif'}
             and 'photography' not in p.parts and 'thumbnails' not in p.parts]
    for path in paths:
        preserve(path)
    if paths:
        run('exiftool', '-overwrite_original', '-all=', '-tagsFromFile', '@', '-ICC_Profile', *paths)


if __name__ == '__main__':
    main()
