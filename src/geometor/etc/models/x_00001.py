"""Exact symbolic GEOMETOR construction model for ``X_1 = INCENTER`` (Euclid IV.4)."""

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
    de_longchamps_point,
    feuerbach_point,
    gergonne_point,
    incenter,
    mittenpunkt,
    nagel_point,
    nine_point_center,
    promote_point_to_top,
    spieker_center,
    symmedian_point,
)
from geometor.etc.render import write_center_svg


def construct_x_00001(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct ``X_1 = INCENTER`` and its classical incident central lines on ``ABC``.

    Constructed elements include:

    - Interior angle bisectors ``[ A I_a ]``, ``[ B I_b ]``, ``[ C I_c ]`` concurring at ``X_1``.
    - Right-spread pedal touchpoints ``T_a``, ``T_b``, ``T_c`` and the inscribed ``incircle``.
    - Incident central lines: Nagel ``{ 2, 8 }`` (with ``X_2, X_8, X_10``),
      Incenter-Symmedian ``{ 6, 9 }``, Feuerbach ``{ 5, 11 }``, Soddy ``{ 7, 20 }``,
      and ``OI`` line ``{ 3, 40 }``.
    """
    X_1 = incenter(
        model,
        A,
        B,
        C,
        ID="X_1",
        classes=["selected", "target"],
        draw_bisectors=True,
        draw_incircle=True,
        draw_touchpoints=True,
    )

    X_2 = centroid(model, A, B, C, ID="X_2", classes=["center", "incident"])
    X_8 = nagel_point(model, A, B, C, ID="X_8", classes=["center", "incident"])
    spieker_center(model, A, B, C, ID="X_10", classes=["center", "incident"])
    central_line(model, X_2, X_8, 2, 8, incident=True)

    X_6 = symmedian_point(model, A, B, C, ID="X_6", classes=["center", "incident"])
    X_9 = mittenpunkt(model, A, B, C, ID="X_9", classes=["center", "incident"])
    central_line(model, X_6, X_9, 6, 9, incident=True)

    X_5 = nine_point_center(model, A, B, C, ID="X_5", classes=["center", "incident"])
    X_11 = feuerbach_point(model, A, B, C, ID="X_11", classes=["center", "incident"])
    central_line(model, X_5, X_11, 5, 11, incident=True)

    X_7 = gergonne_point(model, A, B, C, ID="X_7", classes=["center", "incident"])
    X_20 = de_longchamps_point(model, A, B, C, ID="X_20", classes=["center", "incident"])
    central_line(model, X_7, X_20, 7, 20, incident=True)

    X_3 = circumcenter(model, A, B, C, ID="X_3", classes=["center", "incident"])
    X_40 = bevan_point(model, A, B, C, ID="X_40", classes=["center", "incident"])
    central_line(model, X_3, X_40, 3, 40, incident=True)

    return promote_point_to_top(model, X_1)


def build_model(
    preset: str | tuple[sp.Expr | int, sp.Expr | int, sp.Expr | int] = "heronian",
    show_guides: bool = False,
) -> Model:
    """Build an exact symbolic :class:`geometor.model.Model` for ``X_1 = INCENTER``."""
    model = create_model("X_1 = INCENTER")
    if isinstance(preset, str):
        A, B, C = construct_reference_triangle(model, preset, show_guides=show_guides)
    else:
        A, B, C = construct_baseline_triangle(model, *preset, show_guides=show_guides)
    construct_x_00001(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    plate_specs = [
        ("heronian", "x-00001.svg", "Heronian (15, 13, 14) | Δ = 84, r = 4"),
        ("right", "x-00001-right.svg", "Right (3, 4, 5) | Δ = 6, r = 1"),
        ("kepler", "x-00001-kepler.svg", "Kepler (1, √φ, φ) | Δ = √φ / 2"),
        ("kimberling", "x-00001-kimberling.svg", "Kimberling (6, 9, 13) | r = 2√35 / 7"),
    ]
    for preset_key, svg_name, sub_text in plate_specs:
        mdl = build_model(preset_key)
        if preset_key == "heronian":
            mdl.save(str(here / "x-00001.json"))
        write_center_svg(mdl, here / svg_name, subtitle=sub_text)
