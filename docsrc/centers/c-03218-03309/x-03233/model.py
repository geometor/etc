"""GEOMETOR construction model for X_3233 = VERTEX OF THE INSCRIBED KIEPERT PARABOLA."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_03233(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3233 = VERTEX OF THE INSCRIBED KIEPERT PARABOLA on reference triangle ABC."""
    X_3233 = eval_trilinear_point(model, A, B, C, '(b*c*(a**(2) - b**(2))*(a**(2) - c**(2))*(-2*a**(4) + (b**(2) + c**(2))*a**(2) + (b**(2) - c**(2))**(2))**(2))', ID="X_3233", classes=["selected", "target"])
    X_30 = eval_trilinear_point(model, A, B, C, 'cos(A) - 2*cos(B)*cos(C)', ID="X_30", classes=["center", "incident"])
    X_113 = eval_trilinear_point(model, A, B, C, 'sin(B)*sin(C)*((sin(C))/(cos(C) - 2*cos(A)*cos(B)) + (sin(B))/(cos(B) - 2*cos(A)*cos(C)))', ID="X_113", classes=["center", "incident"])
    central_line(model, X_30, X_113, 30, 113, incident=True)
    X_114 = eval_trilinear_point(model, A, B, C, 'b*c*(b*sec(B +  omega  ) + c*sec(C +  omega  ))', ID="X_114", classes=["center", "incident"])
    X_468 = eval_trilinear_point(model, A, B, C, '(sec(A))*(cot(B) + cot(C) - 2*cot(A))', ID="X_468", classes=["center", "incident"])
    central_line(model, X_114, X_468, 114, 468, incident=True)
    X_110 = eval_trilinear_point(model, A, B, C, 'csc(B - C)', ID="X_110", classes=["center", "incident"])
    X_476 = eval_trilinear_point(model, A, B, C, '1/((1 + 2*cos(2*A))*sin(B - C))', ID="X_476", classes=["center", "incident"])
    central_line(model, X_110, X_476, 110, 476, incident=True)
    return promote_point_to_top(model, X_3233)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3233 on the given reference triangle."""
    model = create_model('X_3233 = VERTEX OF THE INSCRIBED KIEPERT PARABOLA')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03233(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03233.json"))
    write_center_svg(
        model_acute,
        here / "x-03233.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
