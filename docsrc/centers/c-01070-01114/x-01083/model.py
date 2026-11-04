"""GEOMETOR construction model for X_1083 = MIDPOINT OF X_105 AND X_644."""

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
    incenter_of,
    midpoint,
    promote_point_to_top,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_01083(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1083 = MIDPOINT OF X_105 AND X_644 on reference triangle ABC."""
    X_105 = eval_trilinear_point(model, A, B, C, '1/(b**(2) + c**(2) - a*(b + c))', ID="X_105", classes=["center"])
    X_644 = eval_trilinear_point(model, A, B, C, '((b + c - a)/(b - c))', ID="X_644", classes=["center"])
    X_1083 = midpoint(model, X_105, X_644, ID="X_1083", classes=["selected", "target"], guide=False)
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center", "incident"])
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center", "incident"])
    central_line(model, X_1, X_6, 1, 6, incident=True)
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center", "incident"])
    X_667 = eval_trilinear_point(model, A, B, C, 'a**(2)*(b - c)', ID="X_667", classes=["center", "incident"])
    central_line(model, X_3, X_667, 3, 667, incident=True)
    central_line(model, X_105, X_644, 105, 644, incident=True)
    return promote_point_to_top(model, X_1083)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1083 on the given reference triangle."""
    model = create_model('X_1083 = MIDPOINT OF X_105 AND X_644')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01083(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01083.json"))
    write_center_svg(
        model_acute,
        here / "x-01083.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
