"""GEOMETOR construction model for X_1326 = INVERSE-IN-CIRCUMCIRCLE OF X_58."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    ceva_conjugate,
    circumcenter_of,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    promote_point_to_top,
    spieker_center_of,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_01326(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1326 = INVERSE-IN-CIRCUMCIRCLE OF X_58 on reference triangle ABC."""
    X_741 = eval_trilinear_point(model, A, B, C, '(1/(a **(-2)*(b**(1) + c**(1)) - a**(0)*(b **(-1) + c **(-1))))', ID="X_741", classes=["center"])
    X_58 = eval_trilinear_point(model, A, B, C, 'a/(b + c)', ID="X_58", classes=["center"])
    X_1326 = ceva_conjugate(model, A, B, C, X_741, X_58, ID="X_1326", classes=["selected", "target"])
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center", "incident"])
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center", "incident"])
    central_line(model, X_3, X_6, 3, 6, incident=True)
    X_10 = spieker_center_of(model, A, B, C, ID="X_10", classes=["center", "incident"])
    X_261 = eval_trilinear_point(model, A, B, C, '(((csc(A))*(sec(B/2 - C/2)))**(2))', ID="X_261", classes=["center", "incident"])
    central_line(model, X_10, X_261, 10, 261, incident=True)
    X_42 = eval_trilinear_point(model, A, B, C, 'a*(b + c)', ID="X_42", classes=["center", "incident"])
    X_593 = eval_trilinear_point(model, A, B, C, 'a/(b + c)**(2)', ID="X_593", classes=["center", "incident"])
    central_line(model, X_42, X_593, 42, 593, incident=True)
    return promote_point_to_top(model, X_1326)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1326 on the given reference triangle."""
    model = create_model('X_1326 = INVERSE-IN-CIRCUMCIRCLE OF X_58')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01326(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01326.json"))
    write_center_svg(
        model_acute,
        here / "x-01326.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
