"""GEOMETOR construction model for X_1516 = ORTHOJOIN OF X_5."""

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
    orthocenter_of,
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_01516(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1516 = ORTHOJOIN OF X_5 on reference triangle ABC."""
    X_4 = orthocenter_of(model, A, B, C, ID="X_4", classes=["center"])
    X_96 = eval_trilinear_point(model, A, B, C, 'sec(2*A)*sec(B - C)', ID="X_96", classes=["center"])
    X_187 = eval_trilinear_point(model, A, B, C, 'a*(2*a**(2) - b**(2) - c**(2))', ID="X_187", classes=["center"])
    X_1514 = point_from_barycentrics(model, A, B, C, -0.40927419, -0.46693548, 1.8762097, ID="X_1514", classes=["center"])
    central_line(model, X_4, X_96, 4, 96)
    central_line(model, X_187, X_1514, 187, 1514)
    X_1516 = intersect_lines(model, X_4, X_96, X_187, X_1514, ID="X_1516", classes=["selected", "target"])
    return promote_point_to_top(model, X_1516)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1516 on the given reference triangle."""
    model = create_model('X_1516 = ORTHOJOIN OF X_5')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01516(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01516.json"))
    write_center_svg(
        model_acute,
        here / "x-01516.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
