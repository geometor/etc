"""GEOMETOR construction model for X_2960 = EXCENTRAL-ISOGONAL CONJUGATE OF X_155."""

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
    point_from_barycentrics,
    promote_point_to_top,
    reflection_in_point,
)
from geometor.etc.render import write_center_svg


def construct_x_02960(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2960 = EXCENTRAL-ISOGONAL CONJUGATE OF X_155 on reference triangle ABC."""
    X_1717 = point_from_barycentrics(model, A, B, C, 0.12150372, 0.23633564, 0.64216064, ID="X_1717", classes=["center"])
    X_2915 = point_from_barycentrics(model, A, B, C, 0.60495253, 0.50192456, -0.10687708, ID="X_2915", classes=["center"])
    X_2960 = reflection_in_point(model, X_1717, X_2915, ID="X_2960", classes=["selected", "target"], guide=False)
    X_30 = eval_trilinear_point(model, A, B, C, 'cos(A) - 2*cos(B)*cos(C)', ID="X_30", classes=["center", "incident"])
    X_40 = eval_trilinear_point(model, A, B, C, 'cos(B) + cos(C) - cos(A) - 1', ID="X_40", classes=["center", "incident"])
    central_line(model, X_30, X_40, 30, 40, incident=True)
    X_35 = eval_trilinear_point(model, A, B, C, '1 + 2*cos(A)', ID="X_35", classes=["center", "incident"])
    X_37 = eval_trilinear_point(model, A, B, C, 'b + c', ID="X_37", classes=["center", "incident"])
    central_line(model, X_35, X_37, 35, 37, incident=True)
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center", "incident"])
    X_1719 = point_from_barycentrics(model, A, B, C, 0.054068409, 0.21351179, 0.7324198, ID="X_1719", classes=["center", "incident"])
    central_line(model, X_1, X_1719, 1, 1719, incident=True)
    return promote_point_to_top(model, X_2960)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2960 on the given reference triangle."""
    model = create_model('X_2960 = EXCENTRAL-ISOGONAL CONJUGATE OF X_155')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02960(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02960.json"))
    write_center_svg(
        model_acute,
        here / "x-02960.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
