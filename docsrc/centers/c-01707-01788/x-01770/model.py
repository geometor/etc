"""GEOMETOR construction model for X_1770 = MIMOSA TRANSFORM OF X_943."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    cevapoint,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    gergonne_point_of,
    incenter_of,
    orthocenter_of,
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_01770(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1770 = MIMOSA TRANSFORM OF X_943 on reference triangle ABC."""
    X_46 = eval_trilinear_point(model, A, B, C, 'cos(B) + cos(C) - cos(A)', ID="X_46", classes=["center"])
    X_1717 = point_from_barycentrics(model, A, B, C, 0.12150372, 0.23633564, 0.64216064, ID="X_1717", classes=["center"])
    X_1770 = cevapoint(model, A, B, C, X_46, X_1717, ID="X_1770", classes=["selected", "target"])
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center", "incident"])
    X_7 = gergonne_point_of(model, A, B, C, ID="X_7", classes=["center", "incident"])
    central_line(model, X_1, X_7, 1, 7, incident=True)
    X_4 = orthocenter_of(model, A, B, C, ID="X_4", classes=["center", "incident"])
    central_line(model, X_4, X_46, 4, 46, incident=True)
    X_30 = eval_trilinear_point(model, A, B, C, 'cos(A) - 2*cos(B)*cos(C)', ID="X_30", classes=["center", "incident"])
    X_65 = eval_trilinear_point(model, A, B, C, 'cos(B) + cos(C)', ID="X_65", classes=["center", "incident"])
    central_line(model, X_30, X_65, 30, 65, incident=True)
    return promote_point_to_top(model, X_1770)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1770 on the given reference triangle."""
    model = create_model('X_1770 = MIMOSA TRANSFORM OF X_943')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01770(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01770.json"))
    write_center_svg(
        model_acute,
        here / "x-01770.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
