"""GEOMETOR construction model for X_2679 = RS(X_98, X_99)."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    centroid_of,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_02679(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2679 = RS(X_98, X_99) on reference triangle ABC."""
    X_2679 = eval_trilinear_point(model, A, B, C, '(a*(b**(2) - c**(2))**(2)*(a**(4) - b**(2)*c**(2))*(b**(4) + c**(4) - a**(2)*b**(2) - a**(2)*c**(2)))', ID="X_2679", classes=["selected", "target"])
    X_114 = eval_trilinear_point(model, A, B, C, 'b*c*(b*sec(B +  omega  ) + c*sec(C +  omega  ))', ID="X_114", classes=["center", "incident"])
    X_325 = eval_trilinear_point(model, A, B, C, '(csc(A))**(2)', ID="X_325", classes=["center", "incident"])
    central_line(model, X_114, X_325, 114, 325, incident=True)
    X_115 = eval_trilinear_point(model, A, B, C, 'b*c*(b**(2) - c**(2))**(2)', ID="X_115", classes=["center", "incident"])
    X_512 = eval_trilinear_point(model, A, B, C, 'a*(b**(2) - c**(2))', ID="X_512", classes=["center", "incident"])
    central_line(model, X_115, X_512, 115, 512, incident=True)
    X_2 = centroid_of(model, A, B, C, ID="X_2", classes=["center", "incident"])
    X_805 = eval_trilinear_point(model, A, B, C, '(1/(a **(-3)*(b**(2) - c**(2)) + a**(1)*(b **(-2) - c **(-2))))', ID="X_805", classes=["center", "incident"])
    central_line(model, X_2, X_805, 2, 805, incident=True)
    return promote_point_to_top(model, X_2679)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2679 on the given reference triangle."""
    model = create_model('X_2679 = RS(X_98, X_99)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02679(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02679.json"))
    write_center_svg(
        model_acute,
        here / "x-02679.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
