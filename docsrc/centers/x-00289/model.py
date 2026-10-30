"""GEOMETOR construction model for X(289) = ISOGONAL CONJUGATE OF X(236)."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    incenter_of,
    isogonal_conjugate,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00289(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(289) = ISOGONAL CONJUGATE OF X(236) on reference triangle ABC."""
    X_236 = eval_trilinear_point(model, A, B, C, '(1 + sin(A/2))/sin(A)', ID="X(236)", classes=["center"])
    X_289 = isogonal_conjugate(model, A, B, C, X_236, ID="X(289)", classes=["selected", "target"])
    X_56 = eval_trilinear_point(model, A, B, C, 'a/(b + c - a)', ID="X(56)", classes=["center", "incident"])
    X_266 = eval_trilinear_point(model, A, B, C, 'sin(A/2)', ID="X(266)", classes=["center", "incident"])
    central_line(model, X_56, X_266, 56, 266, incident=True)
    X_258 = eval_trilinear_point(model, A, B, C, '1/(cos(B/2) + cos(C/2) - cos(A/2))', ID="X(258)", classes=["center", "incident"])
    X_259 = eval_trilinear_point(model, A, B, C, 'cos(A/2)', ID="X(259)", classes=["center", "incident"])
    central_line(model, X_258, X_259, 258, 259, incident=True)
    X_1 = incenter_of(model, A, B, C, ID="X(1)", classes=["center", "incident"])
    X_363 = eval_trilinear_point(model, A, B, C, 'b/(1 + sin(B/2)) + c/(1 + sin(C/2)) - a/(1 + sin(A/2))', ID="X(363)", classes=["center", "incident"])
    central_line(model, X_1, X_363, 1, 363, incident=True)
    return promote_point_to_top(model, X_289)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(289) on the given reference triangle."""
    model = create_model('X(289) = ISOGONAL CONJUGATE OF X(236)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00289(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00289.json"))
    write_center_svg(
        model_acute,
        here / "x-00289.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
