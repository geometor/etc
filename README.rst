GEOMETOR • etc
==============

.. image:: https://img.shields.io/github/license/geometor/etc.svg
   :target: https://github.com/geometor/etc/blob/main/LICENSE

**Digital reconstruction, semantic index, and composable geometric modeling of Clark Kimberling's *Encyclopedia of Triangle Centers* (`X(1)`–`X(53144)`).**

Overview
--------

``geometor.etc`` transforms the archival HTML volumes of Clark Kimberling's *Encyclopedia of Triangle Centers* (ETC) and its supporting *Glossary* into structured registries, executable `geometor/model <https://github.com/geometor/model>`_ constructions, interactive multi-triangle SVG diagrams, and a 2-track **Book Codex** edition powered by `photon-platform/publish <https://github.com/photon-platform/publish>`_.

Process & Pipeline
------------------

1. **Archival Ingestion (`ingest.py`)**:
   - Splits the raw HTML source volumes (`ETC.html`, `ETCPart2.html`–`ETCPart27.html`) into introductory sections, inter-center group preambles, and 53,144 individual center records in `resources/split/`.

2. **Semantic Parsing (`parser.py`)**:
   - Extracts canonical identifiers (`X(n)`), primary names, aliases, trilinear/barycentric/tripolar coordinates, vector/barycentric linear combinations, construction notes, incidence loci (central lines, circles, conics, cubics), and functional center relations (`X(n) = f(X(i), X(j))`).

3. **Scholarly Apparatus & Cross-Referencing (`glossary.py`)**:
   - Builds `resources/glossary.json`, `resources/persons.json`, and `resources/citations.json` and generates `docsrc/glossary.rst`, `docsrc/persons.rst`, and `docsrc/bibliography.rst` to power interactive `:term:`, `:person:`, `:cite:`, and `:ref:` roles across all centers.

4. **Composable Geometric Modeling & Multi-Triangle SVGs (`ops.py`, `construct.py`, `render.py`)**:
   - Constructs each center symbolically via composable geometric operations in `geometor.etc.ops`, emitting a standalone `model.py` script and serialized `x-NNNNN.json` model for `geometor/explorer <https://github.com/geometor/explorer>`_.
   - Renders two-layer interactive SVGs (primary defining construction + toggleable incident central lines) across four canonical reference triangles:
     - **Acute (`x-NNNNN.svg`)**: Sides $(a, b, c) = (5, 6, 7)$
     - **Right (`x-NNNNN-right.svg`)**: Egyptian right triangle $(3, 4, 5)$
     - **Kepler (`x-NNNNN-kepler.svg`)**: Golden right triangle $(1, \sqrt{\varphi}, \varphi)$
     - **Kimberling (`x-NNNNN-kimberling.svg`)**: Obtuse reference triangle $(6, 9, 13)$

5. **2-Track Book Codex Generation (`transform.py`)**:
   - Generates per-center documentation in `docsrc/centers/x-NNNNN/` using `:layout: book`:
     - **Overview Track (`index.rst`)**: Formal `.. enunciation::`, interactive reference-triangle SVG selector, `.. signature:: center` coordinate summary (Trilinears, Barycentrics, Tripolars), and `.. collapse::` sections for Linear Combinations, Notes, Incidence Loci, Functional Relations, and Construction.
     - **Code Track (`code.rst`)**: Standalone `geometor.model` Python construction script (`model.py`).

Coordination with ``publish``
-----------------------------

- Uses `:layout: book` in `photon-platform/publish <https://github.com/photon-platform/publish>`_ for synchronized **Overview** and **Code** tracks with track-preserving `Prev` / `Next` navigation across centers.
- Integrates `:term:`, `:person:`, and `:cite:` hover cards and `intersphinx` links to Euclidean propositions in `geometor/euclid <https://geometor.github.io/euclid>`_ and `geometor/elements <https://geometor.github.io/elements>`_.

Usage
-----

.. code-block:: bash

   # Run the ETC pipeline for the first 1,000 centers (skipping raw HTML split if cached)
   python3 -m geometor.etc --skip-ingest --limit 1000

   # Build and serve the Book Codex documentation locally
   publish test

Resources & Related Projects
----------------------------

- **Live Edition**: https://geometor.github.io/etc
- **Source Code**: https://github.com/geometor/etc
- `GEOMETOR • model <https://github.com/geometor/model>`_: Symbolic geometric construction engine.
- `GEOMETOR • explorer <https://github.com/geometor/explorer>`_: Interactive web workbench for exploring `x-NNNNN.json` models.
- `PHOTON • publish <https://github.com/photon-platform/publish>`_: Sphinx Book Codex publishing engine and theme.
