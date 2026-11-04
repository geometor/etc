"""GEOMETOR construction model for X_1210 = ISOGONAL CONJUGATE OF X_1167."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    centroid_of,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    feuerbach_point_of,
    incenter_of,
    isogonal_conjugate,
    orthocenter_of,
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_01210(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1210 = ISOGONAL CONJUGATE OF X_1167 on reference triangle ABC."""
    X_1167 = point_from_barycentrics(model, A, B, C, 0.35929716, 0.32223282, 0.31847002, ID="X_1167", classes=["center"])
    X_1210 = isogonal_conjugate(model, A, B, C, X_1167, ID="X_1210", classes=["selected", "target"])
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center", "incident"])
    X_2 = centroid_of(model, A, B, C, ID="X_2", classes=["center", "incident"])
    central_line(model, X_1, X_2, 1, 2, incident=True)
    X_4 = orthocenter_of(model, A, B, C, ID="X_4", classes=["center", "incident"])
    X_57 = eval_trilinear_point(model, A, B, C, '1/(b + c - a)', ID="X_57", classes=["center", "incident"])
    central_line(model, X_4, X_57, 4, 57, incident=True)
    X_11 = feuerbach_point_of(model, A, B, C, ID="X_11", classes=["center", "incident"])
    X_65 = eval_trilinear_point(model, A, B, C, 'cos(B) + cos(C)', ID="X_65", classes=["center", "incident"])
    central_line(model, X_11, X_65, 11, 65, incident=True)
    return promote_point_to_top(model, X_1210)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1210 on the given reference triangle."""
    model = create_model('X_1210 = ISOGONAL CONJUGATE OF X_1167')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01210(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01210.json"))
    write_center_svg(
        model_acute,
        here / "x-01210.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
