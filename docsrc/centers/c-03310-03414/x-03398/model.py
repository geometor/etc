"""GEOMETOR construction model for X_3398 = COS(A - 2ω) POINT."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    circumcenter_of,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    midpoint,
    nine_point_center_of,
    promote_point_to_top,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_03398(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3398 = COS(A - 2ω) POINT on reference triangle ABC."""
    X_1342 = eval_trilinear_point(model, A, B, C, 'sin(A) + cos(A)*cot( omega  /2)', ID="X_1342", classes=["center"])
    X_1343 = eval_trilinear_point(model, A, B, C, 'sin(A) - cos(A)*tan( omega  /2)', ID="X_1343", classes=["center"])
    X_3398 = midpoint(model, X_1342, X_1343, ID="X_3398", classes=["selected", "target"], guide=False)
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center", "incident"])
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center", "incident"])
    central_line(model, X_3, X_6, 3, 6, incident=True)
    X_5 = nine_point_center_of(model, A, B, C, ID="X_5", classes=["center", "incident"])
    X_83 = eval_trilinear_point(model, A, B, C, 'b*c/(b**(2) + c**(2))', ID="X_83", classes=["center", "incident"])
    central_line(model, X_5, X_83, 5, 83, incident=True)
    X_140 = eval_trilinear_point(model, A, B, C, '2*cos(A) + cos(B - C)', ID="X_140", classes=["center", "incident"])
    X_325 = eval_trilinear_point(model, A, B, C, '(csc(A))**(2)', ID="X_325", classes=["center", "incident"])
    central_line(model, X_140, X_325, 140, 325, incident=True)
    return promote_point_to_top(model, X_3398)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3398 on the given reference triangle."""
    model = create_model('X_3398 = COS(A - 2ω) POINT')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03398(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03398.json"))
    write_center_svg(
        model_acute,
        here / "x-03398.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
