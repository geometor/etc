"""GEOMETOR construction model for X(901) = ISOGONAL CONJUGATE OF X(900)."""

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


def construct_x_00901(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(901) = ISOGONAL CONJUGATE OF X(900) on reference triangle ABC."""
    X_901 = eval_trilinear_point(model, A, B, C, 'a/((b - c)*(b + c - 2*a))', ID="X(901)", classes=["selected", "target"])
    X_36 = eval_trilinear_point(model, A, B, C, '1 - 2*cos(A)', ID="X(36)", classes=["center", "incident"])
    X_106 = eval_trilinear_point(model, A, B, C, 'a/(2*a - b - c)', ID="X(106)", classes=["center", "incident"])
    central_line(model, X_36, X_106, 36, 106, incident=True)
    X_59 = eval_trilinear_point(model, A, B, C, '1/(1 - cos(B - C))', ID="X(59)", classes=["center", "incident"])
    X_109 = eval_trilinear_point(model, A, B, C, 'a/(cos(B) - cos(C))', ID="X(109)", classes=["center", "incident"])
    central_line(model, X_59, X_109, 59, 109, incident=True)
    X_88 = eval_trilinear_point(model, A, B, C, '1/(b + c - 2*a)', ID="X(88)", classes=["center", "incident"])
    X_105 = eval_trilinear_point(model, A, B, C, '1/(b**(2) + c**(2) - a*(b + c))', ID="X(105)", classes=["center", "incident"])
    central_line(model, X_88, X_105, 88, 105, incident=True)
    return promote_point_to_top(model, X_901)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(901) on the given reference triangle."""
    model = create_model('X(901) = ISOGONAL CONJUGATE OF X(900)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00901(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00901.json"))
    write_center_svg(
        model_acute,
        here / "x-00901.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
