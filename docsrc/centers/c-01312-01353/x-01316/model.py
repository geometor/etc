"""GEOMETOR construction model for X_1316 = 5th MOSES INTERSECTION."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    centroid_of,
    circumcenter_of,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    promote_point_to_top,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_01316(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1316 = 5th MOSES INTERSECTION on reference triangle ABC."""
    X_1316 = eval_trilinear_point(model, A, B, C, 'b*c*(sin(B - C))**(2) + a**(2)*sin(A - B)*sin(A - C)', ID="X_1316", classes=["selected", "target"])
    X_2 = centroid_of(model, A, B, C, ID="X_2", classes=["center"])
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center"])
    central_line(model, X_2, X_3, 2, 3)
    X_250 = eval_trilinear_point(model, A, B, C, '(sec(A))*(csc(B - C))**(2)', ID="X_250", classes=["center", "incident"])
    X_264 = eval_trilinear_point(model, A, B, C, 'csc(A)*csc(2*A)', ID="X_264", classes=["center", "incident"])
    central_line(model, X_250, X_264, 250, 264, incident=True)
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center", "incident"])
    X_523 = eval_trilinear_point(model, A, B, C, 'sin(B -C)', ID="X_523", classes=["center", "incident"])
    central_line(model, X_6, X_523, 6, 523, incident=True)
    return promote_point_to_top(model, X_1316)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1316 on the given reference triangle."""
    model = create_model('X_1316 = 5th MOSES INTERSECTION')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01316(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01316.json"))
    write_center_svg(
        model_acute,
        here / "x-01316.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
