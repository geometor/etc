GEOMETOR • etc
==============

**Visit the Online Archive:** https://geometor.github.io/etc/

.. image:: docsrc/_static/coordinates/barycentric_picture.svg
   :alt: GEOMETOR • etc featured geometric construction
   :target: https://geometor.github.io/etc/
   :align: center

**Encyclopedia of Triangle Centers • Clark Kimberling's X(1)–X(53144) • semantic digital archive**

Mission
-------

``geometor/etc`` is part of the interconnected `GEOMETOR <https://geometor.com>`_ semantic digital archive. It provides a computable, symbolic digital edition of Clark Kimberling's *Encyclopedia of Triangle Centers* (ETC), establishing exact algebraic definitions, trilinear and barycentric coordinates, and interactive multi-triangle vector models for centers :math:`X(1)` through :math:`X(53144)`. Liberating the archive from tabular HTML listings into addressable semantic units, the repository bridges classical triangle loci with automated theorem proving and symbolic geometry across the GEOMETOR corpus.

Catalogs in This Archive
------------------------

- `Encyclopedia of Triangle Centers <https://geometor.github.io/etc/centers/>`_ — Clark Kimberling's ETC in exact symbolic algebra, multi-triangle vector diagrams, and 2-track Book Codex representations.
- `Collection 1 Topics: Conjugacies, Lines, Circles & Triangles <https://geometor.github.io/etc/topics/>`_ — Exact symbolic investigations of central lines, Euler lines, circumcircles, and triangle connections.

Repository Contents
-------------------

- ``docsrc/`` — RST catalog tracks, guides, and preambles compiled by `PHOTON publish <https://github.com/photon-platform/publish>`_.
- ``resources/`` — Ingested center records, coordinate registries, persons registers, and citations manifests.
- ``src/geometor/etc/`` — Archival parsing, symbolic coordinate modeling, SVG rendering, and Book Codex generation engine.

Local Build & Verification
--------------------------

.. code-block:: bash

   publish build
   uv run --no-sync pytest

Part of the GEOMETOR Knowledge Archive
--------------------------------------

Explore all **74 Book Codices** and **11 Mathematical Catalogs** at https://geometor.com/books/.
