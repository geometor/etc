"""GEOMETOR construction model for X_3499 = INTERSECTION OF LINES X_3X_695 AND X_6X_76."""

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
    point_from_barycentrics,
    promote_point_to_top,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_03499(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3499 = INTERSECTION OF LINES X_3X_695 AND X_6X_76 on reference triangle ABC."""
    X_3499 = eval_trilinear_point(model, A, B, C, '(a*(a**(4)*(b**(4) + b**(2)*c**(2) + c**(4)) + a**(2)*b**(2)*c**(2)*(b**(2) + c**(2)) - b**(4)*c**(4)))', ID="X_3499", classes=["selected", "target"])
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center", "incident"])
    X_76 = eval_trilinear_point(model, A, B, C, '1/a**(3)', ID="X_76", classes=["center", "incident"])
    central_line(model, X_6, X_76, 6, 76, incident=True)
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center", "incident"])
    X_695 = eval_trilinear_point(model, A, B, C, 'a/(a**(4) + b**(2)*c**(2))', ID="X_695", classes=["center", "incident"])
    central_line(model, X_3, X_695, 3, 695, incident=True)
    X_2076 = eval_trilinear_point(model, A, B, C, '(sin(A) - 2*cos(A)*sin(2*omega) )', ID="X_2076", classes=["center", "incident"])
    X_2916 = point_from_barycentrics(model, A, B, C, 0.54379762, 0.48047556, -0.024273171, ID="X_2916", classes=["center", "incident"])
    central_line(model, X_2076, X_2916, 2076, 2916, incident=True)
    return promote_point_to_top(model, X_3499)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3499 on the given reference triangle."""
    model = create_model('X_3499 = INTERSECTION OF LINES X_3X_695 AND X_6X_76')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03499(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03499.json"))
    write_center_svg(
        model_acute,
        here / "x-03499.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
