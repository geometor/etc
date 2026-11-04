"""GEOMETOR construction model for X_1324 = CIRCUMCIRCLE-INVERSE OF X_10."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    circumcenter_of,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    promote_point_to_top,
    spieker_center_of,
)
from geometor.etc.render import write_center_svg


def construct_x_01324(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1324 = CIRCUMCIRCLE-INVERSE OF X_10 on reference triangle ABC."""
    X_1324 = eval_trilinear_point(model, A, B, C, '(a*(a**(5) - b**(5) - c**(5) + a**(3)*b*c - b**(3)*c*a - c**(3)*a*b + a**(2)*b**(2)*(b - a) + a**(2)*c**(2)*(c - a) + b**(2)*c**(2)*(b + c)))', ID="X_1324", classes=["selected", "target"])
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center", "incident"])
    X_10 = spieker_center_of(model, A, B, C, ID="X_10", classes=["center", "incident"])
    central_line(model, X_3, X_10, 3, 10, incident=True)
    X_58 = eval_trilinear_point(model, A, B, C, 'a/(b + c)', ID="X_58", classes=["center", "incident"])
    X_181 = eval_trilinear_point(model, A, B, C, 'a*(b + c)**(2)/(b + c - a)', ID="X_181", classes=["center", "incident"])
    central_line(model, X_58, X_181, 58, 181, incident=True)
    X_35 = eval_trilinear_point(model, A, B, C, '1 + 2*cos(A)', ID="X_35", classes=["center", "incident"])
    X_228 = eval_trilinear_point(model, A, B, C, '(sin(2*A))*(sin(B) + sin(C))', ID="X_228", classes=["center", "incident"])
    central_line(model, X_35, X_228, 35, 228, incident=True)
    return promote_point_to_top(model, X_1324)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1324 on the given reference triangle."""
    model = create_model('X_1324 = CIRCUMCIRCLE-INVERSE OF X_10')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01324(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01324.json"))
    write_center_svg(
        model_acute,
        here / "x-01324.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
