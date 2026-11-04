"""GEOMETOR construction model for X_265 = REFLECTION OF X_3 IN X_125."""

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
    promote_point_to_top,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_00265(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_265 = REFLECTION OF X_3 IN X_125 on reference triangle ABC."""
    X_186 = eval_trilinear_point(model, A, B, C, '4*cos(A) - sec(A)', ID="X_186", classes=["center"])
    X_265 = isogonal_conjugate(model, A, B, C, X_186, ID="X_265", classes=["selected", "target"])
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center", "incident"])
    X_13 = eval_trilinear_point(model, A, B, C, 'csc(A +  pi  /3)', ID="X_13", classes=["center", "incident"])
    central_line(model, X_6, X_13, 6, 13, incident=True)
    X_5 = nine_point_center_of(model, A, B, C, ID="X_5", classes=["center", "incident"])
    X_49 = eval_trilinear_point(model, A, B, C, 'cos(3*A)', ID="X_49", classes=["center", "incident"])
    central_line(model, X_5, X_49, 5, 49, incident=True)
    X_4 = orthocenter_of(model, A, B, C, ID="X_4", classes=["center", "incident"])
    X_94 = eval_trilinear_point(model, A, B, C, 'csc(3*A)', ID="X_94", classes=["center", "incident"])
    central_line(model, X_4, X_94, 4, 94, incident=True)
    return promote_point_to_top(model, X_265)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_265 on the given reference triangle."""
    model = create_model('X_265 = REFLECTION OF X_3 IN X_125')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00265(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00265.json"))
    write_center_svg(
        model_acute,
        here / "x-00265.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
