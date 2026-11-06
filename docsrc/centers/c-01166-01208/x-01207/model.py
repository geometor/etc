"""GEOMETOR construction model for X_1207 = 3rd SARAGOSSA POINT OF X_83."""

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
    intersect_lines,
    promote_point_to_top,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_01207(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1207 = 3rd SARAGOSSA POINT OF X_83 on reference triangle ABC."""
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center"])
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center"])
    X_83 = eval_trilinear_point(model, A, B, C, 'b*c/(b**(2) + c**(2))', ID="X_83", classes=["center"])
    X_3978 = eval_barycentric_point(model, A, B, C, 'b**(2)*c**(2)*(a**(2) - b*c)*(a**(2) + b*c)', ID="X_3978", classes=["center"])
    central_line(model, X_3, X_6, 3, 6)
    central_line(model, X_83, X_3978, 83, 3978)
    X_1207 = intersect_lines(model, X_3, X_6, X_83, X_3978, ID="X_1207", classes=["selected", "target"])
    return promote_point_to_top(model, X_1207)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1207 on the given reference triangle."""
    model = create_model('X_1207 = 3rd SARAGOSSA POINT OF X_83')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01207(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01207.json"))
    write_center_svg(
        model_acute,
        here / "x-01207.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
