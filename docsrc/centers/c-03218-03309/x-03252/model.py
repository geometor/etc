"""GEOMETOR construction model for X_3252 = INTERSECTION OF X_7X_192 AND X_37X_513."""

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
    gergonne_point_of,
    promote_point_to_top,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_03252(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3252 = INTERSECTION OF X_7X_192 AND X_37X_513 on reference triangle ABC."""
    X_292 = eval_trilinear_point(model, A, B, C, 'a/(a**(2) - b*c)', ID="X_292", classes=["center"])
    X_672 = eval_trilinear_point(model, A, B, C, 'a*(b**(2) + c**(2) - a*(b + c))', ID="X_672", classes=["center"])
    X_3252 = ceva_conjugate(model, A, B, C, X_292, X_672, ID="X_3252", classes=["selected", "target"])
    X_7 = gergonne_point_of(model, A, B, C, ID="X_7", classes=["center", "incident"])
    X_192 = eval_trilinear_point(model, A, B, C, 'b*c*(c*a + a*b - b*c)', ID="X_192", classes=["center", "incident"])
    central_line(model, X_7, X_192, 7, 192, incident=True)
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center", "incident"])
    central_line(model, X_6, X_292, 6, 292, incident=True)
    X_37 = eval_trilinear_point(model, A, B, C, 'b + c', ID="X_37", classes=["center", "incident"])
    X_513 = eval_trilinear_point(model, A, B, C, 'b - c', ID="X_513", classes=["center", "incident"])
    central_line(model, X_37, X_513, 37, 513, incident=True)
    return promote_point_to_top(model, X_3252)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3252 on the given reference triangle."""
    model = create_model('X_3252 = INTERSECTION OF X_7X_192 AND X_37X_513')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03252(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03252.json"))
    write_center_svg(
        model_acute,
        here / "x-03252.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
