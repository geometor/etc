changelog
=========

:project: geometor.etc

0.2.0
-----

- Added the 4-triangle exact symbolic reference engine (``triangles.py``) and persistent symbolic evaluation cache (``symbolic_cache.py``: ``CenterSymbolicRegistry``, ``SymbolicCenterRecord``) over ``5, 6, 7``, ``3, 4, 5``, ``Kepler``, and ``Kimberling`` triangles.
- Expanded ``ops.py`` with exact Euclidean construction primitives and ``CANONICAL_CENTER_CONCORDANCE`` operators built on ``geometor.model`` v0.6.0 targeted DAGs and Rational Trigonometry invariants.
- Established the 5-act ``X_1`` Book Codex center template, multi-panel Explorer-styled SVG diagrams (``01_primary`` through ``05_four_triangles``), exact symbolic HUD metadata, and synchronized ``videos/x-00001/script.scr`` studio choreography.
- Updated GitHub Actions deployment workflow to install ``geometor/model`` before ``geometor/etc`` with ``contents: write`` permissions.

0.1.8
-----

- Replaced generic local point/triangle symbols (`A'`, `B'`, `C'`, `X`, `Y`, `Z`, `X'`, `Y'`, `Z'`, `I_aI_bI_c`) in enunciations and notes with their canonical special point labels (`T_a, T_b, T_c`, `H_a, H_b, H_c`, `M_a, M_b, M_c`, `N_a, N_b, N_c`, `J_a, J_b, J_c`, `I_a, I_b, I_c`, `Tan_a, Tan_b, Tan_c`, `K_a, K_b, K_c`, `Sym_a, Sym_b, Sym_c`, `Eu_a, Eu_b, Eu_c`, `Ref_a, Ref_b, Ref_c`, `Cm_a, Cm_b, Cm_c`, `O_A, O_B, O_C`, `Nap_a, Nap_b, Nap_c`) whenever bound to a known special triangle or vertex triple.
- Removed redundant side-by-side `(denoted ...)` and `(:g:`A' <T_a>`)` alias annotations from `Constructed Elements` blocks across all 3,000 center pages.

0.1.7
-----

- Expanded coordinate, incidence, and functional relation resolution to `X_1` through `X_3000` (100% resolved across all 4 reference triangles: `5, 6, 7`, `3, 4, 5`, `Kepler`, and `Kimberling`).
- Added preamble transformation handlers (*Orion transforms*, *Eigentransforms*, *Gibert-Simson transforms*, *Rigby-Simson* and *Simson-Rigby* points, *Simson-Moses* points, *Tangential/Medial/Anticomplementary-Isogonal* conjugates, *Dual Center* `DC(X)` / `CD(X)` mappings, and $X_i$-isoconjugates), Steiner inellipse constant $K$, and multi-clause cyclic helper expansion (`h(a,b,c)`, `k(a,b,c)`).
- Added a continuous-limit perturbation pass for removable $0/0$ singularities at $C = 90^\circ$ on right and Kepler triangles.
- Added 14 new thematic collections (`c-02001-02054` through `c-02967-03000`, bringing the total to 52 thematic collections) with 4-triangle constellation graphics (`c-XXXXX-YYYYY.svg`).

0.1.6
-----

- Expanded coordinate and geometric construction resolution to `X_1` through `X_2000` (100% resolved across all 4 reference triangles: `5, 6, 7`, `3, 4, 5`, `Kepler`, and `Kimberling`).
- Added preamble transformation handlers (*Saragossa points*, *Collings transforms*, *Brisse transforms*, *Orthojoin points*, *TCC-perspectors*), `x:y:z = X_k` trilinear coordinate substitutions, and seeded roots (`X_134`, `X_180`, `X_1144`).
- Organized `X_1`–`X_2000` into 38 thematic collections (`docsrc/centers/c-XXXXX-YYYYY/`) aligned with Kimberling's section preambles and geometric families so `docs/centers/index.html` loads instantaneously (~54 KB instead of ~30 MB).
- Generated multi-center constellation graphics (`c-XXXXX-YYYYY.svg` across all 4 reference triangles) for each thematic collection using an editorial selection of 11–16 spatially separated landmark centers with interactive hover labels and click-to-navigate center dots.

0.1.5
-----

- Standardized triangle center identifiers and references from `X(n)` to subscripted `X_n` (`X_1`, `X_2`, …, rendered as `X<sub>n</sub>` in HTML and `<tspan>` subscripts in SVG).
- Added contextual `A'B'C'` classical triangle resolution in prose so `:g:` roles bind `A'`, `B'`, `C'` to their model IDs (`M_a`, `H_a`, `T_a`, `I_a`, etc.) when constructed on the canvas.
- Rendered underscore point labels (`M_a`, `H_a`, `I_a`, `X_n`) with `<tspan>` subscripts and font-relative `0.15em` strokes in Explorer-styled SVGs.
- Redesigned center page headings as two centered lines (`X_n` over bold non-italic subtitle rubric, with `position: absolute` headerlink alignment).

0.1.4
-----

- Added semantic math normalization and `:g:` geometric element roles across parsed center descriptions, notes, and glossary entries.

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

