"""GEOMETOR construction model for X_1216 = ISOGONAL CONJUGATE OF X_1179."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    centroid_of,
    circumcenter_of,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    promote_point_to_top,
    reflection_in_point,
)
from geometor.etc.render import write_center_svg


def construct_x_01216(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1216 = ISOGONAL CONJUGATE OF X_1179 on reference triangle ABC."""
    X_389 = eval_trilinear_point(model, A, B, C, 'cos(A) - cos(2*A)*cos(B - C)', ID="X_389", classes=["center"])
    X_140 = eval_trilinear_point(model, A, B, C, '2*cos(A) + cos(B - C)', ID="X_140", classes=["center"])
    X_1216 = reflection_in_point(model, X_389, X_140, ID="X_1216", classes=["selected", "target"], guide=False)
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center", "incident"])
    X_49 = eval_trilinear_point(model, A, B, C, 'cos(3*A)', ID="X_49", classes=["center", "incident"])
    central_line(model, X_3, X_49, 3, 49, incident=True)
    X_2 = centroid_of(model, A, B, C, ID="X_2", classes=["center", "incident"])
    X_52 = eval_trilinear_point(model, A, B, C, 'cos(2*A)*cos(B - C)', ID="X_52", classes=["center", "incident"])
    central_line(model, X_2, X_52, 2, 52, incident=True)
    X_68 = eval_trilinear_point(model, A, B, C, 'cos(A)*sec(2*A)', ID="X_68", classes=["center", "incident"])
    X_69 = eval_trilinear_point(model, A, B, C, '(cos(A))/a**(2)', ID="X_69", classes=["center", "incident"])
    central_line(model, X_68, X_69, 68, 69, incident=True)
    return promote_point_to_top(model, X_1216)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1216 on the given reference triangle."""
    model = create_model('X_1216 = ISOGONAL CONJUGATE OF X_1179')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01216(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01216.json"))
    write_center_svg(
        model_acute,
        here / "x-01216.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
