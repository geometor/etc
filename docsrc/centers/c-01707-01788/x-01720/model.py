"""GEOMETOR construction model for X_1720 = MIMOSA TRANSFORM OF X_40."""

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
    incenter_of,
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_01720(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1720 = MIMOSA TRANSFORM OF X_40 on reference triangle ABC."""
    X_1158 = eval_trilinear_point(model, A, B, C, 'a**(6) - b**(6) - c**(6) + b**(2)*c**(2)*(b**(2) + c**(2)) + 3*a**(2)*(b**(4) + c**(4) - a**(2)*b**(2) - a**(2)*c**(2)) + 2*a*b*c*(a**(3) - b**(3) - c**(3) - a*b*c + (a**(2) + b*c)*(b + c) - a*b**(2) - a*c**(2))', ID="X_1158", classes=["center"])
    X_46 = eval_trilinear_point(model, A, B, C, 'cos(B) + cos(C) - cos(A)', ID="X_46", classes=["center"])
    X_1720 = ceva_conjugate(model, A, B, C, X_1158, X_46, ID="X_1720", classes=["selected", "target"])
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center", "incident"])
    X_84 = eval_trilinear_point(model, A, B, C, '1/(cos(B) + cos(C) - cos(A) - 1)', ID="X_84", classes=["center", "incident"])
    central_line(model, X_1, X_84, 1, 84, incident=True)
    X_208 = eval_trilinear_point(model, A, B, C, '((1 - sec(A))*(cos(B) + cos(C) - cos(A) - 1))', ID="X_208", classes=["center", "incident"])
    central_line(model, X_46, X_208, 46, 208, incident=True)
    X_90 = eval_trilinear_point(model, A, B, C, '1/(cos(B) + cos(C) - cos(A))', ID="X_90", classes=["center", "incident"])
    X_1718 = point_from_barycentrics(model, A, B, C, 0.43333333, -0.6, 1.1666667, ID="X_1718", classes=["center", "incident"])
    central_line(model, X_90, X_1718, 90, 1718, incident=True)
    return promote_point_to_top(model, X_1720)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1720 on the given reference triangle."""
    model = create_model('X_1720 = MIMOSA TRANSFORM OF X_40')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01720(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01720.json"))
    write_center_svg(
        model_acute,
        here / "x-01720.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
