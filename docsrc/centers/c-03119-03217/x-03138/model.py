"""GEOMETOR construction model for X_3138 = X_103-CEVA CONJUGATE OF X_523."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    centroid_of,
    ceva_conjugate,
    circumcenter_of,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_03138(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3138 = X_103-CEVA CONJUGATE OF X_523 on reference triangle ABC."""
    X_103 = eval_trilinear_point(model, A, B, C, 'a/((a - b)*cot(C) + (a - c)*cot(B))', ID="X_103", classes=["center"])
    X_523 = eval_trilinear_point(model, A, B, C, 'sin(B -C)', ID="X_523", classes=["center"])
    X_3138 = ceva_conjugate(model, A, B, C, X_103, X_523, ID="X_3138", classes=["selected", "target"])
    X_2 = centroid_of(model, A, B, C, ID="X_2", classes=["center"])
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center"])
    central_line(model, X_2, X_3, 2, 3)
    X_116 = eval_trilinear_point(model, A, B, C, 'b*c*((b - c)**(2)*(b**(2) + b*c + c**(2) - a*b - a*c))', ID="X_116", classes=["center", "incident"])
    X_125 = eval_trilinear_point(model, A, B, C, 'cos(A)*(sin(B - C))**(2)', ID="X_125", classes=["center", "incident"])
    central_line(model, X_116, X_125, 116, 125, incident=True)
    X_2972 = eval_trilinear_point(model, A, B, C, '((b*c*(b**(2) - c**(2)))**(2)*(cos(A))**(3))', ID="X_2972", classes=["center", "incident"])
    X_2973 = eval_trilinear_point(model, A, B, C, '((b*c*(b - c))**(2)*cos(B)*cos(C))', ID="X_2973", classes=["center", "incident"])
    central_line(model, X_2972, X_2973, 2972, 2973, incident=True)
    return promote_point_to_top(model, X_3138)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3138 on the given reference triangle."""
    model = create_model('X_3138 = X_103-CEVA CONJUGATE OF X_523')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03138(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03138.json"))
    write_center_svg(
        model_acute,
        here / "x-03138.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
