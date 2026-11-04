"""GEOMETOR construction model for X_2847 = ISOGONAL CONJUGATE OF X_2763."""

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


def construct_x_02847(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2847 = ISOGONAL CONJUGATE OF X_2763 on reference triangle ABC."""
    X_2763 = point_from_barycentrics(model, A, B, C, 1.0032135, 0.0091142396, -0.012327716, ID="X_2763", classes=["center"])
    X_2847 = isogonal_conjugate(model, A, B, C, X_2763, ID="X_2847", classes=["selected", "target"])
    X_107 = eval_trilinear_point(model, A, B, C, '1/(cos(A)*(sin(2*B) - sin(2*C)))', ID="X_107", classes=["center", "incident"])
    X_111 = eval_trilinear_point(model, A, B, C, 'a/(2*a**(2) - b**(2) - c**(2))', ID="X_111", classes=["center", "incident"])
    central_line(model, X_107, X_111, 107, 111, incident=True)
    X_122 = eval_trilinear_point(model, A, B, C, '(b**(2) - c**(2))**(2)*(cos(A) - cos(B)*cos(C))*(cot(A))**(2)', ID="X_122", classes=["center", "incident"])
    X_126 = eval_trilinear_point(model, A, B, C, '(b*c*(2*a**(2) - b**(2) - c**(2))*(b**(4) + c**(4) + a**(2)*(b**(2) + c**(2)) - 4*b**(2)*c**(2)))', ID="X_126", classes=["center", "incident"])
    central_line(model, X_122, X_126, 122, 126, incident=True)
    X_30 = eval_trilinear_point(model, A, B, C, 'cos(A) - 2*cos(B)*cos(C)', ID="X_30", classes=["center", "incident"])
    X_511 = eval_trilinear_point(model, A, B, C, 'cos(A +  omega  )', ID="X_511", classes=["center", "incident"])
    central_line(model, X_30, X_511, 30, 511, incident=True)
    return promote_point_to_top(model, X_2847)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2847 on the given reference triangle."""
    model = create_model('X_2847 = ISOGONAL CONJUGATE OF X_2763')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02847(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02847.json"))
    write_center_svg(
        model_acute,
        here / "x-02847.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
