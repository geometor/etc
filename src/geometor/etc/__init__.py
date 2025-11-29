"""
Tools for processing the Encyclopedia of Triangle Centers (ETC).

Key Components:
---------------
- **Ingest**: Tools (:func:`ingest_folder`) to split and organize the raw HTML source.
- **Parser**: Tools (:func:`parse_center`) to extract center data from HTML.
- **Transform**: Tools (:func:`generate_rst_files`) to generate ReStructuredText documentation.
- **Glossary**: Tools (:func:`extract_glossary_terms`) to handle glossary terms.

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
__author__ = "PHOTON platform"
__maintainer__ = "PHOTON platform"
__email__ = "github@phiarchitect.com"
__version__ = "0.0.2"
__licence__ = "MIT"
