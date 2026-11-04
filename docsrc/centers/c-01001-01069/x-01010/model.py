"""GEOMETOR construction model for X_1010 = INTERCEPT OF EULER LINE AND LINE X_1X_75."""

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
    incenter_of,
    promote_point_to_top,
    spieker_center_of,
)
from geometor.etc.render import write_center_svg


def construct_x_01010(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1010 = INTERCEPT OF EULER LINE AND LINE X_1X_75 on reference triangle ABC."""
    X_1010 = eval_trilinear_point(model, A, B, C, '(b*c*(a**(2) + (b + c)**(2))/(b + c))', ID="X_1010", classes=["selected", "target"])
    X_2 = centroid_of(model, A, B, C, ID="X_2", classes=["center"])
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center"])
    central_line(model, X_2, X_3, 2, 3)
    X_10 = spieker_center_of(model, A, B, C, ID="X_10", classes=["center", "incident"])
    X_58 = eval_trilinear_point(model, A, B, C, 'a/(b + c)', ID="X_58", classes=["center", "incident"])
    central_line(model, X_10, X_58, 10, 58, incident=True)
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center", "incident"])
    X_75 = eval_trilinear_point(model, A, B, C, '1/a**(2)', ID="X_75", classes=["center", "incident"])
    central_line(model, X_1, X_75, 1, 75, incident=True)
    return promote_point_to_top(model, X_1010)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1010 on the given reference triangle."""
    model = create_model('X_1010 = INTERCEPT OF EULER LINE AND LINE X_1X_75')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01010(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01010.json"))
    write_center_svg(
        model_acute,
        here / "x-01010.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
