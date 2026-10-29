"""GEOMETOR construction model for X(729) = EVEN (- 2, 0) CIRCUMCIRCLE POINT."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    isogonal_conjugate,
    point_from_barycentrics,
    promote_point_to_top,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_00729(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(729) = EVEN (- 2, 0) CIRCUMCIRCLE POINT on reference triangle ABC."""
    X_538 = point_from_barycentrics(model, A, B, C, -0.75777793, 0.11558409, 0.64219384, ID="X(538)", classes=["center"])
    X_729 = isogonal_conjugate(model, A, B, C, X_538, ID="X(729)", classes=["selected", "target"])
    X_6 = symmedian_point_of(model, A, B, C, ID="X(6)", classes=["center", "incident"])
    X_99 = eval_trilinear_point(model, A, B, C, 'b*c/(b**(2) - c**(2))', ID="X(99)", classes=["center", "incident"])
    central_line(model, X_6, X_99, 6, 99, incident=True)
    X_32 = eval_trilinear_point(model, A, B, C, 'a**(3)', ID="X(32)", classes=["center", "incident"])
    X_110 = eval_trilinear_point(model, A, B, C, 'csc(B - C)', ID="X(110)", classes=["center", "incident"])
    central_line(model, X_32, X_110, 32, 110, incident=True)
    X_100 = eval_trilinear_point(model, A, B, C, '1/(b - c)', ID="X(100)", classes=["center", "incident"])
    X_213 = eval_trilinear_point(model, A, B, C, '(b + c)*a**(2)', ID="X(213)", classes=["center", "incident"])
    central_line(model, X_100, X_213, 100, 213, incident=True)
    return promote_point_to_top(model, X_729)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(729) on the given reference triangle."""
    model = create_model('X(729) = EVEN (- 2, 0) CIRCUMCIRCLE POINT')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00729(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00729.json"))
    write_center_svg(
        model_acute,
        here / "x-00729.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
