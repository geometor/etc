"""GEOMETOR construction model for X(260) = ISOGONAL CONJUGATE OF X(177)."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    circumcenter_of,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    incenter_of,
    isogonal_conjugate,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00260(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(260) = ISOGONAL CONJUGATE OF X(177) on reference triangle ABC."""
    X_177 = eval_trilinear_point(model, A, B, C, '(cos(B/2) + cos(C/2))*sec(A/2)', ID="X(177)", classes=["center"])
    X_260 = isogonal_conjugate(model, A, B, C, X_177, ID="X(260)", classes=["selected", "target"])
    X_1 = incenter_of(model, A, B, C, ID="X(1)", classes=["center", "incident"])
    X_3 = circumcenter_of(model, A, B, C, ID="X(3)", classes=["center", "incident"])
    central_line(model, X_1, X_3, 1, 3, incident=True)
    X_259 = eval_trilinear_point(model, A, B, C, 'cos(A/2)', ID="X(259)", classes=["center", "incident"])
    X_266 = eval_trilinear_point(model, A, B, C, 'sin(A/2)', ID="X(266)", classes=["center", "incident"])
    central_line(model, X_259, X_266, 259, 266, incident=True)
    return promote_point_to_top(model, X_260)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(260) on the given reference triangle."""
    model = create_model('X(260) = ISOGONAL CONJUGATE OF X(177)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00260(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00260.json"))
    write_center_svg(
        model_acute,
        here / "x-00260.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
