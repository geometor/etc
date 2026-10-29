"""GEOMETOR construction model for X(249) = ISOGONAL CONJUGATE OF X(115)."""

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


def construct_x_00249(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(249) = ISOGONAL CONJUGATE OF X(115) on reference triangle ABC."""
    X_115 = eval_trilinear_point(model, A, B, C, 'b*c*(b**(2) - c**(2))**(2)', ID="X(115)", classes=["center"])
    X_249 = isogonal_conjugate(model, A, B, C, X_115, ID="X(249)", classes=["selected", "target"])
    X_186 = eval_trilinear_point(model, A, B, C, '4*cos(A) - sec(A)', ID="X(186)", classes=["center", "incident"])
    X_250 = eval_trilinear_point(model, A, B, C, '(sec(A))*(csc(B - C))**(2)', ID="X(250)", classes=["center", "incident"])
    central_line(model, X_186, X_250, 186, 250, incident=True)
    X_187 = eval_trilinear_point(model, A, B, C, 'a*(2*a**(2) - b**(2) - c**(2))', ID="X(187)", classes=["center", "incident"])
    X_323 = eval_trilinear_point(model, A, B, C, '4*sin(A) - 3*csc(A)', ID="X(323)", classes=["center", "incident"])
    central_line(model, X_187, X_323, 187, 323, incident=True)
    X_297 = eval_trilinear_point(model, A, B, C, 'csc(2*A)*cos(A + omega )', ID="X(297)", classes=["center", "incident"])
    X_316 = eval_trilinear_point(model, A, B, C, 'b*c*(b**(4)+ c**(4)- a**(4)- b**(2)*c**(2))', ID="X(316)", classes=["center", "incident"])
    central_line(model, X_297, X_316, 297, 316, incident=True)
    return promote_point_to_top(model, X_249)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(249) on the given reference triangle."""
    model = create_model('X(249) = ISOGONAL CONJUGATE OF X(115)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00249(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00249.json"))
    write_center_svg(
        model_acute,
        here / "x-00249.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
