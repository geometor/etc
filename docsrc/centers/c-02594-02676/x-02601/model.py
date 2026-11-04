"""GEOMETOR construction model for X_2601 = CROSSSUM OF PU(69)."""

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
    nine_point_center_of,
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_02601(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2601 = CROSSSUM OF PU(69) on reference triangle ABC."""
    X_2601 = eval_trilinear_point(model, A, B, C, 'sec(A - B)*sec(A - C) + (sec(B - C))**(2)', ID="X_2601", classes=["selected", "target"])
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center", "incident"])
    X_2120 = point_from_barycentrics(model, A, B, C, 0.30475192, 0.22664215, 0.46860594, ID="X_2120", classes=["center", "incident"])
    central_line(model, X_1, X_2120, 1, 2120, incident=True)
    X_5 = nine_point_center_of(model, A, B, C, ID="X_5", classes=["center", "incident"])
    X_2602 = eval_trilinear_point(model, A, B, C, 'sec(A - B)*sec(A - C) - (sec(B - C))**(2)', ID="X_2602", classes=["center", "incident"])
    central_line(model, X_5, X_2602, 5, 2602, incident=True)
    X_2594 = eval_trilinear_point(model, A, B, C, '(cos(C- A) + cos(B - A))', ID="X_2594", classes=["center", "incident"])
    X_2603 = eval_trilinear_point(model, A, B, C, '(1/(sec(A - B)*sec(A - C) - (sec(B - C))**(2)))', ID="X_2603", classes=["center", "incident"])
    central_line(model, X_2594, X_2603, 2594, 2603, incident=True)
    return promote_point_to_top(model, X_2601)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2601 on the given reference triangle."""
    model = create_model('X_2601 = CROSSSUM OF PU(69)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02601(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02601.json"))
    write_center_svg(
        model_acute,
        here / "x-02601.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
