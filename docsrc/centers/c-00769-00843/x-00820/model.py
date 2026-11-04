"""GEOMETOR construction model for X_820 = CROSSPOINT OF X_1 AND X_255."""

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
    incenter_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00820(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_820 = CROSSPOINT OF X_1 AND X_255 on reference triangle ABC."""
    X_820 = eval_trilinear_point(model, A, B, C, '((cos(A))**(2)*((cos(B))**(2) + (cos(C))**(2)))', ID="X_820", classes=["selected", "target"])
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center", "incident"])
    X_29 = eval_trilinear_point(model, A, B, C, '(sec(A))/(cos(B) + cos(C))', ID="X_29", classes=["center", "incident"])
    central_line(model, X_1, X_29, 1, 29, incident=True)
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center", "incident"])
    X_296 = eval_trilinear_point(model, A, B, C, '(cos(A))/((cos(A))**(2) - cos(B)*cos(C))', ID="X_296", classes=["center", "incident"])
    central_line(model, X_3, X_296, 3, 296, incident=True)
    X_662 = eval_trilinear_point(model, A, B, C, '1/(cot(B) - cot(C))', ID="X_662", classes=["center", "incident"])
    X_775 = eval_trilinear_point(model, A, B, C, '(1/((cos(B))**(2) + (cos(C))**(2)))', ID="X_775", classes=["center", "incident"])
    central_line(model, X_662, X_775, 662, 775, incident=True)
    return promote_point_to_top(model, X_820)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_820 on the given reference triangle."""
    model = create_model('X_820 = CROSSPOINT OF X_1 AND X_255')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00820(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00820.json"))
    write_center_svg(
        model_acute,
        here / "x-00820.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
