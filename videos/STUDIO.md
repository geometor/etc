# GEOMETOR Encyclopedia of Triangle Centers (ETC) — Video Studio Context (`STUDIO.md`)

This document defines the project-specific conventions, `.scr` script syntax, SVG visual pipeline, and acoustic vocabulary for producing dual-format (`16:9` 2560x1440 QHD + `9:16` 1080x1920 Shorts) videos in **`geometor/etc`**.

---

## 1. Directory & Package Layout

Every center or topic video package lives in `videos/x-<nnnnn>/` (e.g., `videos/x-00001/`) or `videos/topics/<slug>/`:

### Tier 1 — Git-Tracked Source & Manifests
* `script.scr` — Single source of truth with top-level metadata (`center:`, `title:`, `folio:`, `enunciation:`), modular `=== <section> ===` boundaries, `[screen: ...]` directives, `say:` narration lines, and `[sfx:...]` cues. Compiled directly in memory (`scenes.json` is not needed on disk).
* `svgs/` — The 5 vector diagrams (`01_primary.svg` .. `05_four_triangles.svg`).
* `youtube.json` — Canonical YouTube broadcast state (`long_id`, `short_id`, `playlist_id`, `published_at`).

### Tier 2 — Local Git-Ignored Master Media (Archived via `studio archive push` / `pull`)
All rendered binary masters stay directly in `videos/<pkg>/` as real local files (no symlinks):
* `<prefix>_1080p.mp4` — `16:9` widescreen master rendered at native **`2560x1440` QHD** (`30 fps` CFR, H.264 High@L5.1 + AAC, triggers YouTube VP9).
* `<prefix>_short.mp4` — `9:16` vertical Short master rendered at native **`1080x1920`** (`30 fps` CFR, H.264 High@L4.1 + AAC).
* `<prefix>_thumb.png` / `<prefix>_short_thumb.png` (and `< 2 MB` `.jpg` versions) — Custom thumbnails.
* `<prefix>.wav` / `<prefix>.json` — Full master narration audio (`24000 Hz` PCM WAV) and subsegment timing manifest.
* `.tts_cache/` — Per-line cached PCM stems keyed by SHA-256.

---

## 2. Rendering Mode: Slide Sequence (`slides`)

`etc` uses **Studio Mode 1 (`slides` — Native Vector Slide Sequencing)**:
* **Capture**: `1920x1080` CSS layout rasterized natively at **`2560x1440`** via Chromium `--force-device-scale-factor=1.3333333333` (`4/3`), and `1080x1920` for `9:16` Shorts.
* **Encode**: Clean FFmpeg `-f concat` demuxer with exact per-slide audio durations from `<prefix>.json`:
  `ffmpeg -y -f concat -safe 0 -i concat.txt -i <prefix>.wav -vf fps=30 -shortest <prefix>_1080p.mp4`

---

## 3. Five-Section Modular Structure (`script.scr`)

Every triangle center `script.scr` is organized into five modular `=== <section> ===` blocks corresponding to the 5 analytical SVGs:

1. **`=== primary ===`** (`01_primary.svg`) — Concurrency (`CONSTRUCT`) and inscribed/circumscribed feature (`GOAL`), with `[sfx:concur]` and `[sfx:circle]`.
2. **`=== coordinates ===`** (`02_coordinates.svg`) — Trilinear ($\alpha : \beta : \gamma$) and barycentric ($u : v : w$) coordinates (`ASSERT`), with `[sfx:ratio]`.
3. **`=== central_lines ===`** (`03_central_lines.svg`) — Incident central lines (`INTERSECT`), with `[sfx:line]`.
4. **`=== relations ===`** (`04_relations.svg`) — Isogonal, isotomic, complement, and anticomplement conjugates (`PROVE`), with `[sfx:conjugate]`.
5. **`=== invariance ===`** (`05_four_triangles.svg`) — Invariance across Acute, Right, Kepler, and Kimberling reference triangles (`∴`), with `[sfx:invariant]`.

---

## 4. ETC Acoustic Vocabulary (`[sfx:...]`)

| Cue | Geometric Event | Acoustic Character |
| :--- | :--- | :--- |
| `[sfx:line]` | Drawing cevians, bisectors, altitudes, or central axes | Clean harmonic string draw |
| `[sfx:concur]` | Three cevians meeting at a triangle center $X_n$ | Crystalline three-voice convergence |
| `[sfx:circle]` | Revealing the incircle, circumcircle, nine-point, or pedal circle | Warm resonant arc sweep |
| `[sfx:ratio]` | Revealing trilinear or barycentric coordinate ratios | Balanced harmonic interval chime |
| `[sfx:conjugate]` | Mapping $X_n$ to its isogonal or isotomic conjugate | Mirrored inversion chime |
| `[sfx:invariant]` | Highlighting a harmonic range or collinearity invariant | Deep resonant fifth chord |

---

## 5. Build, Archive & Broadcast Commands

* **Build Center Video**:
  ```bash
  uv run --no-sync python scripts/build_center_video.py 1 --tts
  ```
* **Verify Package Integrity**:
  ```bash
  studio verify videos/x-00001
  ```
* **Push / Pull Git-Ignored Master Media with Google Drive (`gdrive:PHOTON-MEDIA`)**:
  ```bash
  studio archive sync videos/ geometor/etc/videos --direction push
  studio archive sync videos/ geometor/etc/videos --direction pull
  ```
* **Upload / Sync to YouTube (`@geometor`)**:
  ```bash
  studio broadcast upload --collection c-00001-00019 --centers 1
  ```
