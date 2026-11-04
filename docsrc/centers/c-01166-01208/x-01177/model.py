"""GEOMETOR construction model for X_1177 = 1st SARAGOSSA POINT OF X_67."""

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


def construct_x_01177(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1177 = 1st SARAGOSSA POINT OF X_67 on reference triangle ABC."""
    X_858 = eval_trilinear_point(model, A, B, C, '(sin(C))**(3)*sin(2*B)*sin(C - A) + (sin(B))**(3)*sin(2*C)*sin(B - A)', ID="X_858", classes=["center"])
    X_1177 = isogonal_conjugate(model, A, B, C, X_858, ID="X_1177", classes=["selected", "target"])
    X_69 = eval_trilinear_point(model, A, B, C, '(cos(A))/a**(2)', ID="X_69", classes=["center", "incident"])
    X_110 = eval_trilinear_point(model, A, B, C, 'csc(B - C)', ID="X_110", classes=["center", "incident"])
    central_line(model, X_69, X_110, 69, 110, incident=True)
    X_66 = eval_trilinear_point(model, A, B, C, 'b*c/(b**(4) + c**(4) - a**(4))', ID="X_66", classes=["center", "incident"])
    X_125 = eval_trilinear_point(model, A, B, C, 'cos(A)*(sin(B - C))**(2)', ID="X_125", classes=["center", "incident"])
    central_line(model, X_66, X_125, 66, 125, incident=True)
    X_67 = eval_trilinear_point(model, A, B, C, 'b*c/(b**(4) + c**(4) - a**(4) - b**(2)*c**(2))', ID="X_67", classes=["center", "incident"])
    X_468 = eval_trilinear_point(model, A, B, C, '(sec(A))*(cot(B) + cot(C) - 2*cot(A))', ID="X_468", classes=["center", "incident"])
    central_line(model, X_67, X_468, 67, 468, incident=True)
    return promote_point_to_top(model, X_1177)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1177 on the given reference triangle."""
    model = create_model('X_1177 = 1st SARAGOSSA POINT OF X_67')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01177(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01177.json"))
    write_center_svg(
        model_acute,
        here / "x-01177.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
