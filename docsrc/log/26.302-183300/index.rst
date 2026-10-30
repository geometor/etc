:date: 26.302-183300
:author: phi ARCHITECT
:type: log
:categories: parser, constructions
:tags: etc, triangle-centers, svg, apparatus

========================================================================
ETC Semantic Parser, Apparatus Registries & Multi-Triangle Codex Builder
========================================================================

Completed the ingestion, semantic parsing, apparatus cross-referencing, and composable geometric construction pipeline for Clark Kimberling's *Encyclopedia of Triangle Centers*.

Highlights
----------

- **Full-Corpus Ingestion & Semantic Parsing**: Split and parsed ``X(1)`` through ``X(53144)`` alongside group preambles and the ETC Glossary, extracting canonical names, trilinear/barycentric/tripolar coordinates, construction notes, and functional relations.
- **Interactive Apparatus Registries**: Built ``glossary.json``, ``persons.json``, and ``citations.json`` to power ``:term:``, ``:person:``, ``:cite:``, and ``:ref:`` cross-references across all center pages.
- **Composable Constructions & Four-Triangle SVGs**: Implemented ``geometor.etc.ops`` and ``construct.py`` to generate standalone ``model.py`` scripts, ``geometor.model`` JSON snapshots, and two-layer interactive SVGs across scalene, right, Kepler, and Kimberling reference triangles.
