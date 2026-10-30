"""GEOMETOR construction model for X(259) = ISOGONAL CONJUGATE OF X(174)."""

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
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00259(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(259) = ISOGONAL CONJUGATE OF X(174) on reference triangle ABC."""
    X_174 = eval_trilinear_point(model, A, B, C, 'sec(A/2)', ID="X(174)", classes=["center"])
    X_259 = isogonal_conjugate(model, A, B, C, X_174, ID="X(259)", classes=["selected", "target"])
    X_1 = incenter_of(model, A, B, C, ID="X(1)", classes=["center", "incident"])
    X_168 = eval_trilinear_point(model, A, B, C, 'sin(A) - sin(B) - sin(C) + 2*(cos(A/2) + sin(B/2 - A/2) + sin(C/2 - A/2))', ID="X(168)", classes=["center", "incident"])
    central_line(model, X_1, X_168, 1, 168, incident=True)
    X_260 = point_from_barycentrics(model, A, B, C, 0.31448963, 0.34801807, 0.3374923, ID="X(260)", classes=["center", "incident"])
    X_266 = eval_trilinear_point(model, A, B, C, 'sin(A/2)', ID="X(266)", classes=["center", "incident"])
    central_line(model, X_260, X_266, 260, 266, incident=True)
    X_258 = eval_trilinear_point(model, A, B, C, '1/(cos(B/2) + cos(C/2) - cos(A/2))', ID="X(258)", classes=["center", "incident"])
    X_289 = eval_trilinear_point(model, A, B, C, '(sin(A/2))/(cos(B/2) + cos(C/2) - cos(A/2))', ID="X(289)", classes=["center", "incident"])
    central_line(model, X_258, X_289, 258, 289, incident=True)
    return promote_point_to_top(model, X_259)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(259) on the given reference triangle."""
    model = create_model('X(259) = ISOGONAL CONJUGATE OF X(174)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00259(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00259.json"))
    write_center_svg(
        model_acute,
        here / "x-00259.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
