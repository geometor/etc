"""GEOMETOR construction model for X(669) = CROSSDIFFERENCE OF X(2) AND X(39)."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00669(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(669) = CROSSDIFFERENCE OF X(2) AND X(39) on reference triangle ABC."""
    X_669 = eval_trilinear_point(model, A, B, C, 'a**(3)*(b**(2) - c**(2))', ID="X(669)", classes=["selected", "target"])
    X_23 = eval_trilinear_point(model, A, B, C, 'a*(b**(4) + c**(4) - a**(4) - b**(2)*c**(2))', ID="X(23)", classes=["center", "incident"])
    X_385 = eval_trilinear_point(model, A, B, C, 'b*c*(a**(4) - b**(2)*c**(2))', ID="X(385)", classes=["center", "incident"])
    central_line(model, X_23, X_385, 23, 385, incident=True)
    X_187 = eval_trilinear_point(model, A, B, C, 'a*(2*a**(2) - b**(2) - c**(2))', ID="X(187)", classes=["center", "incident"])
    X_237 = eval_trilinear_point(model, A, B, C, 'a**(2)*cos(A + omega )', ID="X(237)", classes=["center", "incident"])
    central_line(model, X_187, X_237, 187, 237, incident=True)
    X_25 = eval_trilinear_point(model, A, B, C, 'sin(A)*tan(A)', ID="X(25)", classes=["center", "incident"])
    X_878 = point_from_barycentrics(model, A, B, C, -0.14706477, 1.0752646, 0.071800149, ID="X(878)", classes=["center", "incident"])
    central_line(model, X_25, X_878, 25, 878, incident=True)
    return promote_point_to_top(model, X_669)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(669) on the given reference triangle."""
    model = create_model('X(669) = CROSSDIFFERENCE OF X(2) AND X(39)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00669(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00669.json"))
    write_center_svg(
        model_acute,
        here / "x-00669.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
