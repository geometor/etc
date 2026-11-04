"""GEOMETOR construction model for X_1182 = 2nd SARAGOSSA POINT OF X_19."""

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
    intersect_lines,
    mittenpunkt_of,
    promote_point_to_top,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_01182(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1182 = 2nd SARAGOSSA POINT OF X_19 on reference triangle ABC."""
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center"])
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center"])
    X_19 = eval_trilinear_point(model, A, B, C, 'tan(A)', ID="X_19", classes=["center"])
    X_208 = eval_trilinear_point(model, A, B, C, '((1 - sec(A))*(cos(B) + cos(C) - cos(A) - 1))', ID="X_208", classes=["center"])
    central_line(model, X_3, X_6, 3, 6)
    central_line(model, X_19, X_208, 19, 208)
    X_1182 = intersect_lines(model, X_3, X_6, X_19, X_208, ID="X_1182", classes=["selected", "target"])
    X_9 = mittenpunkt_of(model, A, B, C, ID="X_9", classes=["center", "incident"])
    X_498 = eval_trilinear_point(model, A, B, C, '1 + 2*sin(B)*sin(C)', ID="X_498", classes=["center", "incident"])
    central_line(model, X_9, X_498, 9, 498, incident=True)
    return promote_point_to_top(model, X_1182)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1182 on the given reference triangle."""
    model = create_model('X_1182 = 2nd SARAGOSSA POINT OF X_19')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01182(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01182.json"))
    write_center_svg(
        model_acute,
        here / "x-01182.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
