:date: 26.323-184000
:author: phi ARCHITECT
:type: log
:categories: architecture, constructions
:tags: etc, triangle-centers, shards, live-explorer, families, exact-algebra

=============================================================================
Scaling ETC to All 73,310 Centers in Exact Symbolic Algebra & Unified Viewer
=============================================================================

Scaled ``geometor.etc`` from 4,000 static Sphinx center pages to the complete **73,310-center** *Encyclopedia of Triangle Centers* (``X_1``–``X_73310``, Parts 1–37) across **7 canonical reference triangles**, unified every center and all **987 family groups** into one interactive client-side Book Codex explorer, and shrunk clean documentation build times by over 8×.

Architectural Breakthrough
--------------------------

Generating static multi-track RST + SVG directories for tens of thousands of centers hits both Sphinx compilation ceilings and GitHub Pages' 1 GB deployment cap (4,000 static centers already reached ``1.2 GB`` and 6+ minute builds). Replacing static per-center folders with compact **100-center exact symbolic JSON shards** rendered live on top of ``ETCViewer.Controller`` unlocked the entire ETC corpus at once:

- **Exact Algebraic Number Field Evaluator** (:mod:`geometor.etc.field_eval`): Evaluates barycentric, trilinear, and Cartesian coordinates directly inside exact rings (``QElem``, ``QuadElem``, ``BiquadElem``) over all 7 canonical triangles (Heronian ``(15, 13, 14)``, Right ``(5, 3, 4)``, Kepler ``(φ, 1, √φ)``, Kimberling ``(6, 9, 13)``, Golden ``(φ, φ, 1)``, Gnomon ``(1, 1, φ)``, Equilateral ``(2, 2, 2)``) with automatic 50-digit ``mpmath`` fallback for transcendental or >308-digit expressions.
- **Complete Contiguous Corpus (Zero Gaps)**: Fixed 4 upstream Evansville HTML heading typos (``X_57621``, ``X_60349``, ``X_68618``, ``X_71412``) and packed all **73,310 centers** into **734** partner-deduplicated JSON shards plus ``manifest.json``, ``core-centers.json``, ``search-index.json``, and ``families.json`` (**738 files**, ``332 MB`` uncompressed, ``77 MB`` gzipped release archive).
- **Unified Live Explorer & 987 Family Constellations**:
  - **Tier 0–4 Construction Engine**: Textbook compass-and-straightedge constructions for ``X_1``–``X_19`` (incircle, nine-point circle, excircles, Torricelli/Fermat circles, Apollonius circles, Napoleon & Clawson triangles) plus universal derived-triangle, defining-line, functional-relation, and cevian concurrence constructions for ``X_20``–``X_73310``.
  - **Visual Grammar**: Sparse round-dot construction/central lines snapping solid in their own color on hover, zoom-invariant halo rings around highlighted points, subtle construction evidence underneath the Coordinates decomposition, docked stage footer, and true edge-to-edge **Fullscreen App Mode** (``F``) displaying live center ID, title, and 5-track tabs.
  - **Family Groups**: All **925 ETC preamble families** and **62 curated collections** browseable via the searchable ``Families`` drawer, clickable header pills, and live 7-triangle **Family Constellations** (``#family/<id>``).
- **Content/Code Separation**: Moved all 19 exact SymPy ``geometor.model`` construction scripts cleanly into ``src/geometor/etc/models/x_00001.py``–``x_00019.py`` and retired all 4,000 redundant static ``x-00001``–``x-04000`` folders.

Verification Metrics
--------------------

- **Exact Algebraic Resolution**: ``96.9%`` exact on Heronian (``71,004 / 73,310``) and Kimberling (``71,003``); ``97.3%`` on Right & Kepler (``71,338``); ``96.1%`` on Golden & Gnomon (``70,429`` / ``70,436``); ``95.5%`` on Equilateral (``69,986``).
- **Zero-Determinant Collinearity Audit**: ``98.37%`` exact projective incidence pass rate on Kimberling (``66,943 / 68,049``) and ``98.28%`` on Heronian (``66,875 / 68,047``).
- **Build & Footprint**: Clean ``publish build`` completes in ``46.6 s`` with ``0`` local warnings, ``0`` broken local links/assets across all built HTML pages, and a ``409 MB`` total ``docs/`` footprint.
- **Test Suite**: ``70 passed`` across ``tests/test_symbolic_etc.py``, ``tests/test_field_eval.py``, and ``tests/test_shards.py``, plus ``154 / 154`` client-side construction checks across ``X_1``–``X_22`` × 7 triangles.
