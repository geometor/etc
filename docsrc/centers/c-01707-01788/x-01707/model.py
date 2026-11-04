"""GEOMETOR construction model for X_1707 = MIMOSA TRANSFORM OF X_6."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    incenter_of,
    mittenpunkt_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_01707(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1707 = MIMOSA TRANSFORM OF X_6 on reference triangle ABC."""
    X_1707 = eval_trilinear_point(model, A, B, C, '3*a**(2) - b**(2) - c**(2)', ID="X_1707", classes=["selected", "target"])
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center", "incident"])
    X_21 = eval_trilinear_point(model, A, B, C, '1/(cos(B) + cos(C))', ID="X_21", classes=["center", "incident"])
    central_line(model, X_1, X_21, 1, 21, incident=True)
    X_9 = mittenpunkt_of(model, A, B, C, ID="X_9", classes=["center", "incident"])
    X_171 = eval_trilinear_point(model, A, B, C, 'a**(2) + b*c', ID="X_171", classes=["center", "incident"])
    central_line(model, X_9, X_171, 9, 171, incident=True)
    X_43 = eval_trilinear_point(model, A, B, C, 'a*b + a*c - b*c', ID="X_43", classes=["center", "incident"])
    X_165 = eval_trilinear_point(model, A, B, C, 'tan(B/2) + tan(C/2) - tan(A/2)', ID="X_165", classes=["center", "incident"])
    central_line(model, X_43, X_165, 43, 165, incident=True)
    return promote_point_to_top(model, X_1707)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1707 on the given reference triangle."""
    model = create_model('X_1707 = MIMOSA TRANSFORM OF X_6')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01707(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01707.json"))
    write_center_svg(
        model_acute,
        here / "x-01707.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
