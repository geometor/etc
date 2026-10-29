"""GEOMETOR construction model for X(482) = 2nd EPPSTEIN POINT."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    ceva_conjugate,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    gergonne_point_of,
    incenter_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00482(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(482) = 2nd EPPSTEIN POINT on reference triangle ABC."""
    X_79 = eval_trilinear_point(model, A, B, C, '1/(1 + 2*cos(A))', ID="X(79)", classes=["center"])
    X_481 = eval_trilinear_point(model, A, B, C, '1 - 2*sec(A/2)*cos(B/2)*cos(C/2)', ID="X(481)", classes=["center"])
    X_482 = ceva_conjugate(model, A, B, C, X_79, X_481, ID="X(482)", classes=["selected", "target"])
    X_1 = incenter_of(model, A, B, C, ID="X(1)", classes=["center", "incident"])
    X_7 = gergonne_point_of(model, A, B, C, ID="X(7)", classes=["center", "incident"])
    central_line(model, X_1, X_7, 1, 7, incident=True)
    X_226 = eval_trilinear_point(model, A, B, C, '(csc(A))*(cos(B) + cos(C))', ID="X(226)", classes=["center", "incident"])
    X_486 = eval_trilinear_point(model, A, B, C, 'sec(A + pi /4)', ID="X(486)", classes=["center", "incident"])
    central_line(model, X_226, X_486, 226, 486, incident=True)
    return promote_point_to_top(model, X_482)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(482) on the given reference triangle."""
    model = create_model('X(482) = 2nd EPPSTEIN POINT')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00482(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00482.json"))
    write_center_svg(
        model_acute,
        here / "x-00482.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
