"""GEOMETOR construction model for X_3448 = ISOGONAL CONJUGATE OF X_3447."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    centroid_of,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    isogonal_conjugate,
    orthocenter_of,
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_03448(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3448 = ISOGONAL CONJUGATE OF X_3447 on reference triangle ABC."""
    X_3447 = point_from_barycentrics(model, A, B, C, 1.4554469, 0.27442248, -0.72986939, ID="X_3447", classes=["center"])
    X_3448 = isogonal_conjugate(model, A, B, C, X_3447, ID="X_3448", classes=["selected", "target"])
    X_20 = eval_trilinear_point(model, A, B, C, 'cos(A) - cos(B)*cos(C)', ID="X_20", classes=["center", "incident"])
    X_68 = eval_trilinear_point(model, A, B, C, 'cos(A)*sec(2*A)', ID="X_68", classes=["center", "incident"])
    central_line(model, X_20, X_68, 20, 68, incident=True)
    X_4 = orthocenter_of(model, A, B, C, ID="X_4", classes=["center", "incident"])
    X_94 = eval_trilinear_point(model, A, B, C, 'csc(3*A)', ID="X_94", classes=["center", "incident"])
    central_line(model, X_4, X_94, 4, 94, incident=True)
    X_2 = centroid_of(model, A, B, C, ID="X_2", classes=["center", "incident"])
    X_98 = eval_trilinear_point(model, A, B, C, 'sec(A +  omega  )', ID="X_98", classes=["center", "incident"])
    central_line(model, X_2, X_98, 2, 98, incident=True)
    return promote_point_to_top(model, X_3448)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3448 on the given reference triangle."""
    model = create_model('X_3448 = ISOGONAL CONJUGATE OF X_3447')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03448(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03448.json"))
    write_center_svg(
        model_acute,
        here / "x-03448.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
