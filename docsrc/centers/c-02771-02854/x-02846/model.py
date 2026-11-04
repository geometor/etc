"""GEOMETOR construction model for X_2846 = ISOGONAL CONJUGATE OF X_2762."""

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
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_02846(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2846 = ISOGONAL CONJUGATE OF X_2762 on reference triangle ABC."""
    X_2762 = point_from_barycentrics(model, A, B, C, -0.050107095, 0.08028427, 0.96982283, ID="X_2762", classes=["center"])
    X_2846 = isogonal_conjugate(model, A, B, C, X_2762, ID="X_2846", classes=["selected", "target"])
    X_107 = eval_trilinear_point(model, A, B, C, '1/(cos(A)*(sin(2*B) - sin(2*C)))', ID="X_107", classes=["center", "incident"])
    X_109 = eval_trilinear_point(model, A, B, C, 'a/(cos(B) - cos(C))', ID="X_109", classes=["center", "incident"])
    central_line(model, X_107, X_109, 107, 109, incident=True)
    X_122 = eval_trilinear_point(model, A, B, C, '(b**(2) - c**(2))**(2)*(cos(A) - cos(B)*cos(C))*(cot(A))**(2)', ID="X_122", classes=["center", "incident"])
    X_124 = eval_trilinear_point(model, A, B, C, '(b*c*(b + c - a)*(b - c)**(2)*((b + c)*(b**(2) + c**(2) - a**(2) - b*c) + a*b*c))', ID="X_124", classes=["center", "incident"])
    central_line(model, X_122, X_124, 122, 124, incident=True)
    X_117 = point_from_barycentrics(model, A, B, C, 0.19223485, -0.017045455, 0.82481061, ID="X_117", classes=["center", "incident"])
    X_133 = eval_trilinear_point(model, A, B, C, '(sec(A))*((sin(2*B) - sin(2*C))**(2) + (sin(2*A))*(sin(2*B)) + (sin(2*A))*(sin(2*C)) - 2*(sin(2*B))*(sin(2*C)))*(2*sin(2*A) - sin(2*B) - sin(2*C))', ID="X_133", classes=["center", "incident"])
    central_line(model, X_117, X_133, 117, 133, incident=True)
    return promote_point_to_top(model, X_2846)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2846 on the given reference triangle."""
    model = create_model('X_2846 = ISOGONAL CONJUGATE OF X_2762')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02846(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02846.json"))
    write_center_svg(
        model_acute,
        here / "x-02846.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
