"""GEOMETOR construction model for X(362) = CONGRUENT CIRCUMCIRCLES ISOSCELIZER POINT."""

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


def construct_x_00362(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(362) = CONGRUENT CIRCUMCIRCLES ISOSCELIZER POINT on reference triangle ABC."""
    X_362 = eval_trilinear_point(model, A, B, C, 'b*cos(B/2) + c*cos(C/2) - a*cos(A/2)', ID="X(362)", classes=["selected", "target"])
    X_57 = eval_trilinear_point(model, A, B, C, '1/(b + c - a)', ID="X(57)", classes=["center", "incident"])
    X_234 = eval_trilinear_point(model, A, B, C, '(cos(B/2) + cos(C/2))*(cos(B/2)*cos(C/2))**(2)', ID="X(234)", classes=["center", "incident"])
    central_line(model, X_57, X_234, 57, 234, incident=True)
    return promote_point_to_top(model, X_362)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(362) on the given reference triangle."""
    model = create_model('X(362) = CONGRUENT CIRCUMCIRCLES ISOSCELIZER POINT')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00362(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00362.json"))
    write_center_svg(
        model_acute,
        here / "x-00362.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
