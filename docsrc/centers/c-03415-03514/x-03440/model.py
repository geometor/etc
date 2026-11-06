"""GEOMETOR construction model for X_3440 = X_15-VERTEX CONJUGATE OF X_15."""

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
    isogonal_conjugate,
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_03440(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3440 = X_15-VERTEX CONJUGATE OF X_15 on reference triangle ABC."""
    X_616 = point_from_barycentrics(model, A, B, C, 0.54029552, 0.39971531, 0.059989162, ID="X_616", classes=["center"])
    X_3440 = isogonal_conjugate(model, A, B, C, X_616, ID="X_3440", classes=["selected", "target"])
    X_30 = eval_trilinear_point(model, A, B, C, 'cos(A) - 2*cos(B)*cos(C)', ID="X_30", classes=["center", "incident"])
    X_298 = eval_trilinear_point(model, A, B, C, '(csc(A))**(2)*sin(A +  pi  /3)', ID="X_298", classes=["center", "incident"])
    central_line(model, X_30, X_298, 30, 298, incident=True)
    X_15 = eval_trilinear_point(model, A, B, C, 'sin(A +  pi  /3)', ID="X_15", classes=["center", "incident"])
    X_1495 = eval_trilinear_point(model, A, B, C, 'a*((b**(2) - c**(2))**(2) + a**(2)*(b**(2) + c**(2) - 2*a**(2)))', ID="X_1495", classes=["center", "incident"])
    central_line(model, X_15, X_1495, 15, 1495, incident=True)
    X_399 = eval_trilinear_point(model, A, B, C, '5*cos(A) - 4*cos(B)*cos(C) - 8*sin(B)*sin(C)*(cos(A))**(2)', ID="X_399", classes=["center", "incident"])
    X_1338 = eval_barycentric_point(model, A, B, C, '(a**(2)*(2*D*U + 3**(1/2)*V*W)/(4*D - 3**(1/2)*a**(2)))', ID="X_1338", classes=["center", "incident"])
    central_line(model, X_399, X_1338, 399, 1338, incident=True)
    return promote_point_to_top(model, X_3440)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3440 on the given reference triangle."""
    model = create_model('X_3440 = X_15-VERTEX CONJUGATE OF X_15')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03440(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03440.json"))
    write_center_svg(
        model_acute,
        here / "x-03440.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
