"""Exact symbolic GEOMETOR construction model for ``X_6 = SYMMEDIAN POINT``."""

from __future__ import annotations

from pathlib import Path

import sympy as sp
import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    centroid,
    circumcenter,
    clawson_point,
    construct_baseline_triangle,
    construct_reference_triangle,
    create_model,
    exact_center_point,
    incenter,
    mittenpunkt,
    promote_point_to_top,
    symmedian_point,
)
from geometor.etc.render import write_center_svg


def construct_x_00006(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct ``X_6 = SYMMEDIAN POINT`` and its classical incident central lines on ``ABC``.

    Constructed elements include:

    - Circumcircle, symmedial triangle ``< Sym_a Sym_b Sym_c >``, and symmedians
      ``[ A Sym_a ]``, ``[ B Sym_b ]``, ``[ C Sym_c ]`` concurring at ``X_6``.
    - Incident central lines: Incenter-Mittenpunkt ``{ 1, 9 }``, Brocard axis
      ``{ 3, 32 }``, Centroid-Isotomic ``{ 2, 69 }``, and ``{ 19, 65 }``.
    """
    X_6 = symmedian_point(
        model,
        A,
        B,
        C,
        ID="X_6",
        classes=["selected", "target"],
        draw_symmedians=True,
    )

    X_1 = incenter(model, A, B, C, ID="X_1", classes=["center", "incident"])
    X_9 = mittenpunkt(model, A, B, C, ID="X_9", classes=["center", "incident"])
    central_line(model, X_1, X_9, 1, 9, incident=True)

    X_3 = circumcenter(model, A, B, C, ID="X_3", classes=["center", "incident"])
    X_32 = exact_center_point(
        model, A, B, C, 32, ID="X_32", classes=["center", "incident"]
    )
    central_line(model, X_3, X_32, 3, 32, incident=True)

    X_2 = centroid(model, A, B, C, ID="X_2", classes=["center", "incident"])
    X_69 = exact_center_point(
        model, A, B, C, 69, ID="X_69", classes=["center", "incident"]
    )
    central_line(model, X_2, X_69, 2, 69, incident=True)

    X_19 = clawson_point(model, A, B, C, ID="X_19", classes=["center", "incident"])
    X_65 = exact_center_point(
        model, A, B, C, 65, ID="X_65", classes=["center", "incident"]
    )
    central_line(model, X_19, X_65, 19, 65, incident=True)

    return promote_point_to_top(model, X_6)


def build_model(
    preset: str | tuple[sp.Expr | int, sp.Expr | int, sp.Expr | int] = "heronian",
    show_guides: bool = False,
) -> Model:
    """Build an exact symbolic :class:`geometor.model.Model` for ``X_6 = SYMMEDIAN POINT``."""
    model = create_model("X_6 = SYMMEDIAN POINT")
    if isinstance(preset, str):
        A, B, C = construct_reference_triangle(model, preset, show_guides=show_guides)
    else:
        A, B, C = construct_baseline_triangle(model, *preset, show_guides=show_guides)
    construct_x_00006(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    plate_specs = [
        ("heronian", "x-00006.svg", "Heronian (15, 13, 14) | Δ = 84, a² : b² : c²"),
        ("right", "x-00006-right.svg", "Right (3, 4, 5) | Δ = 6, 9 : 16 : 25"),
        ("kepler", "x-00006-kepler.svg", "Kepler (1, √φ, φ) | 1 : φ : φ + 1"),
        ("kimberling", "x-00006-kimberling.svg", "Kimberling (6, 9, 13) | 36 : 81 : 169"),
    ]
    for preset_key, svg_name, sub_text in plate_specs:
        mdl = build_model(preset_key)
        if preset_key == "heronian":
            mdl.save(str(here / "x-00006.json"))
        write_center_svg(mdl, here / svg_name, subtitle=sub_text)
