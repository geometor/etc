"""Exact symbolic GEOMETOR construction model for ``X_10 = SPIEKER CENTER``."""

from __future__ import annotations

from pathlib import Path

import sympy as sp
import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    centroid,
    clawson_point,
    construct_baseline_triangle,
    construct_reference_triangle,
    create_model,
    exact_center_point,
    harmonic_feuerbach_point,
    incenter,
    mittenpunkt,
    nagel_point,
    orthocenter,
    promote_point_to_top,
    spieker_center,
)
from geometor.etc.render import write_center_svg


def construct_x_00010(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct ``X_10 = SPIEKER CENTER`` and its classical incident central lines on ``ABC``.

    Constructed elements include:

    - Medial triangle ``< M_a M_b M_c >``, medial angle bisectors ``[ M_a X_10 ]``,
      ``[ M_b X_10 ]``, ``[ M_c X_10 ]``, and inscribed ``spieker_circle``.
    - Incident central lines: Nagel ``{ 1, 2 }`` (with ``X_1, X_2, X_8``),
      Orthocenter-Mittenpunkt-Clawson ``{ 4, 9 }`` (with ``X_4, X_9, X_19``),
      ``{ 12, 65 }``, and ``{ 21, 35 }``.
    """
    X_10 = spieker_center(
        model,
        A,
        B,
        C,
        ID="X_10",
        classes=["selected", "target"],
        draw_medial=True,
        draw_bisectors=True,
        draw_circle=True,
    )

    X_1 = incenter(model, A, B, C, ID="X_1", classes=["center", "incident"])
    X_2 = centroid(model, A, B, C, ID="X_2", classes=["center", "incident"])
    nagel_point(model, A, B, C, ID="X_8", classes=["center", "incident"])
    central_line(model, X_1, X_2, 1, 2, incident=True)

    X_4 = orthocenter(model, A, B, C, ID="X_4", classes=["center", "incident"])
    X_9 = mittenpunkt(model, A, B, C, ID="X_9", classes=["center", "incident"])
    clawson_point(model, A, B, C, ID="X_19", classes=["center", "incident"])
    central_line(model, X_4, X_9, 4, 9, incident=True)

    X_12 = harmonic_feuerbach_point(
        model, A, B, C, ID="X_12", classes=["center", "incident"]
    )
    X_65 = exact_center_point(
        model, A, B, C, 65, ID="X_65", classes=["center", "incident"]
    )
    central_line(model, X_12, X_65, 12, 65, incident=True)

    X_21 = exact_center_point(
        model, A, B, C, 21, ID="X_21", classes=["center", "incident"]
    )
    X_35 = exact_center_point(
        model, A, B, C, 35, ID="X_35", classes=["center", "incident"]
    )
    central_line(model, X_21, X_35, 21, 35, incident=True)

    return promote_point_to_top(model, X_10)


def build_model(
    preset: str | tuple[sp.Expr | int, sp.Expr | int, sp.Expr | int] = "heronian",
    show_guides: bool = False,
) -> Model:
    """Build an exact symbolic :class:`geometor.model.Model` for ``X_10 = SPIEKER CENTER``."""
    model = create_model("X_10 = SPIEKER CENTER")
    if isinstance(preset, str):
        A, B, C = construct_reference_triangle(model, preset, show_guides=show_guides)
    else:
        A, B, C = construct_baseline_triangle(model, *preset, show_guides=show_guides)
    construct_x_00010(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    plate_specs = [
        ("heronian", "x-00010.svg", "Heronian (15, 13, 14) | Δ = 84, r_S = 2"),
        ("right", "x-00010-right.svg", "Right (3, 4, 5) | Δ = 6, r_S = 1/2"),
        ("kepler", "x-00010-kepler.svg", "Kepler (1, √φ, φ) | Δ = √φ / 2"),
        ("kimberling", "x-00010-kimberling.svg", "Kimberling (6, 9, 13) | r_S = √35 / 7"),
    ]
    for preset_key, svg_name, sub_text in plate_specs:
        mdl = build_model(preset_key)
        if preset_key == "heronian":
            mdl.save(str(here / "x-00010.json"))
        write_center_svg(mdl, here / svg_name, subtitle=sub_text)
