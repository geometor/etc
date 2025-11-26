geometor-etc
============

The **Encyclopedia of Triangle Centers (ETC)** is a monumental work by Clark Kimberling. This project, ``geometor-etc``, aims to transform the original HTML content of the ETC into a structured, machine-readable, and semantically interconnected dataset and documentation site.

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

   python3 -m geometor.etc --input /path/to/source --split-dir /path/to/split --output /path/to/docsrc/centers

Options:

*   ``--limit N``: Process only the first N centers (useful for testing).
*   ``--skip-ingest``: Skip the HTML splitting step if already done.

Output
------

The pipeline generates:

*   Individual RST files for each center (e.g., ``x-00001.rst``).
*   A ``glossary.rst`` file with extracted definitions.
*   An ``index.rst`` using the ``collection`` directive to organize the centers.

Dependencies
------------

*   beautifulsoup4
*   docutils
*   sphinx
*   photon-platform (for configuration)
