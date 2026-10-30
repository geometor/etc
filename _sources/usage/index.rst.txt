:navigation: header
:order: 20

=====
usage
=====

``geometor.etc`` executes a 4-stage pipeline—**Ingest**, **Parse**, **Construct**, and **Render**—to build the *Encyclopedia of Triangle Centers* Book Codex.

CLI Usage
---------

.. code-block:: bash

   # Build the first 1,000 centers (skipping raw HTML splitting if already cached)
   python3 -m geometor.etc --skip-ingest --limit 1000

   # Build specific triangle centers by ID
   python3 -m geometor.etc --skip-ingest --centers 1 2 3 4 5 6 7 8 9 10 11 13

   # Compile the Sphinx HTML site
   publish build

Composable Geometric Operations (``geometor.etc.ops``)
------------------------------------------------------

Each modeled center directory (``docsrc/centers/x-NNNNN/``) includes a standalone ``model.py`` script built from ``geometor.etc.ops`` primitives (e.g., ``orthocenter``, ``incenter``, ``circumcenter``, ``centroid``, ``isogonal_conjugate``, ``isotomic_conjugate``, ``trilinear_pole``, ``perspector``) and renders interactive SVGs across four reference triangles (``scalene``, ``right``, ``kepler``, and ``kimberling``).
