"""GEOMETOR construction model for X_1763 = MIMOSA TRANSFORM OF X_326."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    ceva_conjugate,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    incenter_of,
    promote_point_to_top,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_01763(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1763 = MIMOSA TRANSFORM OF X_326 on reference triangle ABC."""
    X_69 = eval_trilinear_point(model, A, B, C, '(cos(A))/a**(2)', ID="X_69", classes=["center"])
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center"])
    X_1763 = ceva_conjugate(model, A, B, C, X_69, X_1, ID="X_1763", classes=["selected", "target"])
    X_25 = eval_trilinear_point(model, A, B, C, 'sin(A)*tan(A)', ID="X_25", classes=["center", "incident"])
    central_line(model, X_1, X_25, 1, 25, incident=True)
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center", "incident"])
    X_57 = eval_trilinear_point(model, A, B, C, '1/(b + c - a)', ID="X_57", classes=["center", "incident"])
    central_line(model, X_6, X_57, 6, 57, incident=True)
    X_43 = eval_trilinear_point(model, A, B, C, 'a*b + a*c - b*c', ID="X_43", classes=["center", "incident"])
    X_46 = eval_trilinear_point(model, A, B, C, 'cos(B) + cos(C) - cos(A)', ID="X_46", classes=["center", "incident"])
    central_line(model, X_43, X_46, 43, 46, incident=True)
    return promote_point_to_top(model, X_1763)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1763 on the given reference triangle."""
    model = create_model('X_1763 = MIMOSA TRANSFORM OF X_326')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01763(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01763.json"))
    write_center_svg(
        model_acute,
        here / "x-01763.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
