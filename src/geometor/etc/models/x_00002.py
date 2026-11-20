"""Exact symbolic GEOMETOR construction model for ``X_2 = CENTROID``."""

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
    feuerbach_point,
    gergonne_point,
    incenter,
    mittenpunkt,
    nagel_point,
    nine_point_center,
    orthocenter,
    promote_point_to_top,
    spieker_center,
    symmedian_point,
)
from geometor.etc.render import write_center_svg


def construct_x_00002(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct ``X_2 = CENTROID`` and its classical incident central lines on ``ABC``.

    Constructed elements include:

    - Medial triangle ``< M_a M_b M_c >`` and medians ``[ A M_a ]``, ``[ B M_b ]``,
      ``[ C M_c ]`` concurring at ``X_2``.
    - Incident central lines: Euler ``{ 3, 4 }`` (with ``X_3, X_4, X_5``),
      Nagel ``{ 1, 8 }`` (with ``X_1, X_8, X_10``), Gergonne-Mittenpunkt ``{ 7, 9 }``,
      Symmedian-Isotomic ``{ 6, 69 }``, and Feuerbach-Insimilicenter ``{ 11, 55 }``.
    """
    X_2 = centroid(
        model,
        A,
        B,
        C,
        ID="X_2",
        classes=["selected", "target"],
        draw_medians=True,
    )

    X_3 = circumcenter(model, A, B, C, ID="X_3", classes=["center", "incident"])
    X_4 = orthocenter(model, A, B, C, ID="X_4", classes=["center", "incident"])
    nine_point_center(model, A, B, C, ID="X_5", classes=["center", "incident"])
    central_line(model, X_3, X_4, 3, 4, incident=True)

    X_1 = incenter(model, A, B, C, ID="X_1", classes=["center", "incident"])
    X_8 = nagel_point(model, A, B, C, ID="X_8", classes=["center", "incident"])
    spieker_center(model, A, B, C, ID="X_10", classes=["center", "incident"])
    central_line(model, X_1, X_8, 1, 8, incident=True)

    X_7 = gergonne_point(model, A, B, C, ID="X_7", classes=["center", "incident"])
    X_9 = mittenpunkt(model, A, B, C, ID="X_9", classes=["center", "incident"])
    central_line(model, X_7, X_9, 7, 9, incident=True)

    X_6 = symmedian_point(model, A, B, C, ID="X_6", classes=["center", "incident"])
    X_69 = exact_center_point(
        model, A, B, C, 69, ID="X_69", classes=["center", "incident"]
    )
    central_line(model, X_6, X_69, 6, 69, incident=True)

    X_11 = feuerbach_point(model, A, B, C, ID="X_11", classes=["center", "incident"])
    X_55 = exact_center_point(
        model, A, B, C, 55, ID="X_55", classes=["center", "incident"]
    )
    central_line(model, X_11, X_55, 11, 55, incident=True)

    return promote_point_to_top(model, X_2)


def build_model(
    preset: str | tuple[sp.Expr | int, sp.Expr | int, sp.Expr | int] = "heronian",
    show_guides: bool = False,
) -> Model:
    """Build an exact symbolic :class:`geometor.model.Model` for ``X_2 = CENTROID``."""
    model = create_model("X_2 = CENTROID")
    if isinstance(preset, str):
        A, B, C = construct_reference_triangle(model, preset, show_guides=show_guides)
    else:
        A, B, C = construct_baseline_triangle(model, *preset, show_guides=show_guides)
    construct_x_00002(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    plate_specs = [
        ("heronian", "x-00002.svg", "Heronian (15, 13, 14) | Δ = 84, X_2 = (19/3, 4)"),
        ("right", "x-00002-right.svg", "Right (3, 4, 5) | Δ = 6, X_2 = (61/15, 4/5)"),
        ("kepler", "x-00002-kepler.svg", "Kepler (1, √φ, φ) | Δ = √φ / 2"),
        ("kimberling", "x-00002-kimberling.svg", "Kimberling (6, 9, 13) | Δ = 3√35"),
    ]
    for preset_key, svg_name, sub_text in plate_specs:
        mdl = build_model(preset_key)
        if preset_key == "heronian":
            mdl.save(str(here / "x-00002.json"))
        write_center_svg(mdl, here / svg_name, subtitle=sub_text)
