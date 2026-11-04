"""GEOMETOR construction model for X_2459 = INVERSE-IN-CIRCUMCIRCLE OF X_371."""

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
    promote_point_to_top,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_02459(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2459 = INVERSE-IN-CIRCUMCIRCLE OF X_371 on reference triangle ABC."""
    X_2459 = eval_trilinear_point(model, A, B, C, '(cos(A +  omega  ) - cos(omega)*sin(A) + 3*cos(A)*sin(omega) )', ID="X_2459", classes=["selected", "target"])
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center", "incident"])
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center", "incident"])
    central_line(model, X_3, X_6, 3, 6, incident=True)
    X_485 = eval_trilinear_point(model, A, B, C, 'sec(A -  pi  /4)', ID="X_485", classes=["center", "incident"])
    X_490 = eval_trilinear_point(model, A, B, C, '((cos(A))*(1 + csc(A)*sin(B)*sin(C)) - cos(B)*cos(C))', ID="X_490", classes=["center", "incident"])
    central_line(model, X_485, X_490, 485, 490, incident=True)
    return promote_point_to_top(model, X_2459)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2459 on the given reference triangle."""
    model = create_model('X_2459 = INVERSE-IN-CIRCUMCIRCLE OF X_371')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02459(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02459.json"))
    write_center_svg(
        model_acute,
        here / "x-02459.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
