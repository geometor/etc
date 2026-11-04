"""GEOMETOR construction model for X_1846 = ZOSMA TRANSFORM OF X_104."""

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
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_01846(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1846 = ZOSMA TRANSFORM OF X_104 on reference triangle ABC."""
    X_4 = orthocenter_of(model, A, B, C, ID="X_4", classes=["center"])
    X_11 = feuerbach_point_of(model, A, B, C, ID="X_11", classes=["center"])
    X_19 = eval_trilinear_point(model, A, B, C, 'tan(A)', ID="X_19", classes=["center"])
    X_53 = eval_trilinear_point(model, A, B, C, 'tan(A)*cos(B - C)', ID="X_53", classes=["center"])
    central_line(model, X_4, X_11, 4, 11)
    central_line(model, X_19, X_53, 19, 53)
    X_1846 = intersect_lines(model, X_4, X_11, X_19, X_53, ID="X_1846", classes=["selected", "target"])
    X_517 = eval_trilinear_point(model, A, B, C, '-1 + cos(B) + cos(C)', ID="X_517", classes=["center", "incident"])
    X_1361 = point_from_barycentrics(model, A, B, C, 0.19480519, 0.041558442, 0.76363636, ID="X_1361", classes=["center", "incident"])
    central_line(model, X_517, X_1361, 517, 1361, incident=True)
    return promote_point_to_top(model, X_1846)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1846 on the given reference triangle."""
    model = create_model('X_1846 = ZOSMA TRANSFORM OF X_104')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01846(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01846.json"))
    write_center_svg(
        model_acute,
        here / "x-01846.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
