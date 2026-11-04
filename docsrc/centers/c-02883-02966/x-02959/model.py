"""GEOMETOR construction model for X_2959 = EXCENTRAL-ISOGONAL CONJUGATE OF X_147."""

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
    point_from_barycentrics,
    promote_point_to_top,
    reflection_in_point,
)
from geometor.etc.render import write_center_svg


def construct_x_02959(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2959 = EXCENTRAL-ISOGONAL CONJUGATE OF X_147 on reference triangle ABC."""
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center"])
    X_1326 = eval_trilinear_point(model, A, B, C, '(a*(b**(2) + c**(2) - a**(2) + b*c - a*b - a*c)/(b + c))', ID="X_1326", classes=["center"])
    X_2959 = reflection_in_point(model, X_1, X_1326, ID="X_2959", classes=["selected", "target"], guide=False)
    X_40 = eval_trilinear_point(model, A, B, C, 'cos(B) + cos(C) - cos(A) - 1', ID="X_40", classes=["center", "incident"])
    X_511 = eval_trilinear_point(model, A, B, C, 'cos(A +  omega  )', ID="X_511", classes=["center", "incident"])
    central_line(model, X_40, X_511, 40, 511, incident=True)
    X_19 = eval_trilinear_point(model, A, B, C, 'tan(A)', ID="X_19", classes=["center", "incident"])
    X_1247 = point_from_barycentrics(model, A, B, C, 0.47979502, 0.29838347, 0.22182151, ID="X_1247", classes=["center", "incident"])
    central_line(model, X_19, X_1247, 19, 1247, incident=True)
    central_line(model, X_1, X_1326, 1, 1326, incident=True)
    return promote_point_to_top(model, X_2959)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2959 on the given reference triangle."""
    model = create_model('X_2959 = EXCENTRAL-ISOGONAL CONJUGATE OF X_147')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02959(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02959.json"))
    write_center_svg(
        model_acute,
        here / "x-02959.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
