"""GEOMETOR construction model for X(970) = CENTER OF THE APOLLONIUS CIRCLE."""

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
    nine_point_center_of,
    promote_point_to_top,
    spieker_center_of,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_00970(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(970) = CENTER OF THE APOLLONIUS CIRCLE on reference triangle ABC."""
    X_970 = eval_trilinear_point(model, A, B, C, 'a*(a**(3)*(b + c)**(2) + a*(a*b + a*c - 2*b*c)*(b**(2) + c**(2)) - b*c*(b**(3) + c**(3)) - a*(b**(4) + c**(4)) - (b**(5) + c**(5)))', ID="X(970)", classes=["selected", "target"])
    X_3 = circumcenter_of(model, A, B, C, ID="X(3)", classes=["center", "incident"])
    X_6 = symmedian_point_of(model, A, B, C, ID="X(6)", classes=["center", "incident"])
    central_line(model, X_3, X_6, 3, 6, incident=True)
    X_5 = nine_point_center_of(model, A, B, C, ID="X(5)", classes=["center", "incident"])
    X_10 = spieker_center_of(model, A, B, C, ID="X(10)", classes=["center", "incident"])
    central_line(model, X_5, X_10, 5, 10, incident=True)
    X_21 = eval_trilinear_point(model, A, B, C, '1/(cos(B) + cos(C))', ID="X(21)", classes=["center", "incident"])
    X_51 = eval_trilinear_point(model, A, B, C, 'a**(2)*cos(B - C)', ID="X(51)", classes=["center", "incident"])
    central_line(model, X_21, X_51, 21, 51, incident=True)
    return promote_point_to_top(model, X_970)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(970) on the given reference triangle."""
    model = create_model('X(970) = CENTER OF THE APOLLONIUS CIRCLE')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00970(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00970.json"))
    write_center_svg(
        model_acute,
        here / "x-00970.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
