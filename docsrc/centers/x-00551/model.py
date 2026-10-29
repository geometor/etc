"""GEOMETOR construction model for X(551) = MIDPOINT OF X(1) AND X(2)."""

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
    incenter_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00551(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(551) = MIDPOINT OF X(1) AND X(2) on reference triangle ABC."""
    X_551 = eval_trilinear_point(model, A, B, C, '(4*a + b + c)/a', ID="X(551)", classes=["selected", "target"])
    X_1 = incenter_of(model, A, B, C, ID="X(1)", classes=["center", "incident"])
    X_2 = centroid_of(model, A, B, C, ID="X(2)", classes=["center", "incident"])
    central_line(model, X_1, X_2, 1, 2, incident=True)
    X_86 = eval_trilinear_point(model, A, B, C, 'b*c/(b + c)', ID="X(86)", classes=["center", "incident"])
    X_99 = eval_trilinear_point(model, A, B, C, 'b*c/(b**(2) - c**(2))', ID="X(99)", classes=["center", "incident"])
    central_line(model, X_86, X_99, 86, 99, incident=True)
    X_142 = eval_trilinear_point(model, A, B, C, 'b + c - ((b - c)**(2))/a', ID="X(142)", classes=["center", "incident"])
    X_214 = eval_trilinear_point(model, A, B, C, '(b + c - 2*a)*(b**(2) + c**(2) - a**(2) - b*c)', ID="X(214)", classes=["center", "incident"])
    central_line(model, X_142, X_214, 142, 214, incident=True)
    return promote_point_to_top(model, X_551)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(551) on the given reference triangle."""
    model = create_model('X(551) = MIDPOINT OF X(1) AND X(2)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00551(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00551.json"))
    write_center_svg(
        model_acute,
        here / "x-00551.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
