"""GEOMETOR construction model for X_2246 = X_2-ISOCONJUGATE OF X_840."""

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
    intersect_lines,
    mittenpunkt_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_02246(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2246 = X_2-ISOCONJUGATE OF X_840 on reference triangle ABC."""
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center"])
    X_41 = eval_trilinear_point(model, A, B, C, 'a**(2)*(b + c - a)', ID="X_41", classes=["center"])
    X_45 = eval_trilinear_point(model, A, B, C, '2*b + 2*c - a', ID="X_45", classes=["center"])
    X_55 = eval_trilinear_point(model, A, B, C, 'a*(b + c - a)', ID="X_55", classes=["center"])
    central_line(model, X_1, X_41, 1, 41)
    central_line(model, X_45, X_55, 45, 55)
    X_2246 = intersect_lines(model, X_1, X_41, X_45, X_55, ID="X_2246", classes=["selected", "target"])
    X_9 = mittenpunkt_of(model, A, B, C, ID="X_9", classes=["center", "incident"])
    X_100 = eval_trilinear_point(model, A, B, C, '1/(b - c)', ID="X_100", classes=["center", "incident"])
    central_line(model, X_9, X_100, 9, 100, incident=True)
    return promote_point_to_top(model, X_2246)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2246 on the given reference triangle."""
    model = create_model('X_2246 = X_2-ISOCONJUGATE OF X_840')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02246(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02246.json"))
    write_center_svg(
        model_acute,
        here / "x-02246.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
