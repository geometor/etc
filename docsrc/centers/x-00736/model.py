"""GEOMETOR construction model for X(736) = EVEN (- 2, 4) INFINITY POINT."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_barycentric_point,
    eval_trilinear_point,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00736(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(736) = EVEN (- 2, 4) INFINITY POINT on reference triangle ABC."""
    X_736 = eval_barycentric_point(model, A, B, C, 'a**(6)*(b**(2) + c**(2)) - b**(2)*c**(2)*(b**(4) + c**(4))', ID="X(736)", classes=["selected", "target"])
    X_32 = eval_trilinear_point(model, A, B, C, 'a**(3)', ID="X(32)", classes=["center", "incident"])
    X_76 = eval_trilinear_point(model, A, B, C, '1/a**(3)', ID="X(76)", classes=["center", "incident"])
    central_line(model, X_32, X_76, 32, 76, incident=True)
    X_39 = eval_trilinear_point(model, A, B, C, 'a*(b**(2) + c**(2))', ID="X(39)", classes=["center", "incident"])
    X_325 = eval_trilinear_point(model, A, B, C, 'b*c*(b**(4) + c**(4) - a**(2)*b**(2) - a**(2)*c**(2))', ID="X(325)", classes=["center", "incident"])
    central_line(model, X_39, X_325, 39, 325, incident=True)
    X_194 = eval_trilinear_point(model, A, B, C, 'b*c*(a**(2)*b**(2) + a**(2)*c**(2) - b**(2)*c**(2))', ID="X(194)", classes=["center", "incident"])
    X_315 = eval_trilinear_point(model, A, B, C, 'b*c*(b**(4) + c**(4) - a**(4))', ID="X(315)", classes=["center", "incident"])
    central_line(model, X_194, X_315, 194, 315, incident=True)
    return promote_point_to_top(model, X_736)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(736) on the given reference triangle."""
    model = create_model('X(736) = EVEN (- 2, 4) INFINITY POINT')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00736(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00736.json"))
    write_center_svg(
        model_acute,
        here / "x-00736.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
