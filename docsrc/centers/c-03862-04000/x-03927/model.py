"""GEOMETOR construction model for X_3927 = X_1com[INVERSE(n(EXTANGENTS TRIANGLE))]."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    circumcenter_of,
    construct_baseline_triangle,
    create_model,
    eval_barycentric_point,
    eval_trilinear_point,
    nagel_point_of,
    orthocenter_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_03927(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3927 = X_1com[INVERSE(n(EXTANGENTS TRIANGLE))] on reference triangle ABC."""
    X_3927 = eval_barycentric_point(model, A, B, C, '(a*(2*b + 2*c + a)*(b**(2) + c**(2) - a**(2)))', ID="X_3927", classes=["selected", "target"])
    X_8 = nagel_point_of(model, A, B, C, ID="X_8", classes=["center", "incident"])
    X_30 = eval_trilinear_point(model, A, B, C, 'cos(A) - 2*cos(B)*cos(C)', ID="X_30", classes=["center", "incident"])
    central_line(model, X_8, X_30, 8, 30, incident=True)
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center", "incident"])
    X_63 = eval_trilinear_point(model, A, B, C, 'cot(A)', ID="X_63", classes=["center", "incident"])
    central_line(model, X_3, X_63, 3, 63, incident=True)
    X_4 = orthocenter_of(model, A, B, C, ID="X_4", classes=["center", "incident"])
    X_144 = eval_trilinear_point(model, A, B, C, '(csc(A))*(tan(B/2) + tan(C/2) - tan(A/2))', ID="X_144", classes=["center", "incident"])
    central_line(model, X_4, X_144, 4, 144, incident=True)
    return promote_point_to_top(model, X_3927)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3927 on the given reference triangle."""
    model = create_model('X_3927 = X_1com[INVERSE(n(EXTANGENTS TRIANGLE))]')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03927(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03927.json"))
    write_center_svg(
        model_acute,
        here / "x-03927.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
