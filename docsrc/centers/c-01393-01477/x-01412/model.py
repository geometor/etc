"""GEOMETOR construction model for X_1412 = X_81-BETH CONJUGATE OF X_81."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_01412(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1412 = X_81-BETH CONJUGATE OF X_81 on reference triangle ABC."""
    X_1412 = eval_trilinear_point(model, A, B, C, 'a/((b + c)*(a - b - c))', ID="X_1412", classes=["selected", "target"])
    X_56 = eval_trilinear_point(model, A, B, C, 'a/(b + c - a)', ID="X_56", classes=["center", "incident"])
    X_58 = eval_trilinear_point(model, A, B, C, 'a/(b + c)', ID="X_58", classes=["center", "incident"])
    central_line(model, X_56, X_58, 56, 58, incident=True)
    X_57 = eval_trilinear_point(model, A, B, C, '1/(b + c - a)', ID="X_57", classes=["center", "incident"])
    X_77 = eval_trilinear_point(model, A, B, C, '1/(1 + sec(A))', ID="X_77", classes=["center", "incident"])
    central_line(model, X_57, X_77, 57, 77, incident=True)
    X_86 = eval_trilinear_point(model, A, B, C, 'b*c/(b + c)', ID="X_86", classes=["center", "incident"])
    X_226 = eval_trilinear_point(model, A, B, C, '(csc(A))*(cos(B) + cos(C))', ID="X_226", classes=["center", "incident"])
    central_line(model, X_86, X_226, 86, 226, incident=True)
    return promote_point_to_top(model, X_1412)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1412 on the given reference triangle."""
    model = create_model('X_1412 = X_81-BETH CONJUGATE OF X_81')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01412(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01412.json"))
    write_center_svg(
        model_acute,
        here / "x-01412.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
