"""GEOMETOR construction model for X_2191 = X_2-ISOCONJUGATE OF X_218."""

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


def construct_x_02191(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2191 = X_2-ISOCONJUGATE OF X_218 on reference triangle ABC."""
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center"])
    X_142 = eval_trilinear_point(model, A, B, C, 'b + c - ((b - c)**(2))/a', ID="X_142", classes=["center"])
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center"])
    X_354 = eval_trilinear_point(model, A, B, C, '(b - c)**(2) - a*b - a*c', ID="X_354", classes=["center"])
    central_line(model, X_1, X_142, 1, 142)
    central_line(model, X_6, X_354, 6, 354)
    X_2191 = intersect_lines(model, X_1, X_142, X_6, X_354, ID="X_2191", classes=["selected", "target"])
    X_56 = eval_trilinear_point(model, A, B, C, 'a/(b + c - a)', ID="X_56", classes=["center", "incident"])
    X_1279 = eval_trilinear_point(model, A, B, C, '((b - c)**(2) - a*(b + c - 2*a))', ID="X_1279", classes=["center", "incident"])
    central_line(model, X_56, X_1279, 56, 1279, incident=True)
    return promote_point_to_top(model, X_2191)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2191 on the given reference triangle."""
    model = create_model('X_2191 = X_2-ISOCONJUGATE OF X_218')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02191(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02191.json"))
    write_center_svg(
        model_acute,
        here / "x-02191.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
