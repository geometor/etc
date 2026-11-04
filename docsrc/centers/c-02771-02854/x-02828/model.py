"""GEOMETOR construction model for X_2828 = ISOGONAL CONJUGATE OF X_2744."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    feuerbach_point_of,
    isogonal_conjugate,
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_02828(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2828 = ISOGONAL CONJUGATE OF X_2744 on reference triangle ABC."""
    X_2744 = point_from_barycentrics(model, A, B, C, 0.53595872, 0.38877403, 0.07526725, ID="X_2744", classes=["center"])
    X_2828 = isogonal_conjugate(model, A, B, C, X_2744, ID="X_2828", classes=["selected", "target"])
    X_28 = eval_trilinear_point(model, A, B, C, '(tan(A))/(b + c)', ID="X_28", classes=["center", "incident"])
    X_104 = eval_trilinear_point(model, A, B, C, '1/(-1 + cos(B) + cos(C))', ID="X_104", classes=["center", "incident"])
    central_line(model, X_28, X_104, 28, 104, incident=True)
    X_11 = feuerbach_point_of(model, A, B, C, ID="X_11", classes=["center", "incident"])
    X_133 = eval_trilinear_point(model, A, B, C, '(sec(A))*((sin(2*B) - sin(2*C))**(2) + (sin(2*A))*(sin(2*B)) + (sin(2*A))*(sin(2*C)) - 2*(sin(2*B))*(sin(2*C)))*(2*sin(2*A) - sin(2*B) - sin(2*C))', ID="X_133", classes=["center", "incident"])
    central_line(model, X_11, X_133, 11, 133, incident=True)
    X_119 = eval_trilinear_point(model, A, B, C, '(csc(A))*(-1 + cos(B) + cos(C))*(sin(2*B) + sin(2*C) + 2*(-1 + cos(A))*(sin(B) + sin(C)))', ID="X_119", classes=["center", "incident"])
    X_122 = eval_trilinear_point(model, A, B, C, '(b**(2) - c**(2))**(2)*(cos(A) - cos(B)*cos(C))*(cot(A))**(2)', ID="X_122", classes=["center", "incident"])
    central_line(model, X_119, X_122, 119, 122, incident=True)
    return promote_point_to_top(model, X_2828)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2828 on the given reference triangle."""
    model = create_model('X_2828 = ISOGONAL CONJUGATE OF X_2744')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02828(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02828.json"))
    write_center_svg(
        model_acute,
        here / "x-02828.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
