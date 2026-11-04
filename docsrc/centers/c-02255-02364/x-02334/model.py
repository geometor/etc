"""GEOMETOR construction model for X_2334 = X_2-ISOCONJUGATE OF X_1449."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    intersect_lines,
    nagel_point_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_02334(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2334 = X_2-ISOCONJUGATE OF X_1449 on reference triangle ABC."""
    X_8 = nagel_point_of(model, A, B, C, ID="X_8", classes=["center"])
    X_86 = eval_trilinear_point(model, A, B, C, 'b*c/(b + c)', ID="X_86", classes=["center"])
    X_42 = eval_trilinear_point(model, A, B, C, 'a*(b + c)', ID="X_42", classes=["center"])
    X_56 = eval_trilinear_point(model, A, B, C, 'a/(b + c - a)', ID="X_56", classes=["center"])
    central_line(model, X_8, X_86, 8, 86)
    central_line(model, X_42, X_56, 42, 56)
    X_2334 = intersect_lines(model, X_8, X_86, X_42, X_56, ID="X_2334", classes=["selected", "target"])
    X_55 = eval_trilinear_point(model, A, B, C, 'a*(b + c - a)', ID="X_55", classes=["center", "incident"])
    X_58 = eval_trilinear_point(model, A, B, C, 'a/(b + c)', ID="X_58", classes=["center", "incident"])
    central_line(model, X_55, X_58, 55, 58, incident=True)
    return promote_point_to_top(model, X_2334)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2334 on the given reference triangle."""
    model = create_model('X_2334 = X_2-ISOCONJUGATE OF X_1449')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02334(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02334.json"))
    write_center_svg(
        model_acute,
        here / "x-02334.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
