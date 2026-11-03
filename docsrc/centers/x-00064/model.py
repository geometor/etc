"""GEOMETOR construction model for X_64 = ISOGONAL CONJUGATE OF X_20."""

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


def construct_x_00064(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_64 = ISOGONAL CONJUGATE OF X_20 on reference triangle ABC."""
    X_20 = eval_trilinear_point(model, A, B, C, 'cos(A) - cos(B)*cos(C)', ID="X_20", classes=["center"])
    X_64 = isogonal_conjugate(model, A, B, C, X_20, ID="X_64", classes=["selected", "target"])
    X_69 = eval_trilinear_point(model, A, B, C, '(cos(A))/a**(2)', ID="X_69", classes=["center", "incident"])
    central_line(model, X_20, X_69, 20, 69, incident=True)
    X_24 = eval_trilinear_point(model, A, B, C, 'sec(A)*cos(2*A)', ID="X_24", classes=["center", "incident"])
    X_74 = eval_trilinear_point(model, A, B, C, '1/(cos(A) - 2*cos(B)*cos(C))', ID="X_74", classes=["center", "incident"])
    central_line(model, X_24, X_74, 24, 74, incident=True)
    X_30 = eval_trilinear_point(model, A, B, C, 'cos(A) - 2*cos(B)*cos(C)', ID="X_30", classes=["center", "incident"])
    X_68 = eval_trilinear_point(model, A, B, C, 'cos(A)*sec(2*A)', ID="X_68", classes=["center", "incident"])
    central_line(model, X_30, X_68, 30, 68, incident=True)
    return promote_point_to_top(model, X_64)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_64 on the given reference triangle."""
    model = create_model('X_64 = ISOGONAL CONJUGATE OF X_20')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00064(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00064.json"))
    write_center_svg(
        model_acute,
        here / "x-00064.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
