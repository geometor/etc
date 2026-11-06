"""GEOMETOR construction model for X_3527 = ISOGONAL CONJUGATE OF X_631."""

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
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_03527(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3527 = ISOGONAL CONJUGATE OF X_631 on reference triangle ABC."""
    X_631 = eval_trilinear_point(model, A, B, C, '2*cos(A) + cos(B)*cos(C)', ID="X_631", classes=["center"])
    X_3527 = isogonal_conjugate(model, A, B, C, X_631, ID="X_3527", classes=["selected", "target"])
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center", "incident"])
    X_51 = eval_trilinear_point(model, A, B, C, 'a**(2)*cos(B - C)', ID="X_51", classes=["center", "incident"])
    central_line(model, X_3, X_51, 3, 51, incident=True)
    X_5 = nine_point_center_of(model, A, B, C, ID="X_5", classes=["center", "incident"])
    X_69 = eval_trilinear_point(model, A, B, C, '(cos(A))/a**(2)', ID="X_69", classes=["center", "incident"])
    central_line(model, X_5, X_69, 5, 69, incident=True)
    X_25 = eval_trilinear_point(model, A, B, C, 'sin(A)*tan(A)', ID="X_25", classes=["center", "incident"])
    X_54 = eval_trilinear_point(model, A, B, C, 'sec(B - C)', ID="X_54", classes=["center", "incident"])
    central_line(model, X_25, X_54, 25, 54, incident=True)
    return promote_point_to_top(model, X_3527)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3527 on the given reference triangle."""
    model = create_model('X_3527 = ISOGONAL CONJUGATE OF X_631')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03527(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03527.json"))
    write_center_svg(
        model_acute,
        here / "x-03527.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
