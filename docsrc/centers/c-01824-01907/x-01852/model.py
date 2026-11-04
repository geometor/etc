"""GEOMETOR construction model for X_1852 = ZOSMA TRANSFORM OF X_201."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    feuerbach_point_of,
    intersect_lines,
    orthocenter_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_01852(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1852 = ZOSMA TRANSFORM OF X_201 on reference triangle ABC."""
    X_4 = orthocenter_of(model, A, B, C, ID="X_4", classes=["center"])
    X_12 = eval_trilinear_point(model, A, B, C, '1 + cos(B - C)', ID="X_12", classes=["center"])
    X_11 = feuerbach_point_of(model, A, B, C, ID="X_11", classes=["center"])
    X_28 = eval_trilinear_point(model, A, B, C, '(tan(A))/(b + c)', ID="X_28", classes=["center"])
    central_line(model, X_4, X_12, 4, 12)
    central_line(model, X_11, X_28, 11, 28)
    X_1852 = intersect_lines(model, X_4, X_12, X_11, X_28, ID="X_1852", classes=["selected", "target"])
    X_19 = eval_trilinear_point(model, A, B, C, 'tan(A)', ID="X_19", classes=["center", "incident"])
    X_1837 = eval_trilinear_point(model, A, B, C, 'cos(B) + cos(C) - 2*cos(B)*cos(C)', ID="X_1837", classes=["center", "incident"])
    central_line(model, X_19, X_1837, 19, 1837, incident=True)
    return promote_point_to_top(model, X_1852)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1852 on the given reference triangle."""
    model = create_model('X_1852 = ZOSMA TRANSFORM OF X_201')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01852(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01852.json"))
    write_center_svg(
        model_acute,
        here / "x-01852.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
