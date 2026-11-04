"""GEOMETOR construction model for X_1709 = MIMOSA TRANSFORM OF X_9."""

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
    incenter_of,
    orthocenter_of,
    point_from_barycentrics,
    promote_point_to_top,
    reflection_in_point,
)
from geometor.etc.render import write_center_svg


def construct_x_01709(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1709 = MIMOSA TRANSFORM OF X_9 on reference triangle ABC."""
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center"])
    X_1012 = point_from_barycentrics(model, A, B, C, 0.22671569, 0.26715686, 0.50612745, ID="X_1012", classes=["center"])
    X_1709 = reflection_in_point(model, X_1, X_1012, ID="X_1709", classes=["selected", "target"], guide=False)
    X_4 = orthocenter_of(model, A, B, C, ID="X_4", classes=["center", "incident"])
    X_46 = eval_trilinear_point(model, A, B, C, 'cos(B) + cos(C) - cos(A)', ID="X_46", classes=["center", "incident"])
    central_line(model, X_4, X_46, 4, 46, incident=True)
    X_11 = feuerbach_point_of(model, A, B, C, ID="X_11", classes=["center", "incident"])
    X_57 = eval_trilinear_point(model, A, B, C, '1/(b + c - a)', ID="X_57", classes=["center", "incident"])
    central_line(model, X_11, X_57, 11, 57, incident=True)
    X_30 = eval_trilinear_point(model, A, B, C, 'cos(A) - 2*cos(B)*cos(C)', ID="X_30", classes=["center", "incident"])
    X_40 = eval_trilinear_point(model, A, B, C, 'cos(B) + cos(C) - cos(A) - 1', ID="X_40", classes=["center", "incident"])
    central_line(model, X_30, X_40, 30, 40, incident=True)
    return promote_point_to_top(model, X_1709)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1709 on the given reference triangle."""
    model = create_model('X_1709 = MIMOSA TRANSFORM OF X_9')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01709(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01709.json"))
    write_center_svg(
        model_acute,
        here / "x-01709.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
