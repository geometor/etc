"""GEOMETOR construction model for X_1780 = MIMOSA TRANSFORM OF X_1175."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    ceva_conjugate,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    incenter_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_01780(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1780 = MIMOSA TRANSFORM OF X_1175 on reference triangle ABC."""
    X_27 = eval_trilinear_point(model, A, B, C, '(sec(A))/(b + c)', ID="X_27", classes=["center"])
    X_284 = eval_trilinear_point(model, A, B, C, '(sin(A))/(cos(B) + cos(C))', ID="X_284", classes=["center"])
    X_1780 = ceva_conjugate(model, A, B, C, X_27, X_284, ID="X_1780", classes=["selected", "target"])
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center", "incident"])
    X_21 = eval_trilinear_point(model, A, B, C, '1/(cos(B) + cos(C))', ID="X_21", classes=["center", "incident"])
    central_line(model, X_1, X_21, 1, 21, incident=True)
    X_28 = eval_trilinear_point(model, A, B, C, '(tan(A))/(b + c)', ID="X_28", classes=["center", "incident"])
    X_46 = eval_trilinear_point(model, A, B, C, 'cos(B) + cos(C) - cos(A)', ID="X_46", classes=["center", "incident"])
    central_line(model, X_28, X_46, 28, 46, incident=True)
    X_35 = eval_trilinear_point(model, A, B, C, '1 + 2*cos(A)', ID="X_35", classes=["center", "incident"])
    X_71 = eval_trilinear_point(model, A, B, C, '(b + c)*cos(A)', ID="X_71", classes=["center", "incident"])
    central_line(model, X_35, X_71, 35, 71, incident=True)
    return promote_point_to_top(model, X_1780)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1780 on the given reference triangle."""
    model = create_model('X_1780 = MIMOSA TRANSFORM OF X_1175')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01780(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01780.json"))
    write_center_svg(
        model_acute,
        here / "x-01780.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
