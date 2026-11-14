:navigation: header
:order: 20
:nav_title: Usage

==================
Using This Edition
==================

.. rubric:: Reader's Guide & Computational Pipeline for the Encyclopedia of Triangle Centers

``geometor.etc`` structures and computes the *Encyclopedia of Triangle Centers* (ETC) as an exact symbolic algebraic registry and interactive Book Codex. This guide explains how to navigate the digital edition and details command-line compilation and Python scripting via ``CenterSymbolicRegistry``.

Reader's Guide
==============

1. Synchronized Reading Tracks
------------------------------

Every modeled triangle center (:ref:`X_1 <X_1>` through :ref:`X_4000 <X_4000>`) provides two synchronized companion tracks accessible from the codex header:

* **Synthesis Track (`index.rst`)**: Clean, formal mathematical specification including the classical center name, ``.. signature:: center`` block detailing homogeneous trilinear (:math:`\alpha : \beta : \gamma`) and barycentric (:math:`u : v : w`) coordinates, collapsible incidence and collinearity tables, and interactive multi-triangle SVG diagrams.
* **Code Track (`code.rst`)**: Standalone, reproducible Python script (``model.py``) leveraging ``geometor.model`` and ``geometor.etc.ops`` primitives to construct the center and verify all collinearities algebraically.

2. Interactive Multi-Triangle SVG Visualizations
------------------------------------------------

Each center features interactive SVG plates rendered across four distinct reference triangles:

* **Acute / Scalene**: Standard reference triangle highlighting general position properties.
* **Right**: Demonstrates coordinate behavior and degenerate alignments in Pythagorean triangles.
* **Kepler**: Golden-ratio triangle exploring extreme proportion harmonics.
* **Kimberling**: Specialized reference geometry designed for optimal visual separation of close centers.

Hovering over points, central lines (Euler line, Brocard axis, Nagel line), and central circles highlights the geometric elements in real time.

3. Archival Cross-References & ETC Loci
---------------------------------------

Every center entry provides direct reciprocal hyperlinks to Clark Kimberling's authoritative web edition at the University of Evansville, alongside references to the 925 group preambles cataloged in the :doc:`Guide to Preambles <../preambles>`.

4. Full-Text Search with In-Page Highlighting
---------------------------------------------

The global search indexes all 4,000+ center names, alternative designations, coordinates, and historical notes. Clicking a search result loads the destination page with the search term highlighted in yellow (``?highlight=``), allowing instant location of specific center families and collinearity statements.

5. Taxonomy, Document Types & Collection Views
----------------------------------------------

The :doc:`Triangle Centers <../centers/index>` overview organizes centers into 62 thematic collections:

* **View Toggles**: Choose between **Cards** (visual grid with thumbnails and coordinates), **Banners** (wide horizontal cards with tags), and **List** (compact index table) modes.
* **Taxonomy Facets**: Filter centers by mathematical type, contributor, and algebraic degree in the sidebar.

6. People, Bibliography & Glossary Tooltips
-------------------------------------------

* **Person Badges (``:person:``)**: Hovering over names like :person:`Clark Kimberling <clark-kimberling>`, :person:`Leonhard Euler <leonhard-euler>`, or :person:`Henri Brocard <henri-brocard>` opens biographical cards.
* **Glossary Terms (``:term:``)**: Immediate contextual definitions for central triangles, conjugacies, and projective collineations.
* **Theme Switcher**: Instant toggle between Light and Dark reading modes.

Developer & CLI Guide
=====================

Command-Line Interface
----------------------

``geometor.etc`` executes a 4-stage pipeline—**Ingest**, **Parse**, **Construct**, and **Render**—to build the Book Codex:

.. code-block:: bash

   # Build the first 1,000 centers (skipping raw HTML download if already cached)
   python3 -m geometor.etc --skip-ingest --limit 1000

   # Build specific triangle centers by ID
   python3 -m geometor.etc --skip-ingest --centers 1 2 3 4 5 6 7 8 9 10 11 13

   # Compile the Sphinx HTML documentation site
   publish build

Python API & CenterSymbolicRegistry
-----------------------------------

You can query center coordinates, collinearities, and symbolic expressions programmatically:

.. code-block:: python

   from geometor.etc.symbolic_cache import CenterSymbolicRegistry

   registry = CenterSymbolicRegistry()

   # Query center details
   x1 = registry.get(1)
   print("X(1) Incenter trilinears:", x1.trilinears)
   print("X(1) Barycentrics:", x1.barycentrics)

   # Query collinearities on the Euler line
   euler_centers = registry.get_line_centers("Euler")
   print("Centers on Euler line:", euler_centers[:10])

Composable Geometric Operations (``geometor.etc.ops``)
------------------------------------------------------

Standalone constructions in ``model.py`` utilize primitives from ``geometor.etc.ops``:

.. code-block:: python

   from geometor.etc.ops import (
       orthocenter,
       circumcenter,
       centroid,
       nine_point_center,
       isogonal_conjugate,
       isotomic_conjugate,
   )

   # Construct Euler line centers
   H = orthocenter(A, B, C)
   O = circumcenter(A, B, C)
   G = centroid(A, B, C)
   N = nine_point_center(A, B, C)
