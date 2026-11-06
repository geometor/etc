"""GEOMETOR construction model for X_3804 = X_647com[INVERSE(nT(a², a² + c²))]."""

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
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_03804(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3804 = X_647com[INVERSE(nT(a², a² + c²))] on reference triangle ABC."""
    X_3804 = eval_barycentric_point(model, A, B, C, '(a**(2)*(b**(2) - c**(2))*(3*a**(2) + b**(2) + c**(2)))', ID="X_3804", classes=["selected", "target"])
    X_187 = eval_trilinear_point(model, A, B, C, 'a*(2*a**(2) - b**(2) - c**(2))', ID="X_187", classes=["center", "incident"])
    X_237 = eval_trilinear_point(model, A, B, C, 'a**(2)*cos(A +  omega  )', ID="X_237", classes=["center", "incident"])
    central_line(model, X_187, X_237, 187, 237, incident=True)
    X_1499 = eval_trilinear_point(model, A, B, C, 'b*c*(b**(2) - c**(2))*(b**(2) + c**(2) - 5*a**(2))', ID="X_1499", classes=["center", "incident"])
    X_3265 = eval_trilinear_point(model, A, B, C, '((csc(A))**(2))*(cos(A))*(sin(2*B) - sin(2*C))', ID="X_3265", classes=["center", "incident"])
    central_line(model, X_1499, X_3265, 1499, 3265, incident=True)
    X_2525 = eval_trilinear_point(model, A, B, C, '(b*c*(b**(4) - c**(4))*(b**(2) + c**(2) - a**(2)))', ID="X_2525", classes=["center", "incident"])
    X_3566 = eval_trilinear_point(model, A, B, C, '(b*c*(3*a**(2) - b**(2) - c**(2))*(b**(2) - c**(2)))', ID="X_3566", classes=["center", "incident"])
    central_line(model, X_2525, X_3566, 2525, 3566, incident=True)
    return promote_point_to_top(model, X_3804)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3804 on the given reference triangle."""
    model = create_model('X_3804 = X_647com[INVERSE(nT(a², a² + c²))]')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03804(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03804.json"))
    write_center_svg(
        model_acute,
        here / "x-03804.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
