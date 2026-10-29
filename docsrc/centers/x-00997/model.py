"""GEOMETOR construction model for X(997) = MIDPOINT OF X(1) AND X(200)."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    centroid_of,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    incenter_of,
    mittenpunkt_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00997(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(997) = MIDPOINT OF X(1) AND X(200) on reference triangle ABC."""
    X_997 = eval_trilinear_point(model, A, B, C, 'a**(3)- a**(2)*(b + c) - a*(b - c)**(2)+ (b + c)*(b**(2)+ c**(2))', ID="X(997)", classes=["selected", "target"])
    X_1 = incenter_of(model, A, B, C, ID="X(1)", classes=["center", "incident"])
    X_2 = centroid_of(model, A, B, C, ID="X(2)", classes=["center", "incident"])
    central_line(model, X_1, X_2, 1, 2, incident=True)
    X_9 = mittenpunkt_of(model, A, B, C, ID="X(9)", classes=["center", "incident"])
    X_48 = eval_trilinear_point(model, A, B, C, 'tan(B) + tan(C)', ID="X(48)", classes=["center", "incident"])
    central_line(model, X_9, X_48, 9, 48, incident=True)
    X_36 = eval_trilinear_point(model, A, B, C, '1 - 2*cos(A)', ID="X(36)", classes=["center", "incident"])
    X_63 = eval_trilinear_point(model, A, B, C, 'cot(A)', ID="X(63)", classes=["center", "incident"])
    central_line(model, X_36, X_63, 36, 63, incident=True)
    return promote_point_to_top(model, X_997)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(997) on the given reference triangle."""
    model = create_model('X(997) = MIDPOINT OF X(1) AND X(200)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00997(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00997.json"))
    write_center_svg(
        model_acute,
        here / "x-00997.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
