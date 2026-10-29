"""GEOMETOR construction model for X(741) = EVEN (- 1, 1) CIRCUMCIRCLE POINT."""

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
)
from geometor.etc.render import write_center_svg


def construct_x_00741(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(741) = EVEN (- 1, 1) CIRCUMCIRCLE POINT on reference triangle ABC."""
    X_740 = eval_trilinear_point(model, A, B, C, 'a **(-2)*(b**(1) + c**(1)) - a**(0)*(b **(-1) + c **(-1))', ID="X(740)", classes=["center"])
    X_741 = isogonal_conjugate(model, A, B, C, X_740, ID="X(741)", classes=["selected", "target"])
    X_1 = incenter_of(model, A, B, C, ID="X(1)", classes=["center", "incident"])
    X_99 = eval_trilinear_point(model, A, B, C, 'b*c/(b**(2) - c**(2))', ID="X(99)", classes=["center", "incident"])
    central_line(model, X_1, X_99, 1, 99, incident=True)
    X_42 = eval_trilinear_point(model, A, B, C, 'a*(b + c)', ID="X(42)", classes=["center", "incident"])
    X_81 = eval_trilinear_point(model, A, B, C, '1/(b + c)', ID="X(81)", classes=["center", "incident"])
    central_line(model, X_42, X_81, 42, 81, incident=True)
    X_31 = eval_trilinear_point(model, A, B, C, 'a**(2)', ID="X(31)", classes=["center", "incident"])
    X_110 = eval_trilinear_point(model, A, B, C, 'csc(B - C)', ID="X(110)", classes=["center", "incident"])
    central_line(model, X_31, X_110, 31, 110, incident=True)
    return promote_point_to_top(model, X_741)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(741) on the given reference triangle."""
    model = create_model('X(741) = EVEN (- 1, 1) CIRCUMCIRCLE POINT')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00741(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00741.json"))
    write_center_svg(
        model_acute,
        here / "x-00741.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
