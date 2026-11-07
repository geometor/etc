# GEOMETOR Encyclopedia of Triangle Centers (ETC) — Video Studio Context (`STUDIO.md`)

This document defines the project-specific conventions, script syntax, SVG visual pipeline, and acoustic vocabulary for producing dual-format (`16:9` 1440p QHD + `9:16` 1080x1920 Shorts) videos in **`geometor/etc`**.

---

## 1. Directory & Package Layout

Every center or topic video package lives in `videos/x-<nnnnn>/` (e.g., `videos/x-00001/`) or `videos/topics/<slug>/`:

### Tier 1 — Git-Tracked Source & Manifests
* `script.txt` — Canonical source script with `=== <section> ===` boundaries, `[screen: ...]` directives, `say:` narration lines, and `[sfx:...]` cues.
* `scenes.json` — Compiled slide timing, SVG asset paths, highlights, and spoken transcript.
* `youtube.json` — Canonical YouTube broadcast state (`long_id`, `short_id`, `playlist_id`, `published_at`).

### Tier 2 — Vault-Linked Master Media (`/home/phi/MEDIA/geometor/etc/videos/<pkg>/`)
* `<id>.mp4` — `16:9` widescreen master (`2560x1440` QHD, H.264 + AAC).
* `<id>_short.mp4` — `9:16` vertical Short master (`1080x1920`, H.264 + AAC).
* `<id>_thumb.png` / `<id>_short_thumb.png` — Custom thumbnails.
* `narration.wav` — Full concatenated master narration audio (`24000 Hz` WAV).
* `sections/<section_id>.wav` — Per-section cached audio stems for incremental re-synthesis.

---

## 2. Five-Section Modular Structure (`script.txt`)

Every triangle center `script.txt` is organized into five modular `=== <section> ===` blocks corresponding to the analytical layers of the center:

1. **`=== title ===`** (`01_hero.svg`)
   * Opens with the ETC signature bell (`[bell:D4,A4,F#5@2.0]`) and identifier (`X 1. The Incenter.`).
   * Introduces the center's fundamental geometric identity over the hero triangle configuration.
2. **`=== construction ===`** (`02_construction.svg`)
   * Explains the cevian, pedal, or circumcevian concurrency that defines the center.
   * Uses progressive `step` sub-slides (`02_construction_step1.svg`, `02_construction_step2.svg`, ...) so the reference triangle, cevians, and concurrency point appear in sync with `[sfx:line]`, `[sfx:concur]`, and `[sfx:circle]`.
3. **`=== coordinates ===`** (`03_coordinates.svg`)
   * Presents the normalized trilinear ($\alpha : \beta : \gamma$) and barycentric ($a : b : c$) coordinates and their geometric meaning (`[sfx:ratio]`).
4. **`=== lines_and_conjugates ===`** (`04_lines.svg`)
   * Explores the central lines passing through $X_n$ (Euler line, Nagel line, Soddy line, $X_1 X_2$ axis) and its isogonal, isotomic, and complement conjugates (`[sfx:conjugate]`).
5. **`=== properties ===`** (`05_properties.svg`)
   * Synthesizes the deeper algebraic, harmonic, and circle-center invariants (`[sfx:invariant]`) and closes on the harmonic bell triad.

---

## 3. Screen Block Directives (`[screen: ...]`)

```text
[screen: 02_construction.svg | THE THREE ANGLE BISECTORS]
  stage: bisectors
  highlight: line_AI, line_BI, line_CI, pt_X1
  badge: Concurrency
say: [sfx:line] Bisect the interior angles at vertices A, B, and C. [pause:0.35]
say: [sfx:concur] Those three bisectors concur at a single point: X 1, the incenter. [pause:0.4]
```

* Header syntax: `[screen: <svg_filename> | <SUBTITLE_BANNER>]`
* `stage:` — Progressive layer group within the SVG (`reference`, `bisectors`, `feet`, `incircle`, `full`).
* `highlight:` — SVG element IDs emphasized on this sub-slide.
* `badge:` — Conceptual tag pill (`Trilinears`, `Barycentrics`, `Nagel Line`, `Isogonal Conjugate`, etc.).

---

## 4. ETC Acoustic Vocabulary (`[sfx:...]`)

| Cue | Geometric Event | Acoustic Character |
| :--- | :--- | :--- |
| `[bell:D4,A4,F#5@2.0]` | Center Entry Signature | Warm D-major harmonic bell triad |
| `[sfx:line]` | Drawing cevians, bisectors, altitudes, or central axes | Clean harmonic string draw |
| `[sfx:concur]` | Three cevians meeting at a triangle center $X_n$ | Crystalline three-voice convergence |
| `[sfx:circle]` | Revealing the incircle, circumcircle, nine-point, or pedal circle | Warm resonant arc sweep |
| `[sfx:ratio]` | Revealing trilinear or barycentric coordinate ratios | Balanced harmonic interval chime |
| `[sfx:conjugate]` | Mapping $X_n$ to its isogonal or isotomic conjugate | Mirrored inversion chime |
| `[sfx:invariant]` | Highlighting a harmonic range or collinearity invariant | Deep resonant fifth chord |
| `[pause:0.4]` | Intentional breathing pause between analytical clauses | Exact silence (`0.4s`) |

---

## 5. Build & Broadcast Commands

* **Compile & Build Center Video from `script.txt`**:
  ```bash
  uv run --no-sync python scripts/build_center_video.py --center 1 --from-script
  ```
* **Verify Package Integrity**:
  ```bash
  studio verify --project etc
  ```
* **Link Master Binaries to `/home/phi/MEDIA` Vault**:
  ```bash
  studio archive link --project etc --execute
  ```
* **Upload / Sync to YouTube (`@geometor`)**:
  ```bash
  studio broadcast upload --project etc --center X_1
  ```
