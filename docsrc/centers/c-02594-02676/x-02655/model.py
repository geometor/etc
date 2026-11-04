"""GEOMETOR construction model for X_2655 = CROSSDIFFERENCE OF PU(82)."""

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


def construct_x_02655(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2655 = CROSSDIFFERENCE OF PU(82) on reference triangle ABC."""
    X_2655 = eval_trilinear_point(model, A, B, C, '((sec(A) + sec(B))*(sec(A) + sec(C)) - (sec(B) + sec(C))**(2))', ID="X_2655", classes=["selected", "target"])
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center", "incident"])
    X_4 = orthocenter_of(model, A, B, C, ID="X_4", classes=["center", "incident"])
    central_line(model, X_1, X_4, 1, 4, incident=True)
    X_65 = eval_trilinear_point(model, A, B, C, 'cos(B) + cos(C)', ID="X_65", classes=["center", "incident"])
    X_1047 = point_from_barycentrics(model, A, B, C, 0.47678192, 0.53587009, -0.012652005, ID="X_1047", classes=["center", "incident"])
    central_line(model, X_65, X_1047, 65, 1047, incident=True)
    X_296 = eval_trilinear_point(model, A, B, C, '(cos(A))/((cos(A))**(2) - cos(B)*cos(C))', ID="X_296", classes=["center", "incident"])
    X_851 = eval_trilinear_point(model, A, B, C, 'sin(2*B)*sin(C - A) + sin(2*C)*sin(B - A)', ID="X_851", classes=["center", "incident"])
    central_line(model, X_296, X_851, 296, 851, incident=True)
    return promote_point_to_top(model, X_2655)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2655 on the given reference triangle."""
    model = create_model('X_2655 = CROSSDIFFERENCE OF PU(82)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02655(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02655.json"))
    write_center_svg(
        model_acute,
        here / "x-02655.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
