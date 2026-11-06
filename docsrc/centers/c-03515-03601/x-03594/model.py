"""GEOMETOR construction model for X_3594 = ISOGONAL CONJUGATE OF 2nd DIXIT POINT."""

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


def construct_x_03594(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3594 = ISOGONAL CONJUGATE OF 2nd DIXIT POINT on reference triangle ABC."""
    X_3594 = eval_trilinear_point(model, A, B, C, '(a*(b**(2) + c**(2) - a**(2) - 6*area ))', ID="X_3594", classes=["selected", "target"])
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center", "incident"])
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center", "incident"])
    central_line(model, X_3, X_6, 3, 6, incident=True)
    X_486 = eval_trilinear_point(model, A, B, C, 'sec(A +  pi  /4)', ID="X_486", classes=["center", "incident"])
    X_546 = eval_trilinear_point(model, A, B, C, '3*cos(B - C) - 2*cos(A)', ID="X_546", classes=["center", "incident"])
    central_line(model, X_486, X_546, 486, 546, incident=True)
    X_615 = eval_trilinear_point(model, A, B, C, '(a**(2) - 4*area )/a', ID="X_615", classes=["center", "incident"])
    X_1587 = eval_trilinear_point(model, A, B, C, '(sin(A) + cos(B)*cos(C))', ID="X_1587", classes=["center", "incident"])
    central_line(model, X_615, X_1587, 615, 1587, incident=True)
    return promote_point_to_top(model, X_3594)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3594 on the given reference triangle."""
    model = create_model('X_3594 = ISOGONAL CONJUGATE OF 2nd DIXIT POINT')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03594(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03594.json"))
    write_center_svg(
        model_acute,
        here / "x-03594.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
