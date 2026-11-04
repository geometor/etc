"""GEOMETOR construction model for X_2813 = ISOGONAL CONJUGATE OF X_2729."""

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


def construct_x_02813(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2813 = ISOGONAL CONJUGATE OF X_2729 on reference triangle ABC."""
    X_2729 = point_from_barycentrics(model, A, B, C, 0.71174829, -0.30626744, 0.59451916, ID="X_2729", classes=["center"])
    X_2813 = isogonal_conjugate(model, A, B, C, X_2729, ID="X_2813", classes=["selected", "target"])
    X_42 = eval_trilinear_point(model, A, B, C, 'a*(b + c)', ID="X_42", classes=["center", "incident"])
    X_101 = eval_trilinear_point(model, A, B, C, 'a/(b - c)', ID="X_101", classes=["center", "incident"])
    central_line(model, X_42, X_101, 42, 101, incident=True)
    X_116 = eval_trilinear_point(model, A, B, C, 'b*c*((b - c)**(2)*(b**(2) + b*c + c**(2) - a*b - a*c))', ID="X_116", classes=["center", "incident"])
    X_126 = eval_trilinear_point(model, A, B, C, '(b*c*(2*a**(2) - b**(2) - c**(2))*(b**(4) + c**(4) + a**(2)*(b**(2) + c**(2)) - 4*b**(2)*c**(2)))', ID="X_126", classes=["center", "incident"])
    central_line(model, X_116, X_126, 116, 126, incident=True)
    X_30 = eval_trilinear_point(model, A, B, C, 'cos(A) - 2*cos(B)*cos(C)', ID="X_30", classes=["center", "incident"])
    X_511 = eval_trilinear_point(model, A, B, C, 'cos(A +  omega  )', ID="X_511", classes=["center", "incident"])
    central_line(model, X_30, X_511, 30, 511, incident=True)
    return promote_point_to_top(model, X_2813)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2813 on the given reference triangle."""
    model = create_model('X_2813 = ISOGONAL CONJUGATE OF X_2729')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02813(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02813.json"))
    write_center_svg(
        model_acute,
        here / "x-02813.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
