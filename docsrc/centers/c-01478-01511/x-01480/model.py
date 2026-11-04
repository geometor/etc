"""GEOMETOR construction model for X_1480 = 1st SHADOW POINT."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    ceva_conjugate,
    circumcenter_of,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    incenter_of,
    point_from_barycentrics,
    promote_point_to_top,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_01480(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1480 = 1st SHADOW POINT on reference triangle ABC."""
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center"])
    X_999 = eval_trilinear_point(model, A, B, C, '2 - cos(A)', ID="X_999", classes=["center"])
    X_1480 = ceva_conjugate(model, A, B, C, X_1, X_999, ID="X_1480", classes=["selected", "target"])
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center", "incident"])
    X_517 = eval_trilinear_point(model, A, B, C, '-1 + cos(B) + cos(C)', ID="X_517", classes=["center", "incident"])
    central_line(model, X_6, X_517, 6, 517, incident=True)
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center", "incident"])
    X_902 = eval_trilinear_point(model, A, B, C, 'a*(b + c - 2*a)', ID="X_902", classes=["center", "incident"])
    central_line(model, X_3, X_902, 3, 902, incident=True)
    X_1406 = point_from_barycentrics(model, A, B, C, 0.0058479532, 0.14596491, 0.84818713, ID="X_1406", classes=["center", "incident"])
    central_line(model, X_1, X_1406, 1, 1406, incident=True)
    return promote_point_to_top(model, X_1480)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1480 on the given reference triangle."""
    model = create_model('X_1480 = 1st SHADOW POINT')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01480(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01480.json"))
    write_center_svg(
        model_acute,
        here / "x-01480.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
