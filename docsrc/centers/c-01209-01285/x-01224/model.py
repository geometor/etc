"""GEOMETOR construction model for X_1224 = ISOGONAL CONJUGATE OF X_1203."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    isogonal_conjugate,
    promote_point_to_top,
    spieker_center_of,
)
from geometor.etc.render import write_center_svg


def construct_x_01224(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1224 = ISOGONAL CONJUGATE OF X_1203 on reference triangle ABC."""
    X_1203 = eval_trilinear_point(model, A, B, C, '(a*((a + b + c)**(2) - b*c))', ID="X_1203", classes=["center"])
    X_1224 = isogonal_conjugate(model, A, B, C, X_1203, ID="X_1224", classes=["selected", "target"])
    X_12 = eval_trilinear_point(model, A, B, C, '1 + cos(B - C)', ID="X_12", classes=["center", "incident"])
    X_57 = eval_trilinear_point(model, A, B, C, '1/(b + c - a)', ID="X_57", classes=["center", "incident"])
    central_line(model, X_12, X_57, 12, 57, incident=True)
    X_10 = spieker_center_of(model, A, B, C, ID="X_10", classes=["center", "incident"])
    X_81 = eval_trilinear_point(model, A, B, C, '1/(b + c)', ID="X_81", classes=["center", "incident"])
    central_line(model, X_10, X_81, 10, 81, incident=True)
    X_274 = eval_trilinear_point(model, A, B, C, 'b**(2)*c**(2)/(b + c)', ID="X_274", classes=["center", "incident"])
    X_313 = eval_trilinear_point(model, A, B, C, '(b + c)*b**(3)*c**(3)', ID="X_313", classes=["center", "incident"])
    central_line(model, X_274, X_313, 274, 313, incident=True)
    return promote_point_to_top(model, X_1224)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1224 on the given reference triangle."""
    model = create_model('X_1224 = ISOGONAL CONJUGATE OF X_1203')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01224(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01224.json"))
    write_center_svg(
        model_acute,
        here / "x-01224.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
