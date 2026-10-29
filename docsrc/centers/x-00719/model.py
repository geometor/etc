"""GEOMETOR construction model for X(719) = EVEN (- 3, 1) CIRCUMCIRCLE POINT."""

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


def construct_x_00719(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(719) = EVEN (- 3, 1) CIRCUMCIRCLE POINT on reference triangle ABC."""
    X_718 = eval_trilinear_point(model, A, B, C, 'a**(-4)*(b**(1)+ c**(1)) - a**(0)*(b**(-3)+ c**(-3))', ID="X(718)", classes=["center"])
    X_719 = isogonal_conjugate(model, A, B, C, X_718, ID="X(719)", classes=["selected", "target"])
    X_1 = incenter_of(model, A, B, C, ID="X(1)", classes=["center", "incident"])
    X_689 = eval_trilinear_point(model, A, B, C, '1/(a**(3)*(b**(4) - c**(4)))', ID="X(689)", classes=["center", "incident"])
    central_line(model, X_1, X_689, 1, 689, incident=True)
    X_560 = eval_trilinear_point(model, A, B, C, 'a**(4)', ID="X(560)", classes=["center", "incident"])
    X_827 = eval_trilinear_point(model, A, B, C, '1/(a**(-1)*(b**(4) - c**(4)) + a**(3)*(b**(0) - c**(0)))', ID="X(827)", classes=["center", "incident"])
    central_line(model, X_560, X_827, 560, 827, incident=True)
    return promote_point_to_top(model, X_719)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(719) on the given reference triangle."""
    model = create_model('X(719) = EVEN (- 3, 1) CIRCUMCIRCLE POINT')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00719(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00719.json"))
    write_center_svg(
        model_acute,
        here / "x-00719.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
