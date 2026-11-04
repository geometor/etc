"""GEOMETOR construction model for X_1723 = MIMOSA TRANSFORM OF X_57."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    crosspoint,
    eval_trilinear_point,
    incenter_of,
    promote_point_to_top,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_01723(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1723 = MIMOSA TRANSFORM OF X_57 on reference triangle ABC."""
    X_653 = eval_trilinear_point(model, A, B, C, '1/(sec(B) - sec(C))', ID="X_653", classes=["center"])
    X_765 = eval_trilinear_point(model, A, B, C, '(b - c) **(-2)', ID="X_765", classes=["center"])
    X_1723 = crosspoint(model, A, B, C, X_653, X_765, ID="X_1723", classes=["selected", "target"])
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center", "incident"])
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center", "incident"])
    central_line(model, X_1, X_6, 1, 6, incident=True)
    X_19 = eval_trilinear_point(model, A, B, C, 'tan(A)', ID="X_19", classes=["center", "incident"])
    X_46 = eval_trilinear_point(model, A, B, C, 'cos(B) + cos(C) - cos(A)', ID="X_46", classes=["center", "incident"])
    central_line(model, X_19, X_46, 19, 46, incident=True)
    X_35 = eval_trilinear_point(model, A, B, C, '1 + 2*cos(A)', ID="X_35", classes=["center", "incident"])
    X_380 = eval_trilinear_point(model, A, B, C, '((b + c - a)*(3*a**(3) + (b + c)*(3*a**(2) + (b - c)**(2) + a*(b + c))))', ID="X_380", classes=["center", "incident"])
    central_line(model, X_35, X_380, 35, 380, incident=True)
    return promote_point_to_top(model, X_1723)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1723 on the given reference triangle."""
    model = create_model('X_1723 = MIMOSA TRANSFORM OF X_57')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01723(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01723.json"))
    write_center_svg(
        model_acute,
        here / "x-01723.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
