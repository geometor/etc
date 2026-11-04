"""GEOMETOR construction model for X_2260 = X_2-ISOCONJUGATE OF X_943."""

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
    promote_point_to_top,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_02260(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2260 = X_2-ISOCONJUGATE OF X_943 on reference triangle ABC."""
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center"])
    X_41 = eval_trilinear_point(model, A, B, C, 'a**(2)*(b + c - a)', ID="X_41", classes=["center"])
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center"])
    X_71 = eval_trilinear_point(model, A, B, C, '(b + c)*cos(A)', ID="X_71", classes=["center"])
    central_line(model, X_6, X_41, 6, 41)
    central_line(model, X_1, X_71, 1, 71)
    X_2260 = intersect_lines(model, X_6, X_41, X_1, X_71, ID="X_2260", classes=["selected", "target"])
    X_37 = eval_trilinear_point(model, A, B, C, 'b + c', ID="X_37", classes=["center", "incident"])
    X_38 = eval_trilinear_point(model, A, B, C, 'b**(2) + c**(2)', ID="X_38", classes=["center", "incident"])
    central_line(model, X_37, X_38, 37, 38, incident=True)
    return promote_point_to_top(model, X_2260)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2260 on the given reference triangle."""
    model = create_model('X_2260 = X_2-ISOCONJUGATE OF X_943')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02260(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02260.json"))
    write_center_svg(
        model_acute,
        here / "x-02260.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
