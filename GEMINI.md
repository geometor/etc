# GEOMETOR ETC

A digital reconstruction and semantic index of Clark Kimberling's *Encyclopedia of Triangle Centers* (ETC).

## Mission

To parse, structure, cross-reference, and evaluate the complete *Encyclopedia of Triangle Centers* (`X_1` through `X_73310`, Parts 1–37) in exact algebraic number fields across 7 canonical reference triangles, establishing a computable dependency and incidence graph ready for symbolic and graphical exploration in `geometor.model`, `geometor.explorer`, and the unified client-side Live Center Explorer.

## Overview

`geometor.etc` transforms the archival HTML volumes of Clark Kimberling's *Encyclopedia of Triangle Centers* and its supporting *Glossary* into structured apparatus registries, exact algebraic 100-center JSON shards, and a unified Book Codex powered by `photon-platform/publish`.

It is responsible for:

- **Ingestion**: Splitting raw HTML source volumes (`ETC.html`, `ETCPart2.html`–`ETCPart37.html`) into introductory sections, 925 inter-center group preambles, and 73,310 contiguous center records (`resources/split/`).
- **Semantic Parsing**: Extracting canonical identifiers, primary names, aliases, trilinear/barycentric/tripolar coordinates, vector/barycentric linear combinations, construction notes, incidence loci, and functional center relations (`X_n = f(X_i, X_j)`) with `:math:` LaTeX normalization.
- **Exact Symbolic Field Evaluation & Sharding (`field_eval.py`, `shards.py`)**: Evaluating all 73,310 centers inside exact algebraic rings (`QElem`, `QuadElem`, `BiquadElem`, with 50-digit `mpmath` fallback) across all 7 canonical triangles (Heronian, Right, Kepler, Kimberling, Golden, Gnomon, Equilateral) into 734 partner-deduplicated JSON shards plus `manifest.json`, `core-centers.json`, `search-index.json`, and `families.json` (925 ETC families + 62 curated collections) in `.cache/etc_data/`.
- **Classical Symbolic Models (`src/geometor/etc/models/`, `ops.py`)**: Exact zero-float `geometor.model` compass-and-straightedge constructions for `X_1`–`X_19` (`models/x_00001.py`–`x_00019.py`) and canonical *Principles of Geometry* operators.
- **Unified Live Explorer & Book Codex (`docsrc/centers/explore.rst`, `etc-live-viewer.js`, `etc-viewer.js`)**: Serving all `X_1`–`X_73310` centers and all 987 interactive family constellations client-side with 5 synchronized tracks, Tier 0–4 geometric constructions, sparse-dot-to-solid line highlights, zoom-invariant point rings, docked stage footer, and Fullscreen App Mode (`F`).

## Repository Layout

- `resources/source/`: Archival HTML source volumes (`ETC.html`, `ETCPart2.html`–`ETCPart37.html`, `GLOSSARY...html`, `Guide_to_preambles_in_ETC.html`).
- `resources/split/`: Intermediate split HTML files for centers, preambles, and intro sections (git-ignored).
- `.cache/etc_data/`: Exact symbolic JSON shards (`shards/s-XXXXX-YYYYY.json`), indices (`manifest.json`, `core-centers.json`, `search-index.json`, `families.json`), and per-triangle gzip checkpoints (git-ignored; distributed via GitHub Release assets for CI).
- `src/geometor/etc/`: Core Python package (`ingest.py`, `parser.py`, `field_eval.py`, `shards.py`, `glossary.py`, `ops.py`, `models/x_00001.py`–`x_00019.py`, `construct.py`, `plates.py`, `render.py`, `svg_opt.py`, `transform.py`, `tracks.py`, `topics.py`, `triangles.py`, `symbolic_cache.py`).
- `docsrc/centers/`: Unified Live Explorer (`explore.rst`) and 62 thematic collection chapter pages (`c-00001-00019/`–`c-03961-04000/`) with constellation SVGs and live member tables.

## CLI Usage

```bash
uv run --no-sync python3 -m geometor.etc.shards --max-center 73310 --workers 4
uv run --no-sync python3 -m geometor.etc.shards --families-only
publish build
uv run --no-sync pytest
```

