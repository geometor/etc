"""GEOMETOR construction model for X_2395 = GIBERT-SIMSON TRANSFORM OF X_98."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    centroid_of,
    construct_baseline_triangle,
    create_model,
    eval_barycentric_point,
    eval_trilinear_point,
    promote_point_to_top,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_02395(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2395 = GIBERT-SIMSON TRANSFORM OF X_98 on reference triangle ABC."""
    X_2395 = eval_barycentric_point(model, A, B, C, '(b**(2) - c**(2))/(b**(4) + c**(4) - a**(2)*b**(2) - a**(2)*c**(2))', ID="X_2395", classes=["selected", "target"])
    X_98 = eval_trilinear_point(model, A, B, C, 'sec(A +  omega  )', ID="X_98", classes=["center", "incident"])
    X_111 = eval_trilinear_point(model, A, B, C, 'a/(2*a**(2) - b**(2) - c**(2))', ID="X_111", classes=["center", "incident"])
    central_line(model, X_98, X_111, 98, 111, incident=True)
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center", "incident"])
    X_523 = eval_trilinear_point(model, A, B, C, 'sin(B -C)', ID="X_523", classes=["center", "incident"])
    central_line(model, X_6, X_523, 6, 523, incident=True)
    X_2 = centroid_of(model, A, B, C, ID="X_2", classes=["center", "incident"])
    X_647 = eval_trilinear_point(model, A, B, C, 'a*(b**(2) - c**(2))*(b**(2) + c**(2) - a**(2))', ID="X_647", classes=["center", "incident"])
    central_line(model, X_2, X_647, 2, 647, incident=True)
    return promote_point_to_top(model, X_2395)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2395 on the given reference triangle."""
    model = create_model('X_2395 = GIBERT-SIMSON TRANSFORM OF X_98')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02395(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02395.json"))
    write_center_svg(
        model_acute,
        here / "x-02395.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
