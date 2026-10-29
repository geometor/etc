"""GEOMETOR construction model for X(947) = ISOGONAL CONJUGATE OF X(946)."""

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


def construct_x_00947(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(947) = ISOGONAL CONJUGATE OF X(946) on reference triangle ABC."""
    X_946 = eval_trilinear_point(model, A, B, C, 'b*c*(a**(3)*(b + c) + (b - c)**(2)*(a**(2) - a*b - a*c - b**(2) - c**(2) - 2*b*c))', ID="X(946)", classes=["center"])
    X_947 = isogonal_conjugate(model, A, B, C, X_946, ID="X(947)", classes=["selected", "target"])
    X_40 = eval_trilinear_point(model, A, B, C, 'cos(B) + cos(C) - cos(A) - 1', ID="X(40)", classes=["center", "incident"])
    X_77 = eval_trilinear_point(model, A, B, C, '1/(1 + sec(A))', ID="X(77)", classes=["center", "incident"])
    central_line(model, X_40, X_77, 40, 77, incident=True)
    X_73 = eval_trilinear_point(model, A, B, C, 'sec(B) + sec(C)', ID="X(73)", classes=["center", "incident"])
    X_102 = eval_trilinear_point(model, A, B, C, '1/(sin(B)*(sec(A) - sec(B)) + sin(C)*(sec(A) - sec(C)))', ID="X(102)", classes=["center", "incident"])
    central_line(model, X_73, X_102, 73, 102, incident=True)
    X_48 = eval_trilinear_point(model, A, B, C, 'tan(B) + tan(C)', ID="X(48)", classes=["center", "incident"])
    X_282 = eval_trilinear_point(model, A, B, C, '(cot(A/2))/(-1 - cos(A) + cos(B) + cos(C))', ID="X(282)", classes=["center", "incident"])
    central_line(model, X_48, X_282, 48, 282, incident=True)
    return promote_point_to_top(model, X_947)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(947) on the given reference triangle."""
    model = create_model('X(947) = ISOGONAL CONJUGATE OF X(946)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00947(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00947.json"))
    write_center_svg(
        model_acute,
        here / "x-00947.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
