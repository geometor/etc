changelog
=========

:project: geometor.etc

0.1.3
-----

- Adopted the Book Codex layout (`:layout: book`) across `docsrc/centers/` and the scholarly apparatus (`glossary.rst`, `persons.rst`, `bibliography.rst`).
- Added a 2-track companion switcher (`Overview` | `Code`) generating per-center `code.rst` pages alongside `index.rst`.
- Extracted primary geometric definitions into `.. enunciation::` banners (powering collection excerpts and `:ref:` tooltips) and consolidated primary coordinates into a compact `.. signature:: center` card.
- Organized secondary apparatus into collapsible `.. collapse::` sections (`Alternate Coordinates`, `Linear Combinations`, `Incident Central Lines`, and `Functional Relations`) with count badges.

0.1.2
-----

- Simplified initial center graphics into a focused primary construction layer showing only the specific defining geometric relationship (and the golden Euler line whenever $X(n)$ lies on the Euler line).
- Added a `Lines` toolbar toggle button to show/hide incident central lines `{i, j}` and their defining centers across all 4 reference triangle tabs.
- Escaped XML special characters (`<`, `>`, `&`) as JSON unicode sequences in embedded SVG metadata so collection page `<img>` thumbnails pass strict XML validation.
- Expanded coordinate/incidence resolution and generated documentation and interactive graphics for `X(1)` through `X(1000)`.

0.1.1
-----

- Added interactive Explorer-styled SVG controls (zoom, pan, reset, label/guide toggles) and native topmost element hover highlighting with named points, lines, circles, and triangles.
- Scaled point radii and label typography $1.5\times$ for legibility.
- Unified reference triangle graphics into a 4-tab graphics panel (`5, 6, 7`, `3, 4, 5`, `Kepler`, and `Kimberling`) on center pages while keeping static thumbnails on collection pages.
- Added projective limit fallback evaluation and coincident point handling for right triangles (`3, 4, 5` and `Kepler`).


0.1.0
-----

- Added semantic parser, glossary/person/citation registries, composable triangle construction operators (`ops.py`), and per-center folders with `model.py`, `x-NNNNN.json`, and `x-NNNNN.svg`.

0.0.2
-----

-   Refined docstrings and type hinting.
-   Fixed `from __future__ import annotations` placement.

0.0.1 
-----

:init: 2025.330
:merge:
:pub: 

  index for the encyclopedia of triangle centers

- initalize project

