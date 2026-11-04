"""GEOMETOR construction model for X_2386 = ISOGONAL CONJUGATE OF X_2366."""

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
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_02386(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2386 = ISOGONAL CONJUGATE OF X_2366 on reference triangle ABC."""
    X_2366 = point_from_barycentrics(model, A, B, C, 0.91671538, 0.7139641, -0.63067949, ID="X_2366", classes=["center"])
    X_2386 = isogonal_conjugate(model, A, B, C, X_2366, ID="X_2386", classes=["selected", "target"])
    X_25 = eval_trilinear_point(model, A, B, C, 'sin(A)*tan(A)', ID="X_25", classes=["center", "incident"])
    X_32 = eval_trilinear_point(model, A, B, C, 'a**(3)', ID="X_32", classes=["center", "incident"])
    central_line(model, X_25, X_32, 25, 32, incident=True)
    X_30 = eval_trilinear_point(model, A, B, C, 'cos(A) - 2*cos(B)*cos(C)', ID="X_30", classes=["center", "incident"])
    X_511 = eval_trilinear_point(model, A, B, C, 'cos(A +  omega  )', ID="X_511", classes=["center", "incident"])
    central_line(model, X_30, X_511, 30, 511, incident=True)
    X_305 = eval_trilinear_point(model, A, B, C, 'b**(4)*c**(4)*cos(A)', ID="X_305", classes=["center", "incident"])
    X_315 = eval_trilinear_point(model, A, B, C, 'b*c*(b**(4) + c**(4) - a**(4))', ID="X_315", classes=["center", "incident"])
    central_line(model, X_305, X_315, 305, 315, incident=True)
    return promote_point_to_top(model, X_2386)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2386 on the given reference triangle."""
    model = create_model('X_2386 = ISOGONAL CONJUGATE OF X_2366')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02386(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02386.json"))
    write_center_svg(
        model_acute,
        here / "x-02386.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
