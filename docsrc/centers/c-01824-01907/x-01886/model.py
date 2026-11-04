"""GEOMETOR construction model for X_1886 = ZOSMA TRANSFORM OF X_910."""

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
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_01886(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1886 = ZOSMA TRANSFORM OF X_910 on reference triangle ABC."""
    X_1815 = eval_trilinear_point(model, A, B, C, '(cot(A))/(a**(2) - b**(2)*cos(C) - c**(2)*cos(B))', ID="X_1815", classes=["center"])
    X_1886 = isogonal_conjugate(model, A, B, C, X_1815, ID="X_1886", classes=["selected", "target"])
    X_33 = eval_trilinear_point(model, A, B, C, '1 + sec(A)', ID="X_33", classes=["center", "incident"])
    X_42 = eval_trilinear_point(model, A, B, C, 'a*(b + c)', ID="X_42", classes=["center", "incident"])
    central_line(model, X_33, X_42, 33, 42, incident=True)
    X_19 = eval_trilinear_point(model, A, B, C, 'tan(A)', ID="X_19", classes=["center", "incident"])
    X_57 = eval_trilinear_point(model, A, B, C, '1/(b + c - a)', ID="X_57", classes=["center", "incident"])
    central_line(model, X_19, X_57, 19, 57, incident=True)
    X_230 = eval_trilinear_point(model, A, B, C, 'b*c*(a**(2)*(2*a**(2) - b**(2) - c**(2)) + (b**(2) - c**(2))**(2))', ID="X_230", classes=["center", "incident"])
    X_231 = eval_trilinear_point(model, A, B, C, '(cos(B))*(4*(sin(C))**(2) - 1)*(cos(A)*sin(B) - sin(A)*cos(B)) - (cos(C))*(4*(sin(B))**(2) - 1)*(cos(C)*sin(A) - sin(C)*cos(A))', ID="X_231", classes=["center", "incident"])
    central_line(model, X_230, X_231, 230, 231, incident=True)
    return promote_point_to_top(model, X_1886)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1886 on the given reference triangle."""
    model = create_model('X_1886 = ZOSMA TRANSFORM OF X_910')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01886(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01886.json"))
    write_center_svg(
        model_acute,
        here / "x-01886.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
