"""GEOMETOR construction model for X_2869 = ISOGONAL CONJUGATE OF X_2855."""

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
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_02869(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2869 = ISOGONAL CONJUGATE OF X_2855 on reference triangle ABC."""
    X_2855 = point_from_barycentrics(model, A, B, C, 0.66076696, 1.0042482, -0.66501513, ID="X_2855", classes=["center"])
    X_2869 = isogonal_conjugate(model, A, B, C, X_2855, ID="X_2869", classes=["selected", "target"])
    X_30 = eval_trilinear_point(model, A, B, C, 'cos(A) - 2*cos(B)*cos(C)', ID="X_30", classes=["center", "incident"])
    X_511 = eval_trilinear_point(model, A, B, C, 'cos(A +  omega  )', ID="X_511", classes=["center", "incident"])
    central_line(model, X_30, X_511, 30, 511, incident=True)
    X_351 = eval_trilinear_point(model, A, B, C, '(a*(b**(2) - c**(2))*(b**(2) + c**(2) - 2*a**(2)))', ID="X_351", classes=["center", "incident"])
    X_878 = point_from_barycentrics(model, A, B, C, -0.14706477, 1.0752646, 0.071800149, ID="X_878", classes=["center", "incident"])
    central_line(model, X_351, X_878, 351, 878, incident=True)
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center", "incident"])
    X_2510 = eval_trilinear_point(model, A, B, C, '(a*(b**(2) + c**(2) - a**(2))*(b**(2) - c**(2))*(a**(4) + b**(4) + c**(4) - 3*b**(2)*c**(2)))', ID="X_2510", classes=["center", "incident"])
    central_line(model, X_6, X_2510, 6, 2510, incident=True)
    return promote_point_to_top(model, X_2869)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2869 on the given reference triangle."""
    model = create_model('X_2869 = ISOGONAL CONJUGATE OF X_2855')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02869(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02869.json"))
    write_center_svg(
        model_acute,
        here / "x-02869.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
