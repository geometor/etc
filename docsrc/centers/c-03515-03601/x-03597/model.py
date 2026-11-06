"""GEOMETOR construction model for X_3597 = 2nd ODEHNAL POINT."""

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
    orthocenter_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_03597(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3597 = 2nd ODEHNAL POINT on reference triangle ABC."""
    X_3597 = eval_trilinear_point(model, A, B, C, '(b*c/(a**(5) + a**(4)*(b + c) - a**(3)*(b - c)**(2) - a**(2)*(b + c)*(b**(2) + c**(2)) - 2*a*b*c*(b**(2) + b*c + c**(2)) - 2*b**(2)*c**(2)*(b + c)))', ID="X_3597", classes=["selected", "target"])
    X_2 = centroid_of(model, A, B, C, ID="X_2", classes=["center", "incident"])
    X_970 = eval_trilinear_point(model, A, B, C, 'a*(a**(3)*(b + c)**(2) + a*(a*b + a*c - 2*b*c)*(b**(2) + c**(2)) - b*c*(b**(3) + c**(3)) - a*(b**(4) + c**(4)) - (b**(5) + c**(5)))', ID="X_970", classes=["center", "incident"])
    central_line(model, X_2, X_970, 2, 970, incident=True)
    X_226 = eval_trilinear_point(model, A, B, C, '(csc(A))*(cos(B) + cos(C))', ID="X_226", classes=["center", "incident"])
    X_986 = eval_trilinear_point(model, A, B, C, '(a*(b**(2) + b*c + c**(2)) + b**(3) + c**(3))', ID="X_986", classes=["center", "incident"])
    central_line(model, X_226, X_986, 226, 986, incident=True)
    X_4 = orthocenter_of(model, A, B, C, ID="X_4", classes=["center", "incident"])
    X_2092 = eval_trilinear_point(model, A, B, C, '(a**(2)*(b + c)**(2) + a*(b + c)*(b**(2) + c**(2)))', ID="X_2092", classes=["center", "incident"])
    central_line(model, X_4, X_2092, 4, 2092, incident=True)
    return promote_point_to_top(model, X_3597)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3597 on the given reference triangle."""
    model = create_model('X_3597 = 2nd ODEHNAL POINT')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03597(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03597.json"))
    write_center_svg(
        model_acute,
        here / "x-03597.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
