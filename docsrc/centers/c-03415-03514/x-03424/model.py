"""GEOMETOR construction model for X_3424 = X_2-VERTEX CONJUGATE OF X_3."""

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
    isogonal_conjugate,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_03424(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3424 = X_2-VERTEX CONJUGATE OF X_3 on reference triangle ABC."""
    X_1350 = eval_trilinear_point(model, A, B, C, 'a - 4*R*cot(omega)*cos(A)', ID="X_1350", classes=["center"])
    X_3424 = isogonal_conjugate(model, A, B, C, X_1350, ID="X_3424", classes=["selected", "target"])
    X_20 = eval_trilinear_point(model, A, B, C, 'cos(A) - cos(B)*cos(C)', ID="X_20", classes=["center", "incident"])
    X_76 = eval_trilinear_point(model, A, B, C, '1/a**(3)', ID="X_76", classes=["center", "incident"])
    central_line(model, X_20, X_76, 20, 76, incident=True)
    X_2 = centroid_of(model, A, B, C, ID="X_2", classes=["center", "incident"])
    X_154 = eval_trilinear_point(model, A, B, C, '(cos(A) - cos(B)*cos(C))*a**(2)', ID="X_154", classes=["center", "incident"])
    central_line(model, X_2, X_154, 2, 154, incident=True)
    X_253 = eval_trilinear_point(model, A, B, C, '((csc(A))/(tan(B) + tan(C) - tan(A)))', ID="X_253", classes=["center", "incident"])
    X_1297 = eval_trilinear_point(model, A, B, C, '(a/(b**(6) + c**(6) - 2*a**(6) + a**(4)*b**(2) + a**(4)*c**(2) - b**(4)*c**(2) - b**(2)*c**(4)))', ID="X_1297", classes=["center", "incident"])
    central_line(model, X_253, X_1297, 253, 1297, incident=True)
    return promote_point_to_top(model, X_3424)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3424 on the given reference triangle."""
    model = create_model('X_3424 = X_2-VERTEX CONJUGATE OF X_3')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03424(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03424.json"))
    write_center_svg(
        model_acute,
        here / "x-03424.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
