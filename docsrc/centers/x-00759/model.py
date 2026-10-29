"""GEOMETOR construction model for X(759) = EVEN (1, 3) CIRCUMCIRCLE POINT."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    incenter_of,
    isogonal_conjugate,
    promote_point_to_top,
    spieker_center_of,
)
from geometor.etc.render import write_center_svg


def construct_x_00759(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(759) = EVEN (1, 3) CIRCUMCIRCLE POINT on reference triangle ABC."""
    X_758 = eval_trilinear_point(model, A, B, C, 'a**(0)*(b**(3) + c**(3)) - a**(2)*(b**(1) + c**(1))', ID="X(758)", classes=["center"])
    X_759 = isogonal_conjugate(model, A, B, C, X_758, ID="X(759)", classes=["selected", "target"])
    X_10 = spieker_center_of(model, A, B, C, ID="X(10)", classes=["center", "incident"])
    X_21 = eval_trilinear_point(model, A, B, C, '1/(cos(B) + cos(C))', ID="X(21)", classes=["center", "incident"])
    central_line(model, X_10, X_21, 10, 21, incident=True)
    X_1 = incenter_of(model, A, B, C, ID="X(1)", classes=["center", "incident"])
    X_60 = eval_trilinear_point(model, A, B, C, '1/(1 + cos(B - C))', ID="X(60)", classes=["center", "incident"])
    central_line(model, X_1, X_60, 1, 60, incident=True)
    X_58 = eval_trilinear_point(model, A, B, C, 'a/(b + c)', ID="X(58)", classes=["center", "incident"])
    X_65 = eval_trilinear_point(model, A, B, C, 'cos(B) + cos(C)', ID="X(65)", classes=["center", "incident"])
    central_line(model, X_58, X_65, 58, 65, incident=True)
    return promote_point_to_top(model, X_759)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(759) on the given reference triangle."""
    model = create_model('X(759) = EVEN (1, 3) CIRCUMCIRCLE POINT')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00759(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00759.json"))
    write_center_svg(
        model_acute,
        here / "x-00759.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
