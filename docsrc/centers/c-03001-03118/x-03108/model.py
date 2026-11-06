"""GEOMETOR construction model for X_3108 = DC(X_83)."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    intersect_lines,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_03108(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3108 = DC(X_83) on reference triangle ABC."""
    X_39 = eval_trilinear_point(model, A, B, C, 'a*(b**(2) + c**(2))', ID="X_39", classes=["center"])
    X_251 = eval_trilinear_point(model, A, B, C, 'a**(2)*csc(A +  omega  )', ID="X_251", classes=["center"])
    X_25 = eval_trilinear_point(model, A, B, C, 'sin(A)*tan(A)', ID="X_25", classes=["center"])
    X_1180 = eval_trilinear_point(model, A, B, C, 'a*(b**(4) + c**(4) + b**(2)*c**(2) + c**(2)*a**(2) + a**(2)*b**(2))', ID="X_1180", classes=["center"])
    central_line(model, X_39, X_251, 39, 251)
    central_line(model, X_25, X_1180, 25, 1180)
    X_3108 = intersect_lines(model, X_39, X_251, X_25, X_1180, ID="X_3108", classes=["selected", "target"])
    X_111 = eval_trilinear_point(model, A, B, C, 'a/(2*a**(2) - b**(2) - c**(2))', ID="X_111", classes=["center", "incident"])
    X_1194 = eval_trilinear_point(model, A, B, C, '(a*(b**(4) + c**(4) + a**(2)*b**(2) + a**(2)*c**(2)))', ID="X_1194", classes=["center", "incident"])
    central_line(model, X_111, X_1194, 111, 1194, incident=True)
    return promote_point_to_top(model, X_3108)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3108 on the given reference triangle."""
    model = create_model('X_3108 = DC(X_83)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03108(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03108.json"))
    write_center_svg(
        model_acute,
        here / "x-03108.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
