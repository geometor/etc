geometor-etc
============

An index and toolkit for the Encyclopedia of Triangle Centers.

Mission
-------

Our goal is to modernize the ETC by:

*   **Structuring Data**: Parsing unstructured HTML into rigorous Python objects and data structures.
*   **Semantic Linking**: Establishing explicit, machine-verifiable links between centers (e.g., ``X(1)`` to ``X(2)``) and glossary terms.
*   **Enhanced Documentation**: Generating high-quality ReStructuredText (RST) documentation compatible with Sphinx, featuring MathJax for coordinates and equations.
*   **Integration**: Preparing the data for integration with ``geometor-explorer`` and other tools in the GEOMETOR ecosystem.

Pipeline
--------

The project employs a multi-stage pipeline to process the ETC:

1.  **Ingestion**: Splitting the massive source HTML files into manageable, individual center files.
2.  **Parsing**: Extracting structured data (trilinears, barycentrics, notes) from each center's HTML.
3.  **Glossary Extraction**: Automatically identifying and extracting terms from the ETC glossary.
4.  **Transformation**: Generating RST files with:
    *   Canonical cross-references (e.g., ``:ref:`X(1) <X(1)>```).
    *   Automatic glossary term linking (e.g., ``:term:`isogonal conjugate```).
    *   Metadata for sorting and categorization.

Usage
-----

To run the pipeline:

.. code-block:: bash

   python3 -m geometor.etc --limit 100

Or with explicit directory paths:

.. code-block:: bash

   python3 -m geometor.etc --input resources/source --split-dir resources/split --output docsrc/centers

Options:

*   ``--limit N``: Process only the first N centers (useful for testing).
*   ``--skip-ingest``: Skip the HTML splitting step if already done.

Output
------

The pipeline generates:

*   Per-center folders (e.g., ``docsrc/centers/x-00001/``) containing:
    *   ``index.rst``: Semantic RST documentation with ``Coordinates``, ``Linear Combinations``, ``Notes``, ``Incidence``, ``Relations``, ``Construction``, and embedded SVG figures.
    *   ``model.py``: Standalone, executable ``geometor.model`` construction script built from ``geometor.etc.ops``.
    *   ``x-NNNNN.svg`` (and ``x-NNNNN-kimberling.svg`` for ``X(1)``–``X(20)``): Explorer-styled SVG diagrams.
    *   ``x-NNNNN.json``: Serialized ``geometor.model.Model`` JSON for ``geometor-explorer``.
*   ``docsrc/glossary.rst``, ``docsrc/persons.rst``, and ``docsrc/bibliography.rst`` alongside ``resources/glossary.json``, ``resources/persons.json``, and ``resources/citations.json``.
*   ``docsrc/centers/index.rst`` using the ``collection`` directive to organize the centers.

Dependencies
------------

*   beautifulsoup4
*   docutils
*   sphinx
*   geometor-model
*   photon-platform-publish
