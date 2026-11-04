"""GEOMETOR construction model for X_2808 = ISOGONAL CONJUGATE OF X_2724."""

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
    isogonal_conjugate,
    nine_point_center_of,
    orthocenter_of,
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_02808(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2808 = ISOGONAL CONJUGATE OF X_2724 on reference triangle ABC."""
    X_2724 = point_from_barycentrics(model, A, B, C, 0.99050454, -0.024659864, 0.034155329, ID="X_2724", classes=["center"])
    X_2808 = isogonal_conjugate(model, A, B, C, X_2724, ID="X_2808", classes=["selected", "target"])
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center", "incident"])
    X_101 = eval_trilinear_point(model, A, B, C, 'a/(b - c)', ID="X_101", classes=["center", "incident"])
    central_line(model, X_3, X_101, 3, 101, incident=True)
    X_5 = nine_point_center_of(model, A, B, C, ID="X_5", classes=["center", "incident"])
    X_116 = eval_trilinear_point(model, A, B, C, 'b*c*((b - c)**(2)*(b**(2) + b*c + c**(2) - a*b - a*c))', ID="X_116", classes=["center", "incident"])
    central_line(model, X_5, X_116, 5, 116, incident=True)
    X_4 = orthocenter_of(model, A, B, C, ID="X_4", classes=["center", "incident"])
    X_150 = eval_trilinear_point(model, A, B, C, '(b*c*(b**(4) + c**(4) - a**(4) + a*(b*c**(2) +c*b**(2) - b**(3) - c**(3)) - b*c*(a**(2) + b**(2) + c**(2)) + (b + c)*a**(3)))', ID="X_150", classes=["center", "incident"])
    central_line(model, X_4, X_150, 4, 150, incident=True)
    return promote_point_to_top(model, X_2808)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2808 on the given reference triangle."""
    model = create_model('X_2808 = ISOGONAL CONJUGATE OF X_2724')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02808(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02808.json"))
    write_center_svg(
        model_acute,
        here / "x-02808.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
