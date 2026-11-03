"""GEOMETOR construction model for X_954 = INTERSECTION OF LINES X_1X_6 AND X_3X_7."""

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
    gergonne_point_of,
    incenter_of,
    promote_point_to_top,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_00954(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_954 = INTERSECTION OF LINES X_1X_6 AND X_3X_7 on reference triangle ABC."""
    X_954 = eval_trilinear_point(model, A, B, C, 'a**(5) + (b + c)*(2*a**(2)*(b**(2) + c**(2) - a**(2) + b*c) - (b - c)**(2)*(2*b*c + a*b + a*c))', ID="X_954", classes=["selected", "target"])
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center", "incident"])
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center", "incident"])
    central_line(model, X_1, X_6, 1, 6, incident=True)
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center", "incident"])
    X_7 = gergonne_point_of(model, A, B, C, ID="X_7", classes=["center", "incident"])
    central_line(model, X_3, X_7, 3, 7, incident=True)
    X_21 = eval_trilinear_point(model, A, B, C, '1/(cos(B) + cos(C))', ID="X_21", classes=["center", "incident"])
    X_144 = eval_trilinear_point(model, A, B, C, '(csc(A))*(tan(B/2) + tan(C/2) - tan(A/2))', ID="X_144", classes=["center", "incident"])
    central_line(model, X_21, X_144, 21, 144, incident=True)
    return promote_point_to_top(model, X_954)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_954 on the given reference triangle."""
    model = create_model('X_954 = INTERSECTION OF LINES X_1X_6 AND X_3X_7')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00954(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00954.json"))
    write_center_svg(
        model_acute,
        here / "x-00954.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
