"""GEOMETOR construction model for X_991 = INTERSECTION OF LINES X_1X_7 AND X_3X_6."""

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
    gergonne_point_of,
    incenter_of,
    promote_point_to_top,
    reflection_in_point,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_00991(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_991 = INTERSECTION OF LINES X_1X_7 AND X_3X_6 on reference triangle ABC."""
    X_573 = eval_trilinear_point(model, A, B, C, 'cos(A + U)', ID="X_573", classes=["center"])
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center"])
    X_991 = reflection_in_point(model, X_573, X_3, ID="X_991", classes=["selected", "target"], guide=False)
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center", "incident"])
    X_7 = gergonne_point_of(model, A, B, C, ID="X_7", classes=["center", "incident"])
    central_line(model, X_1, X_7, 1, 7, incident=True)
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center", "incident"])
    central_line(model, X_3, X_6, 3, 6, incident=True)
    X_55 = eval_trilinear_point(model, A, B, C, 'a*(b + c - a)', ID="X_55", classes=["center", "incident"])
    X_103 = eval_trilinear_point(model, A, B, C, 'a/((a - b)*cot(C) + (a - c)*cot(B))', ID="X_103", classes=["center", "incident"])
    central_line(model, X_55, X_103, 55, 103, incident=True)
    return promote_point_to_top(model, X_991)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_991 on the given reference triangle."""
    model = create_model('X_991 = INTERSECTION OF LINES X_1X_7 AND X_3X_6')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00991(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00991.json"))
    write_center_svg(
        model_acute,
        here / "x-00991.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
