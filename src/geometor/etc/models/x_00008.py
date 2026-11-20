"""Exact symbolic GEOMETOR construction model for ``X_8 = NAGEL POINT``."""

from __future__ import annotations

from pathlib import Path

import sympy as sp
import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    centroid,
    circumcenter,
    construct_baseline_triangle,
    construct_reference_triangle,
    create_model,
    exact_center_point,
    gergonne_point,
    incenter,
    nagel_point,
    orthocenter,
    promote_point_to_top,
    spieker_center,
)
from geometor.etc.render import write_center_svg


def construct_x_00008(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct ``X_8 = NAGEL POINT`` and its classical incident central lines on ``ABC``.

    Constructed elements include:

    - Extouch triangle ``< N_a N_b N_c >`` and Nagel cevians ``[ A N_a ]``,
      ``[ B N_b ]``, ``[ C N_c ]`` concurring at ``X_8``.
    - Incident central lines: Nagel ``{ 1, 2 }`` (with ``X_1, X_2, X_10``),
      Gergonne-Intouch ``{ 7, 65 }``, ``{ 4, 72 }``, and ``{ 3, 100 }``.
    """
    X_8 = nagel_point(
        model,
        A,
        B,
        C,
        ID="X_8",
        classes=["selected", "target"],
        draw_cevians=True,
        draw_extouch=True,
    )

    X_1 = incenter(model, A, B, C, ID="X_1", classes=["center", "incident"])
    X_2 = centroid(model, A, B, C, ID="X_2", classes=["center", "incident"])
    spieker_center(model, A, B, C, ID="X_10", classes=["center", "incident"])
    central_line(model, X_1, X_2, 1, 2, incident=True)

    X_7 = gergonne_point(model, A, B, C, ID="X_7", classes=["center", "incident"])
    X_65 = exact_center_point(
        model, A, B, C, 65, ID="X_65", classes=["center", "incident"]
    )
    central_line(model, X_7, X_65, 7, 65, incident=True)

    X_4 = orthocenter(model, A, B, C, ID="X_4", classes=["center", "incident"])
    X_72 = exact_center_point(
        model, A, B, C, 72, ID="X_72", classes=["center", "incident"]
    )
    central_line(model, X_4, X_72, 4, 72, incident=True)

    X_3 = circumcenter(model, A, B, C, ID="X_3", classes=["center", "incident"])
    X_100 = exact_center_point(
        model, A, B, C, 100, ID="X_100", classes=["center", "incident"]
    )
    central_line(model, X_3, X_100, 3, 100, incident=True)

    return promote_point_to_top(model, X_8)


def build_model(
    preset: str | tuple[sp.Expr | int, sp.Expr | int, sp.Expr | int] = "heronian",
    show_guides: bool = False,
) -> Model:
    """Build an exact symbolic :class:`geometor.model.Model` for ``X_8 = NAGEL POINT``."""
    model = create_model("X_8 = NAGEL POINT")
    if isinstance(preset, str):
        A, B, C = construct_reference_triangle(model, preset, show_guides=show_guides)
    else:
        A, B, C = construct_baseline_triangle(model, *preset, show_guides=show_guides)
    construct_x_00008(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    plate_specs = [
        ("heronian", "x-00008.svg", "Heronian (15, 13, 14) | Δ = 84, 6 : 8 : 7"),
        ("right", "x-00008-right.svg", "Right (3, 4, 5) | Δ = 6, 3 : 2 : 1"),
        ("kepler", "x-00008-kepler.svg", "Kepler (1, √φ, φ) | Δ = √φ / 2"),
        ("kimberling", "x-00008-kimberling.svg", "Kimberling (6, 9, 13) | 8 : 5 : 1"),
    ]
    for preset_key, svg_name, sub_text in plate_specs:
        mdl = build_model(preset_key)
        if preset_key == "heronian":
            mdl.save(str(here / "x-00008.json"))
        write_center_svg(mdl, here / svg_name, subtitle=sub_text)
