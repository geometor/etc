"""GEOMETOR construction model for X_2120 = EIGENTRANSFORM OF X_5."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    incenter_of,
    intersect_lines,
    nine_point_center_of,
    orthocenter_of,
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_02120(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2120 = EIGENTRANSFORM OF X_5 on reference triangle ABC."""
    X_4 = orthocenter_of(model, A, B, C, ID="X_4", classes=["center"])
    X_1157 = eval_trilinear_point(model, A, B, C, '4*cos(A) + cos(3*A)*sec(A)*sec(B - C)', ID="X_1157", classes=["center"])
    X_5 = nine_point_center_of(model, A, B, C, ID="X_5", classes=["center"])
    X_2121 = point_from_barycentrics(model, A, B, C, 0.23747658, 0.45982126, 0.30270216, ID="X_2121", classes=["center"])
    central_line(model, X_4, X_1157, 4, 1157)
    central_line(model, X_5, X_2121, 5, 2121)
    X_2120 = intersect_lines(model, X_4, X_1157, X_5, X_2121, ID="X_2120", classes=["selected", "target"])
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center", "incident"])
    X_3461 = point_from_barycentrics(model, A, B, C, 0.25970945, 0.40479923, 0.33549132, ID="X_3461", classes=["center", "incident"])
    central_line(model, X_1, X_3461, 1, 3461, incident=True)
    return promote_point_to_top(model, X_2120)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2120 on the given reference triangle."""
    model = create_model('X_2120 = EIGENTRANSFORM OF X_5')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02120(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02120.json"))
    write_center_svg(
        model_acute,
        here / "x-02120.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
