"""GEOMETOR construction model for X_2853 = ISOGONAL CONJUGATE OF X_2769."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    isogonal_conjugate,
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_02853(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2853 = ISOGONAL CONJUGATE OF X_2769 on reference triangle ABC."""
    X_2769 = point_from_barycentrics(model, A, B, C, -0.088240128, 0.15600913, 0.932231, ID="X_2769", classes=["center"])
    X_2853 = isogonal_conjugate(model, A, B, C, X_2769, ID="X_2853", classes=["selected", "target"])
    X_109 = eval_trilinear_point(model, A, B, C, 'a/(cos(B) - cos(C))', ID="X_109", classes=["center", "incident"])
    X_112 = eval_trilinear_point(model, A, B, C, 'a/(sin(2*B) - sin(2*C))', ID="X_112", classes=["center", "incident"])
    central_line(model, X_109, X_112, 109, 112, incident=True)
    X_117 = point_from_barycentrics(model, A, B, C, 0.19223485, -0.017045455, 0.82481061, ID="X_117", classes=["center", "incident"])
    X_132 = point_from_barycentrics(model, A, B, C, 0.11002416, 0.049913231, 0.84006261, ID="X_132", classes=["center", "incident"])
    central_line(model, X_117, X_132, 117, 132, incident=True)
    X_124 = eval_trilinear_point(model, A, B, C, '(b*c*(b + c - a)*(b - c)**(2)*((b + c)*(b**(2) + c**(2) - a**(2) - b*c) + a*b*c))', ID="X_124", classes=["center", "incident"])
    X_127 = eval_trilinear_point(model, A, B, C, 'b*c*(sin(2*B) - sin(2*C))*((b**(2) - c**(2))*sin(2*A) - b**(2)*sin(2*B) + c**(2)*sin(2*C))', ID="X_127", classes=["center", "incident"])
    central_line(model, X_124, X_127, 124, 127, incident=True)
    return promote_point_to_top(model, X_2853)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2853 on the given reference triangle."""
    model = create_model('X_2853 = ISOGONAL CONJUGATE OF X_2769')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02853(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02853.json"))
    write_center_svg(
        model_acute,
        here / "x-02853.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
