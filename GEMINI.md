# GEOMETOR ETC

A digital reconstruction and semantic index of Clark Kimberling's *Encyclopedia of Triangle Centers* (ETC).

## Mission

To parse, structure, cross-reference, and model the *Encyclopedia of Triangle Centers* (`X(1)` through `X(53144)`), establishing a computable dependency and incidence graph ready for symbolic and graphical exploration in `geometor.model` and `geometor.explorer`.

## Overview

`geometor.etc` transforms the archival HTML volumes of Clark Kimberling's *Encyclopedia of Triangle Centers* and its supporting *Glossary* into structured data registries and rich ReStructuredText (RST) documentation powered by `photon-platform/publish`.

It is responsible for:

- **Ingestion**: Splitting raw HTML source volumes (`ETC.html`, `ETCPart2.html`–`ETCPart27.html`) into introductory sections, inter-center group preambles, and individual center records (`resources/split/`).
- **Semantic Parsing**: Extracting canonical identifiers, primary names, aliases, trilinear/barycentric/tripolar coordinates, vector/barycentric linear combinations, construction notes, incidence loci (lines, circles, conics, cubics), and functional center relations (`X(n) = f(X(i), X(j))`).
- **Apparatus & Cross-Referencing**: Building `resources/glossary.json`, `resources/persons.json`, and `resources/citations.json` to power interactive `:term:`, `:person:`, `:cite:`, and `:ref:` roles across all centers.
- **Composable Geometric Modeling**: Constructing each center via `src/geometor/etc/ops.py` and generating standalone per-center `model.py` scripts, `geometor.model` JSON files, and Explorer-styled SVGs.
- **RST Generation**: Generating structured Sphinx documentation per center (`docsrc/centers/x-NNNNN/index.rst`, `docsrc/glossary.rst`, `docsrc/persons.rst`, `docsrc/bibliography.rst`).

## Repository Layout

- `resources/source/`: Archival HTML source files (`ETC.html`, `ETCPart2.html`–`ETCPart27.html`, `GLOSSARY...html`).
- `resources/split/`: Intermediate split HTML files for centers, preambles, and intro sections (git-ignored).
- `resources/centers/`: Full archive of 53,144 generated per-center folders (git-ignored).
- `resources/`: Extracted apparatus registries (`glossary.json`, `persons.json`, `citations.json`).
- `src/geometor/etc/`: Core Python package (`ingest.py`, `parser.py`, `glossary.py`, `ops.py`, `construct.py`, `render.py`, `transform.py`, `__main__.py`).
- `docsrc/centers/x-NNNNN/`: Per-center folder containing `index.rst`, `model.py`, `x-NNNNN.json`, and interactive SVGs across 4 reference triangles (`x-NNNNN.svg`, `x-NNNNN-right.svg`, `x-NNNNN-kepler.svg`, `x-NNNNN-kimberling.svg`).

## CLI Usage

```bash
python3 -m geometor.etc --skip-ingest --limit 100
```
