"""GEOMETOR construction model for X_1737 = MIMOSA TRANSFORM OF X_104."""

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
    incenter_of,
    midpoint,
    nine_point_center_of,
    orthocenter_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_01737(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1737 = MIMOSA TRANSFORM OF X_104 on reference triangle ABC."""
    X_36 = eval_trilinear_point(model, A, B, C, '1 - 2*cos(A)', ID="X_36", classes=["center"])
    X_80 = eval_trilinear_point(model, A, B, C, '1/(1 - 2*cos(A))', ID="X_80", classes=["center"])
    X_1737 = midpoint(model, X_36, X_80, ID="X_1737", classes=["selected", "target"], guide=False)
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center", "incident"])
    X_2 = centroid_of(model, A, B, C, ID="X_2", classes=["center", "incident"])
    central_line(model, X_1, X_2, 1, 2, incident=True)
    X_4 = orthocenter_of(model, A, B, C, ID="X_4", classes=["center", "incident"])
    X_46 = eval_trilinear_point(model, A, B, C, 'cos(B) + cos(C) - cos(A)', ID="X_46", classes=["center", "incident"])
    central_line(model, X_4, X_46, 4, 46, incident=True)
    X_5 = nine_point_center_of(model, A, B, C, ID="X_5", classes=["center", "incident"])
    X_65 = eval_trilinear_point(model, A, B, C, 'cos(B) + cos(C)', ID="X_65", classes=["center", "incident"])
    central_line(model, X_5, X_65, 5, 65, incident=True)
    return promote_point_to_top(model, X_1737)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1737 on the given reference triangle."""
    model = create_model('X_1737 = MIMOSA TRANSFORM OF X_104')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01737(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01737.json"))
    write_center_svg(
        model_acute,
        here / "x-01737.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
