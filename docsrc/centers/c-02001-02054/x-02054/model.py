"""GEOMETOR construction model for X_2054 = X_2-ISOCONJUGATE OF X_1931."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    centroid_of,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_02054(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2054 = X_2-ISOCONJUGATE OF X_1931 on reference triangle ABC."""
    X_2054 = eval_trilinear_point(model, A, B, C, '(a*(b + c)/((b + c)**(2) - (a + b)*(a + c)))', ID="X_2054", classes=["selected", "target"])
    X_2 = centroid_of(model, A, B, C, ID="X_2", classes=["center", "incident"])
    X_846 = eval_trilinear_point(model, A, B, C, '(- a**(2) + b**(2) + c**(2) + b*c + c*a + a*b)', ID="X_846", classes=["center", "incident"])
    central_line(model, X_2, X_846, 2, 846, incident=True)
    X_111 = eval_trilinear_point(model, A, B, C, 'a/(2*a**(2) - b**(2) - c**(2))', ID="X_111", classes=["center", "incident"])
    X_902 = eval_trilinear_point(model, A, B, C, 'a*(b + c - 2*a)', ID="X_902", classes=["center", "incident"])
    central_line(model, X_111, X_902, 111, 902, incident=True)
    X_110 = eval_trilinear_point(model, A, B, C, 'csc(B - C)', ID="X_110", classes=["center", "incident"])
    X_1171 = eval_trilinear_point(model, A, B, C, 'a/((b + c)*(2*a + b + c))', ID="X_1171", classes=["center", "incident"])
    central_line(model, X_110, X_1171, 110, 1171, incident=True)
    return promote_point_to_top(model, X_2054)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2054 on the given reference triangle."""
    model = create_model('X_2054 = X_2-ISOCONJUGATE OF X_1931')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02054(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02054.json"))
    write_center_svg(
        model_acute,
        here / "x-02054.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
