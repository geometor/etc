"""Exact symbolic GEOMETOR construction model for ``X_3 = CIRCUMCENTER`` (Euclid IV.5)."""

from __future__ import annotations

from pathlib import Path

import sympy as sp
import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    bevan_point,
    central_line,
    centroid,
    circumcenter,
    construct_baseline_triangle,
    construct_reference_triangle,
    create_model,
    exact_center_point,
    incenter,
    nagel_point,
    nine_point_center,
    orthocenter,
    promote_point_to_top,
    symmedian_point,
)
from geometor.etc.render import write_center_svg


def construct_x_00003(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct ``X_3 = CIRCUMCENTER`` and its classical incident central lines on ``ABC``.

    Constructed elements include:

    - Perpendicular bisectors ``[ X_3 M_a ]``, ``[ X_3 M_b ]``, ``[ X_3 M_c ]`` and
      circumscribed ``circumcircle``.
    - Incident central lines: Euler ``{ 2, 4 }`` (with ``X_2, X_4, X_5``),
      Brocard axis ``{ 6, 32 }``, ``OI`` line ``{ 1, 40 }``, and ``{ 8, 100 }``.
    """
    X_3 = circumcenter(
        model,
        A,
        B,
        C,
        ID="X_3",
        classes=["selected", "target"],
        draw_bisectors=True,
        draw_circumcircle=True,
    )

    X_2 = centroid(model, A, B, C, ID="X_2", classes=["center", "incident"])
    X_4 = orthocenter(model, A, B, C, ID="X_4", classes=["center", "incident"])
    nine_point_center(model, A, B, C, ID="X_5", classes=["center", "incident"])
    central_line(model, X_2, X_4, 2, 4, incident=True)

    X_6 = symmedian_point(model, A, B, C, ID="X_6", classes=["center", "incident"])
    X_32 = exact_center_point(
        model, A, B, C, 32, ID="X_32", classes=["center", "incident"]
    )
    central_line(model, X_6, X_32, 6, 32, incident=True)

    X_1 = incenter(model, A, B, C, ID="X_1", classes=["center", "incident"])
    X_40 = bevan_point(model, A, B, C, ID="X_40", classes=["center", "incident"])
    central_line(model, X_1, X_40, 1, 40, incident=True)

    X_8 = nagel_point(model, A, B, C, ID="X_8", classes=["center", "incident"])
    X_100 = exact_center_point(
        model, A, B, C, 100, ID="X_100", classes=["center", "incident"]
    )
    central_line(model, X_8, X_100, 8, 100, incident=True)

    return promote_point_to_top(model, X_3)


def build_model(
    preset: str | tuple[sp.Expr | int, sp.Expr | int, sp.Expr | int] = "heronian",
    show_guides: bool = False,
) -> Model:
    """Build an exact symbolic :class:`geometor.model.Model` for ``X_3 = CIRCUMCENTER``."""
    model = create_model("X_3 = CIRCUMCENTER")
    if isinstance(preset, str):
        A, B, C = construct_reference_triangle(model, preset, show_guides=show_guides)
    else:
        A, B, C = construct_baseline_triangle(model, *preset, show_guides=show_guides)
    construct_x_00003(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    plate_specs = [
        ("heronian", "x-00003.svg", "Heronian (15, 13, 14) | Δ = 84, R = 65/8"),
        ("right", "x-00003-right.svg", "Right (3, 4, 5) | Δ = 6, R = 5/2"),
        ("kepler", "x-00003-kepler.svg", "Kepler (1, √φ, φ) | R = φ / 2"),
        ("kimberling", "x-00003-kimberling.svg", "Kimberling (6, 9, 13) | R = 39√35 / 35"),
    ]
    for preset_key, svg_name, sub_text in plate_specs:
        mdl = build_model(preset_key)
        if preset_key == "heronian":
            mdl.save(str(here / "x-00003.json"))
        write_center_svg(mdl, here / svg_name, subtitle=sub_text)
