"""GEOMETOR construction model for X_1908 = MIDPOINT OF PU(8)."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_01908(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1908 = MIDPOINT OF PU(8) on reference triangle ABC."""
    X_1908 = eval_trilinear_point(model, A, B, C, '(a**(2)*(b**(3) + c**(3)) + 2*a*b*c*(a**(2) + b*c))', ID="X_1908", classes=["selected", "target"])
    X_171 = eval_trilinear_point(model, A, B, C, 'a**(2) + b*c', ID="X_171", classes=["center", "incident"])
    X_292 = eval_trilinear_point(model, A, B, C, 'a/(a**(2) - b*c)', ID="X_292", classes=["center", "incident"])
    central_line(model, X_171, X_292, 171, 292, incident=True)
    X_42 = eval_trilinear_point(model, A, B, C, 'a*(b + c)', ID="X_42", classes=["center", "incident"])
    X_649 = eval_trilinear_point(model, A, B, C, 'a*(b - c)', ID="X_649", classes=["center", "incident"])
    central_line(model, X_42, X_649, 42, 649, incident=True)
    X_39 = eval_trilinear_point(model, A, B, C, 'a*(b**(2) + c**(2))', ID="X_39", classes=["center", "incident"])
    X_1155 = eval_trilinear_point(model, A, B, C, '(cos(B) + cos(C) - 2*cos(A))', ID="X_1155", classes=["center", "incident"])
    central_line(model, X_39, X_1155, 39, 1155, incident=True)
    return promote_point_to_top(model, X_1908)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1908 on the given reference triangle."""
    model = create_model('X_1908 = MIDPOINT OF PU(8)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01908(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01908.json"))
    write_center_svg(
        model_acute,
        here / "x-01908.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
