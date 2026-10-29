"""GEOMETOR construction model for X(957) = ISOGONAL CONJUGATE OF X(956)."""

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


def construct_x_00957(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(957) = ISOGONAL CONJUGATE OF X(956) on reference triangle ABC."""
    X_956 = eval_trilinear_point(model, A, B, C, 'a**(3)- a*(b - c)**(2)- 2*b*c*(b + c)', ID="X(956)", classes=["center"])
    X_957 = isogonal_conjugate(model, A, B, C, X_956, ID="X(957)", classes=["selected", "target"])
    X_2 = centroid_of(model, A, B, C, ID="X(2)", classes=["center", "incident"])
    X_392 = eval_trilinear_point(model, A, B, C, '(b + c)*(b**(2) + c**(2) - a**(2)) + 4*a*b*c', ID="X(392)", classes=["center", "incident"])
    central_line(model, X_2, X_392, 2, 392, incident=True)
    X_81 = eval_trilinear_point(model, A, B, C, '1/(b + c)', ID="X(81)", classes=["center", "incident"])
    X_859 = eval_trilinear_point(model, A, B, C, '(sin(A) + sin(B))*sin(2*B)*sin(C - A) + (sin(A) + sin(C))*sin(2*C)*sin(B - A)', ID="X(859)", classes=["center", "incident"])
    central_line(model, X_81, X_859, 81, 859, incident=True)
    X_57 = eval_trilinear_point(model, A, B, C, '1/(b + c - a)', ID="X(57)", classes=["center", "incident"])
    X_995 = eval_trilinear_point(model, A, B, C, 'a*(a*b + a*c - b*c + b**(2) + c**(2))', ID="X(995)", classes=["center", "incident"])
    central_line(model, X_57, X_995, 57, 995, incident=True)
    return promote_point_to_top(model, X_957)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(957) on the given reference triangle."""
    model = create_model('X(957) = ISOGONAL CONJUGATE OF X(956)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00957(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00957.json"))
    write_center_svg(
        model_acute,
        here / "x-00957.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
