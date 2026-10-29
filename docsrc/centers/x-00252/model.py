"""GEOMETOR construction model for X(252) = ISOGONAL CONJUGATE OF X(143)."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    circumcenter_of,
    construct_baseline_triangle,
    create_model,
    eval_barycentric_point,
    eval_trilinear_point,
    isogonal_conjugate,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00252(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(252) = ISOGONAL CONJUGATE OF X(143) on reference triangle ABC."""
    X_143 = eval_trilinear_point(model, A, B, C, '(sec(A))*(cos(2*C - 2*A) + cos(2*A - 2*B))', ID="X(143)", classes=["center"])
    X_252 = isogonal_conjugate(model, A, B, C, X_143, ID="X(252)", classes=["selected", "target"])
    X_54 = eval_trilinear_point(model, A, B, C, 'sec(B - C)', ID="X(54)", classes=["center", "incident"])
    X_140 = eval_trilinear_point(model, A, B, C, '2*cos(A) + cos(B - C)', ID="X(140)", classes=["center", "incident"])
    central_line(model, X_54, X_140, 54, 140, incident=True)
    X_93 = eval_trilinear_point(model, A, B, C, 'sec(3*A)', ID="X(93)", classes=["center", "incident"])
    X_186 = eval_trilinear_point(model, A, B, C, '4*cos(A) - sec(A)', ID="X(186)", classes=["center", "incident"])
    central_line(model, X_93, X_186, 93, 186, incident=True)
    X_3 = circumcenter_of(model, A, B, C, ID="X(3)", classes=["center", "incident"])
    X_930 = eval_barycentric_point(model, A, B, C, '1/((b**(2) - c**(2))*(a**(4) + b**(4) + c**(4) - 2*a**(2)*b**(2) - 2*a**(2)*c**(2) - b**(2)*c**(2)))', ID="X(930)", classes=["center", "incident"])
    central_line(model, X_3, X_930, 3, 930, incident=True)
    return promote_point_to_top(model, X_252)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(252) on the given reference triangle."""
    model = create_model('X(252) = ISOGONAL CONJUGATE OF X(143)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00252(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00252.json"))
    write_center_svg(
        model_acute,
        here / "x-00252.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
