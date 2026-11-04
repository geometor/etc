"""GEOMETOR construction model for X_1172 = 1st SARAGOSSA POINT OF X_48."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    gergonne_point_of,
    incenter_of,
    intersect_lines,
    orthocenter_of,
    promote_point_to_top,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_01172(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1172 = 1st SARAGOSSA POINT OF X_48 on reference triangle ABC."""
    X_4 = orthocenter_of(model, A, B, C, ID="X_4", classes=["center"])
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center"])
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center"])
    X_19 = eval_trilinear_point(model, A, B, C, 'tan(A)', ID="X_19", classes=["center"])
    central_line(model, X_4, X_6, 4, 6)
    central_line(model, X_1, X_19, 1, 19)
    X_1172 = intersect_lines(model, X_4, X_6, X_1, X_19, ID="X_1172", classes=["selected", "target"])
    X_7 = gergonne_point_of(model, A, B, C, ID="X_7", classes=["center", "incident"])
    X_27 = eval_trilinear_point(model, A, B, C, '(sec(A))/(b + c)', ID="X_27", classes=["center", "incident"])
    central_line(model, X_7, X_27, 7, 27, incident=True)
    return promote_point_to_top(model, X_1172)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1172 on the given reference triangle."""
    model = create_model('X_1172 = 1st SARAGOSSA POINT OF X_48')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01172(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01172.json"))
    write_center_svg(
        model_acute,
        here / "x-01172.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
