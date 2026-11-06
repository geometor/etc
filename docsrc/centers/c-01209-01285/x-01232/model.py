"""GEOMETOR construction model for X_1232 = ISOTOMIC CONJUGATE OF X_1173."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    isotomic_conjugate,
    orthocenter_of,
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_01232(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1232 = ISOTOMIC CONJUGATE OF X_1173 on reference triangle ABC."""
    X_1173 = eval_trilinear_point(model, A, B, C, 'a/(2*a**(4) - 3*a**(2)*(b**(2) + c**(2)) + (b**(2) - c**(2))**(2))', ID="X_1173", classes=["center"])
    X_1232 = isotomic_conjugate(model, A, B, C, X_1173, ID="X_1232", classes=["selected", "target"])
    X_4 = orthocenter_of(model, A, B, C, ID="X_4", classes=["center", "incident"])
    X_69 = eval_trilinear_point(model, A, B, C, '(cos(A))/a**(2)', ID="X_69", classes=["center", "incident"])
    central_line(model, X_4, X_69, 4, 69, incident=True)
    X_95 = eval_trilinear_point(model, A, B, C, 'b**(2)*c**(2)*sec(B - C)', ID="X_95", classes=["center", "incident"])
    X_252 = eval_trilinear_point(model, A, B, C, '(sec(B - C)/(1 - 2*cos(2*A)))', ID="X_252", classes=["center", "incident"])
    central_line(model, X_95, X_252, 95, 252, incident=True)
    X_313 = eval_trilinear_point(model, A, B, C, '(b + c)*b**(3)*c**(3)', ID="X_313", classes=["center", "incident"])
    X_1227 = point_from_barycentrics(model, A, B, C, 0.58333333, 1.8875832e-16, 0.41666667, ID="X_1227", classes=["center", "incident"])
    central_line(model, X_313, X_1227, 313, 1227, incident=True)
    return promote_point_to_top(model, X_1232)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1232 on the given reference triangle."""
    model = create_model('X_1232 = ISOTOMIC CONJUGATE OF X_1173')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01232(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01232.json"))
    write_center_svg(
        model_acute,
        here / "x-01232.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
