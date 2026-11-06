"""GEOMETOR construction model for X_3964 = X_1609com[INVERSE(n(TANGENTIAL TRIANGLE))]."""

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
    isotomic_conjugate,
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_03964(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3964 = X_1609com[INVERSE(n(TANGENTIAL TRIANGLE))] on reference triangle ABC."""
    X_1093 = point_from_barycentrics(model, A, B, C, 0.014812808, 0.040492805, 0.94469439, ID="X_1093", classes=["center"])
    X_3964 = isotomic_conjugate(model, A, B, C, X_1093, ID="X_3964", classes=["selected", "target"])
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center", "incident"])
    X_69 = eval_trilinear_point(model, A, B, C, '(cos(A))/a**(2)', ID="X_69", classes=["center", "incident"])
    central_line(model, X_3, X_69, 3, 69, incident=True)
    X_95 = eval_trilinear_point(model, A, B, C, 'b**(2)*c**(2)*sec(B - C)', ID="X_95", classes=["center", "incident"])
    X_183 = eval_trilinear_point(model, A, B, C, 'b**(2)*c**(2)*cos(A-  omega  )', ID="X_183", classes=["center", "incident"])
    central_line(model, X_95, X_183, 95, 183, incident=True)
    X_25 = eval_trilinear_point(model, A, B, C, 'sin(A)*tan(A)', ID="X_25", classes=["center", "incident"])
    X_317 = eval_trilinear_point(model, A, B, C, 'sec(A)*cos(2*A)*(csc(A))**(2)', ID="X_317", classes=["center", "incident"])
    central_line(model, X_25, X_317, 25, 317, incident=True)
    return promote_point_to_top(model, X_3964)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3964 on the given reference triangle."""
    model = create_model('X_3964 = X_1609com[INVERSE(n(TANGENTIAL TRIANGLE))]')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03964(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03964.json"))
    write_center_svg(
        model_acute,
        here / "x-03964.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
