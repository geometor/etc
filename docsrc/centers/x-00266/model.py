"""GEOMETOR construction model for X(266) = ISOGONAL CONJUGATE OF X(188)."""

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


def construct_x_00266(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(266) = ISOGONAL CONJUGATE OF X(188) on reference triangle ABC."""
    X_188 = eval_trilinear_point(model, A, B, C, 'csc(A/2)', ID="X(188)", classes=["center"])
    X_266 = isogonal_conjugate(model, A, B, C, X_188, ID="X(266)", classes=["selected", "target"])
    X_1 = incenter_of(model, A, B, C, ID="X(1)", classes=["center", "incident"])
    X_164 = eval_trilinear_point(model, A, B, C, 'sin(B/2) + sin(C/2) - sin(A/2)', ID="X(164)", classes=["center", "incident"])
    central_line(model, X_1, X_164, 1, 164, incident=True)
    X_174 = eval_trilinear_point(model, A, B, C, 'sec(A/2)', ID="X(174)", classes=["center", "incident"])
    central_line(model, X_174, X_188, 174, 188, incident=True)
    X_259 = eval_trilinear_point(model, A, B, C, 'cos(A/2)', ID="X(259)", classes=["center", "incident"])
    X_260 = eval_trilinear_point(model, A, B, C, '(cos(A/2))/(cos(B/2) + cos(C/2))', ID="X(260)", classes=["center", "incident"])
    central_line(model, X_259, X_260, 259, 260, incident=True)
    return promote_point_to_top(model, X_266)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(266) on the given reference triangle."""
    model = create_model('X(266) = ISOGONAL CONJUGATE OF X(188)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00266(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00266.json"))
    write_center_svg(
        model_acute,
        here / "x-00266.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
