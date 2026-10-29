"""GEOMETOR construction model for X(504) = 2nd ISOSCELIZER POINT."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00504(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(504) = 2nd ISOSCELIZER POINT on reference triangle ABC."""
    X_504 = eval_trilinear_point(model, A, B, C, 'b*sin(B/2) + c*sin(C/2) - a*sin(A/2)', ID="X(504)", classes=["selected", "target"])
    X_164 = eval_trilinear_point(model, A, B, C, 'sin(B/2) + sin(C/2) - sin(A/2)', ID="X(164)", classes=["center", "incident"])
    X_173 = eval_trilinear_point(model, A, B, C, 'cos(B/2) + cos(C/2) - cos(A/2)', ID="X(173)", classes=["center", "incident"])
    central_line(model, X_164, X_173, 164, 173, incident=True)
    return promote_point_to_top(model, X_504)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(504) on the given reference triangle."""
    model = create_model('X(504) = 2nd ISOSCELIZER POINT')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00504(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00504.json"))
    write_center_svg(
        model_acute,
        here / "x-00504.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
