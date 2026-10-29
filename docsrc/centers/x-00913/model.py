"""GEOMETOR construction model for X(913) = POINT AGENA."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    intersect_lines,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00913(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(913) = POINT AGENA on reference triangle ABC."""
    X_19 = eval_trilinear_point(model, A, B, C, 'tan(A)', ID="X(19)", classes=["center"])
    X_101 = eval_trilinear_point(model, A, B, C, 'a/(b - c)', ID="X(101)", classes=["center"])
    X_27 = eval_trilinear_point(model, A, B, C, '(sec(A))/(b + c)', ID="X(27)", classes=["center"])
    X_662 = eval_trilinear_point(model, A, B, C, '1/(cot(B) - cot(C))', ID="X(662)", classes=["center"])
    central_line(model, X_19, X_101, 19, 101)
    central_line(model, X_27, X_662, 27, 662)
    X_913 = intersect_lines(model, X_19, X_101, X_27, X_662, ID="X(913)", classes=["selected", "target"])
    X_25 = eval_trilinear_point(model, A, B, C, 'sin(A)*tan(A)', ID="X(25)", classes=["center", "incident"])
    X_692 = eval_trilinear_point(model, A, B, C, 'a**(2)/(b - c)', ID="X(692)", classes=["center", "incident"])
    central_line(model, X_25, X_692, 25, 692, incident=True)
    return promote_point_to_top(model, X_913)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(913) on the given reference triangle."""
    model = create_model('X(913) = POINT AGENA')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00913(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00913.json"))
    write_center_svg(
        model_acute,
        here / "x-00913.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
