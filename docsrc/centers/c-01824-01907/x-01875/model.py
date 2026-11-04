"""GEOMETOR construction model for X_1875 = ZOSMA TRANSFORM OF X_515."""

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
    midpoint,
    orthocenter_of,
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_01875(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1875 = ZOSMA TRANSFORM OF X_515 on reference triangle ABC."""
    X_1785 = eval_trilinear_point(model, A, B, C, '(sec(A))*(cos(B) + cos(C) - 1)', ID="X_1785", classes=["center"])
    X_1845 = point_from_barycentrics(model, A, B, C, 0.12337662, 0.012987013, 0.86363636, ID="X_1845", classes=["center"])
    X_1875 = midpoint(model, X_1785, X_1845, ID="X_1875", classes=["selected", "target"], guide=False)
    X_25 = eval_trilinear_point(model, A, B, C, 'sin(A)*tan(A)', ID="X_25", classes=["center", "incident"])
    X_34 = eval_trilinear_point(model, A, B, C, '1 - sec(A)', ID="X_34", classes=["center", "incident"])
    central_line(model, X_25, X_34, 25, 34, incident=True)
    X_4 = orthocenter_of(model, A, B, C, ID="X_4", classes=["center", "incident"])
    X_65 = eval_trilinear_point(model, A, B, C, 'cos(B) + cos(C)', ID="X_65", classes=["center", "incident"])
    central_line(model, X_4, X_65, 4, 65, incident=True)
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center", "incident"])
    X_945 = eval_trilinear_point(model, A, B, C, '(a/(3*a**(4) - 2*a**(3)*(b + c) + (b - c)**(2)*(2*a*b + 2*a*c - 2*b*c - b**(2) - c**(2) - 2*a**(2))))', ID="X_945", classes=["center", "incident"])
    central_line(model, X_1, X_945, 1, 945, incident=True)
    return promote_point_to_top(model, X_1875)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1875 on the given reference triangle."""
    model = create_model('X_1875 = ZOSMA TRANSFORM OF X_515')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01875(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01875.json"))
    write_center_svg(
        model_acute,
        here / "x-01875.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
