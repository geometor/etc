"""GEOMETOR construction model for X_3654 = X_1-EXTRAVERSION OF {X_1, X_2, X_3}."""

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
    nagel_point_of,
    promote_point_to_top,
    spieker_center_of,
)
from geometor.etc.render import write_center_svg


def construct_x_03654(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3654 = X_1-EXTRAVERSION OF {X_1, X_2, X_3} on reference triangle ABC."""
    X_3654 = eval_barycentric_point(model, A, B, C, 'a**(4)+3*(b+c)*a**(3)-2*(b**(2)+3*b*c+c**(2))*a**(2)-3*(b**(2)-c**(2)) * (b-c)*a+(b**(2)-c**(2))**(2)', ID="X_3654", classes=["selected", "target"])
    X_30 = eval_trilinear_point(model, A, B, C, 'cos(A) - 2*cos(B)*cos(C)', ID="X_30", classes=["center", "incident"])
    X_40 = eval_trilinear_point(model, A, B, C, 'cos(B) + cos(C) - cos(A) - 1', ID="X_40", classes=["center", "incident"])
    central_line(model, X_30, X_40, 30, 40, incident=True)
    X_8 = nagel_point_of(model, A, B, C, ID="X_8", classes=["center", "incident"])
    X_376 = eval_trilinear_point(model, A, B, C, '5*cos(A) - cos(B - C)', ID="X_376", classes=["center", "incident"])
    central_line(model, X_8, X_376, 8, 376, incident=True)
    X_10 = spieker_center_of(model, A, B, C, ID="X_10", classes=["center", "incident"])
    X_381 = eval_trilinear_point(model, A, B, C, '2*cos(B - C) - cos(A)', ID="X_381", classes=["center", "incident"])
    central_line(model, X_10, X_381, 10, 381, incident=True)
    return promote_point_to_top(model, X_3654)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3654 on the given reference triangle."""
    model = create_model('X_3654 = X_1-EXTRAVERSION OF {X_1, X_2, X_3}')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03654(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03654.json"))
    write_center_svg(
        model_acute,
        here / "x-03654.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
