"""GEOMETOR construction model for X_2408 = GIBERT-SIMSON TRANSFORM OF X_111."""

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


def construct_x_02408(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2408 = GIBERT-SIMSON TRANSFORM OF X_111 on reference triangle ABC."""
    X_2408 = eval_trilinear_point(model, A, B, C, '(b*c*(b**(2) - c**(2))*(5*a**(2) - b**(2) - c**(2))/(2*a**(2) - b**(2) - c**(2)))', ID="X_2408", classes=["selected", "target"])
    X_2 = centroid_of(model, A, B, C, ID="X_2", classes=["center", "incident"])
    X_523 = eval_trilinear_point(model, A, B, C, 'sin(B -C)', ID="X_523", classes=["center", "incident"])
    central_line(model, X_2, X_523, 2, 523, incident=True)
    X_690 = eval_trilinear_point(model, A, B, C, 'b*c*(b**(2) - c**(2))*(2*a**(2) - b**(2) - c**(2))', ID="X_690", classes=["center", "incident"])
    X_895 = eval_trilinear_point(model, A, B, C, 'a*(b**(2) + c**(2) - a**(2))/(b**(2) + c**(2) - 2*a**(2))', ID="X_895", classes=["center", "incident"])
    central_line(model, X_690, X_895, 690, 895, incident=True)
    X_691 = eval_trilinear_point(model, A, B, C, 'a/((b**(2) - c**(2))*(2*a**(2) - b**(2) - c**(2)))', ID="X_691", classes=["center", "incident"])
    X_2407 = eval_trilinear_point(model, A, B, C, '(csc(C - A)*cos(C) - csc(A - B)*cos(B))*(csc(B - C)/a)**(2)', ID="X_2407", classes=["center", "incident"])
    central_line(model, X_691, X_2407, 691, 2407, incident=True)
    return promote_point_to_top(model, X_2408)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2408 on the given reference triangle."""
    model = create_model('X_2408 = GIBERT-SIMSON TRANSFORM OF X_111')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02408(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02408.json"))
    write_center_svg(
        model_acute,
        here / "x-02408.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
