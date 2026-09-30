# Yuval Itzhaki’s academic website

```sh
LANG=en_US.UTF-8 LC_ALL=en_US.UTF-8 bundle exec jekyll serve --port 4000
```

Run from the repository root, then open http://localhost:4000.

Source for https://yuvalyitz.github.io, built with Jekyll and AcademicPages.

## First-time setup

Use Ruby 3.2 and Bundler, then install the pinned gems:

```sh
bundle install
```

Restart Jekyll after changing `_config.yml`.
Local previews do not load Google Analytics.

## Editing

- `_config.yml`: shared author details, site settings, and analytics.
- `_data/authors.yml`: photography avatar and bio overrides.
- `_data/navigation.yml`: main navigation.
- `_pages/`, `_publications/`, `_talks/`, `_teaching/`: public content.
- `_data/albums.yml`: album titles, image paths, dimensions, and thumbnails.
- `assets/js/gallery.js`: gallery behavior.

Keep original photographs outside the public asset folders. `local/` is ignored by Git and excluded from Jekyll; the cleanup backup is stored there. Export sanitized, resized web copies and thumbnails with `python3 scripts/prepare_photos.py` before publishing. The exporter needs ImageMagick, ExifTool, FFmpeg, and PyYAML. It preserves animation and applies photo orientation before removing metadata.

## JavaScript

```sh
npm ci
npm run build:js
```

Commit both dependency lockfiles when updating dependencies. `main.min.js` includes jQuery and the theme plugins; do not load another copy of jQuery.

## Build and deployment

```sh
JEKYLL_ENV=production bundle exec jekyll build
python3 scripts/check_site.py _site
```

The Pages workflow builds and deploys pushes to `master`. Local edits are not published until pushed. Development helpers, notebooks, backups, and demo files are excluded from the built site.

## Docker

```sh
docker compose up --build
```

The container uses UID 1000. If bind-mount ownership differs on your system, adjust the container user to match your account; do not make the repository world-writable.

## Credits

Based on [AcademicPages](https://github.com/academicpages/academicpages.github.io) and [Minimal Mistakes](https://github.com/mmistakes/minimal-mistakes). Bundled libraries retain their license notices.
