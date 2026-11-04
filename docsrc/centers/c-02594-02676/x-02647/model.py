"""GEOMETOR construction model for X_2647 = CROSSSUM OF PU(80)."""

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
    orthocenter_of,
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_02647(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2647 = CROSSSUM OF PU(80) on reference triangle ABC."""
    X_2647 = eval_trilinear_point(model, A, B, C, '((cos(A) + cos(B))*(cos(A) + cos(C)) +(cos(B) + cos(C))**(2))', ID="X_2647", classes=["selected", "target"])
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center", "incident"])
    X_4 = orthocenter_of(model, A, B, C, ID="X_4", classes=["center", "incident"])
    central_line(model, X_1, X_4, 1, 4, incident=True)
    X_65 = eval_trilinear_point(model, A, B, C, 'cos(B) + cos(C)', ID="X_65", classes=["center", "incident"])
    X_1046 = point_from_barycentrics(model, A, B, C, 0.13236391, 0.3064877, 0.5611484, ID="X_1046", classes=["center", "incident"])
    central_line(model, X_65, X_1046, 65, 1046, incident=True)
    X_21 = eval_trilinear_point(model, A, B, C, '1/(cos(B) + cos(C))', ID="X_21", classes=["center", "incident"])
    X_1254 = point_from_barycentrics(model, A, B, C, 0.14647253, 0.26625065, 0.58727682, ID="X_1254", classes=["center", "incident"])
    central_line(model, X_21, X_1254, 21, 1254, incident=True)
    return promote_point_to_top(model, X_2647)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2647 on the given reference triangle."""
    model = create_model('X_2647 = CROSSSUM OF PU(80)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02647(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02647.json"))
    write_center_svg(
        model_acute,
        here / "x-02647.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
