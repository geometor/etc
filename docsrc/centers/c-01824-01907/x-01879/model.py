"""GEOMETOR construction model for X_1879 = ZOSMA TRANSFORM OF X_563."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    orthocenter_of,
    promote_point_to_top,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_01879(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1879 = ZOSMA TRANSFORM OF X_563 on reference triangle ABC."""
    X_1879 = eval_trilinear_point(model, A, B, C, 'sin(A)*cos(2*B - 2*C)', ID="X_1879", classes=["selected", "target"])
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center", "incident"])
    X_13 = eval_trilinear_point(model, A, B, C, 'csc(A + pi /3)', ID="X_13", classes=["center", "incident"])
    central_line(model, X_6, X_13, 6, 13, incident=True)
    X_4 = orthocenter_of(model, A, B, C, ID="X_4", classes=["center", "incident"])
    X_96 = eval_trilinear_point(model, A, B, C, 'sec(2*A)*sec(B - C)', ID="X_96", classes=["center", "incident"])
    central_line(model, X_4, X_96, 4, 96, incident=True)
    X_53 = eval_trilinear_point(model, A, B, C, 'tan(A)*cos(B - C)', ID="X_53", classes=["center", "incident"])
    X_235 = eval_trilinear_point(model, A, B, C, 'sec(A) - cos(B - C)', ID="X_235", classes=["center", "incident"])
    central_line(model, X_53, X_235, 53, 235, incident=True)
    return promote_point_to_top(model, X_1879)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1879 on the given reference triangle."""
    model = create_model('X_1879 = ZOSMA TRANSFORM OF X_563')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01879(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01879.json"))
    write_center_svg(
        model_acute,
        here / "x-01879.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
