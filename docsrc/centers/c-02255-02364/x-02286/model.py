"""GEOMETOR construction model for X_2286 = X_2-ISOCONJUGATE OF X_1039."""

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
    promote_point_to_top,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_02286(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2286 = X_2-ISOCONJUGATE OF X_1039 on reference triangle ABC."""
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center"])
    X_41 = eval_trilinear_point(model, A, B, C, 'a**(2)*(b + c - a)', ID="X_41", classes=["center"])
    X_63 = eval_trilinear_point(model, A, B, C, 'cot(A)', ID="X_63", classes=["center"])
    X_77 = eval_trilinear_point(model, A, B, C, '1/(1 + sec(A))', ID="X_77", classes=["center"])
    central_line(model, X_6, X_41, 6, 41)
    central_line(model, X_63, X_77, 63, 77)
    X_2286 = intersect_lines(model, X_6, X_41, X_63, X_77, ID="X_2286", classes=["selected", "target"])
    X_37 = eval_trilinear_point(model, A, B, C, 'b + c', ID="X_37", classes=["center", "incident"])
    X_478 = eval_trilinear_point(model, A, B, C, 'a*(a**(4) - 2*a*b*c*(b + c - a) - (b**(2) - c**(2))**(2))/(b + c - a)', ID="X_478", classes=["center", "incident"])
    central_line(model, X_37, X_478, 37, 478, incident=True)
    return promote_point_to_top(model, X_2286)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2286 on the given reference triangle."""
    model = create_model('X_2286 = X_2-ISOCONJUGATE OF X_1039')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02286(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02286.json"))
    write_center_svg(
        model_acute,
        here / "x-02286.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
