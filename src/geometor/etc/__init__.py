"""
Tools for processing and modeling the Encyclopedia of Triangle Centers (ETC).

Key Components:
---------------
- **Ingest**: Tools (:func:`ingest_folder`) to split and organize the raw HTML source.
- **Parser**: Tools (:func:`parse_center`) to extract center data from HTML.
- **Glossary**: Tools (:func:`extract_glossary_terms`) to handle glossary terms, persons, and citations.
- **Ops**: Composable Euclidean construction primitives and triangle operators (:mod:`geometor.etc.ops`).
- **Construct**: Coordinate/incidence resolver, `Model` builder, and per-center `model.py` generator (:mod:`geometor.etc.construct`).
- **Render**: Explorer-styled SVG renderer (:mod:`geometor.etc.render`).
- **Transform**: Tools (:func:`generate_rst_files`) to generate per-center ReStructuredText folders and graphics.

Usage:
------
Use the `main` function in `__main__.py` or the individual modules to process ETC data.
"""
from __future__ import annotations

from .ingest import ingest_folder
from .parser import parse_center
from .transform import generate_rst_files
from .glossary import extract_glossary_terms, generate_glossary_rst

__all__ = [
    "ingest_folder",
    "parse_center",
    "generate_rst_files",
    "extract_glossary_terms",
    "generate_glossary_rst",
]
__version__ = "0.1.1"
