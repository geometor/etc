"""Tools for processing and modeling the Encyclopedia of Triangle Centers (ETC).

Key Components
--------------

- **Triangles**: Exact canonical symbolic reference triangles (:mod:`geometor.etc.triangles`).
- **Symbolic Cache**: Exact symbolic center evaluator and disk cache (:mod:`geometor.etc.symbolic_cache`).
- **Ops**: Exact Euclidean construction primitives and canonical *Principles of Geometry* operators (:mod:`geometor.etc.ops`).
- **Ingest**: Tools (:func:`ingest_folder`) to split and organize the raw HTML source.
- **Parser**: Tools (:func:`parse_center`) to extract center data from HTML.
- **Glossary**: Tools (:func:`extract_glossary_terms`) to handle glossary terms, persons, and citations.
- **Construct**: Coordinate/incidence resolver, ``Model`` builder, and per-center ``model.py`` generator (:mod:`geometor.etc.construct`).
- **Render**: Explorer-styled SVG renderer with exact symbolic HUD metadata (:mod:`geometor.etc.render`).
- **Transform**: Tools (:func:`generate_rst_files`) to generate per-center ReStructuredText folders and graphics.
"""

from __future__ import annotations

from .glossary import extract_glossary_terms, generate_glossary_rst
from .ingest import ingest_folder
from .ops import (
    CANONICAL_CENTER_CONCORDANCE,
    CenterConcordance,
    bevan_point,
    centroid,
    circumcenter,
    circumcircle_inverse_of_incenter,
    clawson_point,
    construct_baseline_triangle,
    construct_reference_triangle,
    create_model,
    de_longchamps_point,
    fermat_point,
    feuerbach_point,
    first_isodynamic_point,
    first_napoleon_point,
    gergonne_point,
    get_center_concordance,
    harmonic_feuerbach_point,
    incenter,
    isotomic_conjugate_of_incenter,
    mittenpunkt,
    nagel_point,
    nine_point_center,
    orthocenter,
    second_isodynamic_point,
    second_isogonic_center,
    second_napoleon_point,
    spieker_center,
    symmedian_point,
)
from .parser import parse_center
from .symbolic_cache import CenterSymbolicRegistry, SymbolicCenterRecord
from .transform import generate_rst_files
from .triangles import (
    CANONICAL_TRIANGLES,
    SymbolicTriangle,
    get_canonical_triangle,
)

__all__ = [
    "CANONICAL_CENTER_CONCORDANCE",
    "CANONICAL_TRIANGLES",
    "CenterConcordance",
    "CenterSymbolicRegistry",
    "SymbolicCenterRecord",
    "SymbolicTriangle",
    "bevan_point",
    "centroid",
    "circumcenter",
    "circumcircle_inverse_of_incenter",
    "clawson_point",
    "construct_baseline_triangle",
    "construct_reference_triangle",
    "create_model",
    "de_longchamps_point",
    "extract_glossary_terms",
    "fermat_point",
    "feuerbach_point",
    "first_isodynamic_point",
    "first_napoleon_point",
    "generate_glossary_rst",
    "generate_rst_files",
    "gergonne_point",
    "get_canonical_triangle",
    "get_center_concordance",
    "harmonic_feuerbach_point",
    "incenter",
    "ingest_folder",
    "isotomic_conjugate_of_incenter",
    "mittenpunkt",
    "nagel_point",
    "nine_point_center",
    "orthocenter",
    "parse_center",
    "second_isodynamic_point",
    "second_isogonic_center",
    "second_napoleon_point",
    "spieker_center",
    "symmedian_point",
]
__version__ = "0.1.8"


