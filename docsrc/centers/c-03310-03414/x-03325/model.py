"""GEOMETOR construction model for X_3325 = INCIRCLE TRANSFORM T(X_896)."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_barycentric_point,
    eval_trilinear_point,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_03325(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3325 = INCIRCLE TRANSFORM T(X_896) on reference triangle ABC."""
    X_3325 = eval_trilinear_point(model, A, B, C, '(a*(b - c)**(2)*(a**(2) + b**(2) + c**(2) + 3*b*c)**(2)/(b + c - a))', ID="X_3325", classes=["selected", "target"])
    X_12 = eval_trilinear_point(model, A, B, C, '1 + cos(B - C)', ID="X_12", classes=["center", "incident"])
    X_126 = eval_trilinear_point(model, A, B, C, '(b*c*(2*a**(2) - b**(2) - c**(2))*(b**(4) + c**(4) + a**(2)*(b**(2) + c**(2)) - 4*b**(2)*c**(2)))', ID="X_126", classes=["center", "incident"])
    central_line(model, X_12, X_126, 12, 126, incident=True)
    X_56 = eval_trilinear_point(model, A, B, C, 'a/(b + c - a)', ID="X_56", classes=["center", "incident"])
    X_111 = eval_trilinear_point(model, A, B, C, 'a/(2*a**(2) - b**(2) - c**(2))', ID="X_111", classes=["center", "incident"])
    central_line(model, X_56, X_111, 56, 111, incident=True)
    X_55 = eval_trilinear_point(model, A, B, C, 'a*(b + c - a)', ID="X_55", classes=["center", "incident"])
    X_1296 = eval_barycentric_point(model, A, B, C, 'a**(2)/((b**(2) - c**(2))*(5*a**(2) - b**(2) - c**(2)))', ID="X_1296", classes=["center", "incident"])
    central_line(model, X_55, X_1296, 55, 1296, incident=True)
    return promote_point_to_top(model, X_3325)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3325 on the given reference triangle."""
    model = create_model('X_3325 = INCIRCLE TRANSFORM T(X_896)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03325(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03325.json"))
    write_center_svg(
        model_acute,
        here / "x-03325.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
