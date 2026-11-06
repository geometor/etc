"""GEOMETOR construction model for X_3048 = INTERSECTION X_110X_126∩X_111X_184."""

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


def construct_x_03048(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3048 = INTERSECTION X_110X_126∩X_111X_184 on reference triangle ABC."""
    X_3048 = eval_trilinear_point(model, A, B, C, '(a**(3)*(a**(4) + b**(4) - c**(4) - 4*a**(2)*b**(2) + 3*b**(2)*c**(2))*(a**(4) - b**(4) + c**(4) - 4*a**(2)*c**(2) + 3*b**(2)*c**(2)))', ID="X_3048", classes=["selected", "target"])
    X_110 = eval_trilinear_point(model, A, B, C, 'csc(B - C)', ID="X_110", classes=["center", "incident"])
    X_126 = eval_trilinear_point(model, A, B, C, '(b*c*(2*a**(2) - b**(2) - c**(2))*(b**(4) + c**(4) + a**(2)*(b**(2) + c**(2)) - 4*b**(2)*c**(2)))', ID="X_126", classes=["center", "incident"])
    central_line(model, X_110, X_126, 110, 126, incident=True)
    X_111 = eval_trilinear_point(model, A, B, C, 'a/(2*a**(2) - b**(2) - c**(2))', ID="X_111", classes=["center", "incident"])
    X_184 = eval_trilinear_point(model, A, B, C, 'a**(2)*cos(A)', ID="X_184", classes=["center", "incident"])
    central_line(model, X_111, X_184, 111, 184, incident=True)
    X_1147 = eval_trilinear_point(model, A, B, C, '(sin(4*A))/sin(A)', ID="X_1147", classes=["center", "incident"])
    X_1296 = eval_barycentric_point(model, A, B, C, 'a**(2)/((b**(2) - c**(2))*(5*a**(2) - b**(2) - c**(2)))', ID="X_1296", classes=["center", "incident"])
    central_line(model, X_1147, X_1296, 1147, 1296, incident=True)
    return promote_point_to_top(model, X_3048)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3048 on the given reference triangle."""
    model = create_model('X_3048 = INTERSECTION X_110X_126∩X_111X_184')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03048(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03048.json"))
    write_center_svg(
        model_acute,
        here / "x-03048.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
