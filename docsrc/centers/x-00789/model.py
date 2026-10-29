"""GEOMETOR construction model for X(789) = o-(- 3, 0) CIRCUMCIRCLE POINT."""

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
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_00789(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(789) = o-(- 3, 0) CIRCUMCIRCLE POINT on reference triangle ABC."""
    X_788 = eval_trilinear_point(model, A, B, C, 'a**(2)*(b**(3) - c**(3))', ID="X(788)", classes=["center"])
    X_789 = isogonal_conjugate(model, A, B, C, X_788, ID="X(789)", classes=["selected", "target"])
    X_6 = symmedian_point_of(model, A, B, C, ID="X(6)", classes=["center", "incident"])
    X_717 = eval_trilinear_point(model, A, B, C, '1/(a**(-4)*(b**(0)+ c**(0)) - a**(-1)*(b**(-3)+ c**(-3)))', ID="X(717)", classes=["center", "incident"])
    central_line(model, X_6, X_717, 6, 717, incident=True)
    X_1 = incenter_of(model, A, B, C, ID="X(1)", classes=["center", "incident"])
    X_731 = eval_trilinear_point(model, A, B, C, '1/(a**(-3)*(b**(1)+ c**(1)) - a**(0)*(b**(-2)+ c**(-2)))', ID="X(731)", classes=["center", "incident"])
    central_line(model, X_1, X_731, 1, 731, incident=True)
    X_31 = eval_trilinear_point(model, A, B, C, 'a**(2)', ID="X(31)", classes=["center", "incident"])
    X_701 = eval_trilinear_point(model, A, B, C, '1/(a**(-5)*(b**(-1)+ c**(-1)) - a**(-2)*(b**(-4)+ c**(-4)))', ID="X(701)", classes=["center", "incident"])
    central_line(model, X_31, X_701, 31, 701, incident=True)
    return promote_point_to_top(model, X_789)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(789) on the given reference triangle."""
    model = create_model('X(789) = o-(- 3, 0) CIRCUMCIRCLE POINT')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00789(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00789.json"))
    write_center_svg(
        model_acute,
        here / "x-00789.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
