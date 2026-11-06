"""GEOMETOR construction model for X_3459 = ISOGONAL CONJUGATE OF X_195."""

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
    nine_point_center_of,
    orthocenter_of,
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_03459(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3459 = ISOGONAL CONJUGATE OF X_195 on reference triangle ABC."""
    X_195 = eval_trilinear_point(model, A, B, C, 'a*(a**(8) + b**(8) + c**(8) - 4*a**(6)*(b**(2) + c**(2)) + a**(4)*(6*b**(4) + 6*c**(4) + 5*b**(2)*c**(2)) - a**(2)*(4*b**(6) + 4*c**(6) - b**(4)*c**(2) - b**(2)*c**(4)) - 2*b**(2)*c**(2)*(b**(4) + c**(4) - b**(2)*c**(2)))', ID="X_195", classes=["center"])
    X_3459 = isogonal_conjugate(model, A, B, C, X_195, ID="X_3459", classes=["selected", "target"])
    X_5 = nine_point_center_of(model, A, B, C, ID="X_5", classes=["center", "incident"])
    central_line(model, X_5, X_195, 5, 195, incident=True)
    X_137 = point_from_barycentrics(model, A, B, C, 0.1354431, 0.64976082, 0.21479608, ID="X_137", classes=["center", "incident"])
    X_252 = eval_trilinear_point(model, A, B, C, '(sec(B - C)/(1 - 2*cos(2*A)))', ID="X_252", classes=["center", "incident"])
    central_line(model, X_137, X_252, 137, 252, incident=True)
    X_4 = orthocenter_of(model, A, B, C, ID="X_4", classes=["center", "incident"])
    X_1157 = eval_trilinear_point(model, A, B, C, '4*cos(A) + cos(3*A)*sec(A)*sec(B - C)', ID="X_1157", classes=["center", "incident"])
    central_line(model, X_4, X_1157, 4, 1157, incident=True)
    return promote_point_to_top(model, X_3459)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3459 on the given reference triangle."""
    model = create_model('X_3459 = ISOGONAL CONJUGATE OF X_195')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03459(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03459.json"))
    write_center_svg(
        model_acute,
        here / "x-03459.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
