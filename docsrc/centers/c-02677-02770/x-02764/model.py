"""GEOMETOR construction model for X_2764 = SR(X_107, X_112)."""

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
    intersect_lines,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_02764(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2764 = SR(X_107, X_112) on reference triangle ABC."""
    X_107 = eval_trilinear_point(model, A, B, C, '1/(cos(A)*(sin(2*B) - sin(2*C)))', ID="X_107", classes=["center"])
    X_525 = eval_trilinear_point(model, A, B, C, '(b*cos(B) - c*cos(C))/a', ID="X_525", classes=["center"])
    X_112 = eval_trilinear_point(model, A, B, C, 'a/(sin(2*B) - sin(2*C))', ID="X_112", classes=["center"])
    X_520 = eval_trilinear_point(model, A, B, C, '(cos(A))*(sin(2*B) - sin(2*C))', ID="X_520", classes=["center"])
    central_line(model, X_107, X_525, 107, 525)
    central_line(model, X_112, X_520, 112, 520)
    X_2764 = intersect_lines(model, X_107, X_525, X_112, X_520, ID="X_2764", classes=["selected", "target"])
    X_1294 = eval_barycentric_point(model, A, B, C, '1/(a**(6)*(b**(2) + c**(2)) - a**(4)*(3*b**(4) - 4*b**(2)*c**(2) + 3*c**(4)) + 3*a**(2)*(b**(2) - c**(2))**(2)*(b**(2) + c**(2)) - (b**(2) - c**(2))**(2)*(b**(4) + 4*b**(2)*c**(2) + c**(4)))', ID="X_1294", classes=["center", "incident"])
    X_1503 = eval_trilinear_point(model, A, B, C, 'sin(A)*tan(omega)  - 2*cos(B)*cos(C)', ID="X_1503", classes=["center", "incident"])
    central_line(model, X_1294, X_1503, 1294, 1503, incident=True)
    return promote_point_to_top(model, X_2764)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2764 on the given reference triangle."""
    model = create_model('X_2764 = SR(X_107, X_112)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02764(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02764.json"))
    write_center_svg(
        model_acute,
        here / "x-02764.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
