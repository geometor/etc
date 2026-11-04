"""GEOMETOR construction model for X_2985 = DC(X_56)."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    isotomic_conjugate,
    nagel_point_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_02985(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2985 = DC(X_56) on reference triangle ABC."""
    X_1029 = eval_trilinear_point(model, A, B, C, '(1/(a + 2*(a + b + c)*cos(A)))', ID="X_1029", classes=["center"])
    X_2985 = isotomic_conjugate(model, A, B, C, X_1029, ID="X_2985", classes=["selected", "target"])
    X_519 = eval_trilinear_point(model, A, B, C, '(2*a - b - c)/a', ID="X_519", classes=["center", "incident"])
    X_595 = eval_trilinear_point(model, A, B, C, 'r + R*(cos(2*A) - 1)', ID="X_595", classes=["center", "incident"])
    central_line(model, X_519, X_595, 519, 595, incident=True)
    X_8 = nagel_point_of(model, A, B, C, ID="X_8", classes=["center", "incident"])
    X_1397 = eval_trilinear_point(model, A, B, C, '((sin(A)*sin(A/2))**(2))', ID="X_1397", classes=["center", "incident"])
    central_line(model, X_8, X_1397, 8, 1397, incident=True)
    X_1999 = eval_trilinear_point(model, A, B, C, '(b*c*(a**(3) + a**(2)*b + a**(2)*c + a*b*c - b**(2)*c - b*c**(2)))', ID="X_1999", classes=["center", "incident"])
    X_2300 = eval_trilinear_point(model, A, B, C, 'a**(2)*(a*s + SA)', ID="X_2300", classes=["center", "incident"])
    central_line(model, X_1999, X_2300, 1999, 2300, incident=True)
    return promote_point_to_top(model, X_2985)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2985 on the given reference triangle."""
    model = create_model('X_2985 = DC(X_56)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02985(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02985.json"))
    write_center_svg(
        model_acute,
        here / "x-02985.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
