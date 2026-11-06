"""GEOMETOR construction model for X_3572 = INTERSECTION OF LINES P(6)U(6) AND P(8)U(8)."""

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
    isogonal_conjugate,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_03572(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3572 = INTERSECTION OF LINES P(6)U(6) AND P(8)U(8) on reference triangle ABC."""
    X_3570 = eval_trilinear_point(model, A, B, C, 'b*c*(a**(2) - b*c)/(b - c)', ID="X_3570", classes=["center"])
    X_3572 = isogonal_conjugate(model, A, B, C, X_3570, ID="X_3572", classes=["selected", "target"])
    X_37 = eval_trilinear_point(model, A, B, C, 'b + c', ID="X_37", classes=["center", "incident"])
    X_513 = eval_trilinear_point(model, A, B, C, 'b - c', ID="X_513", classes=["center", "incident"])
    central_line(model, X_37, X_513, 37, 513, incident=True)
    X_2 = centroid_of(model, A, B, C, ID="X_2", classes=["center", "incident"])
    X_661 = eval_trilinear_point(model, A, B, C, 'cot(B) - cot(C)', ID="X_661", classes=["center", "incident"])
    central_line(model, X_2, X_661, 2, 661, incident=True)
    X_42 = eval_trilinear_point(model, A, B, C, 'a*(b + c)', ID="X_42", classes=["center", "incident"])
    X_649 = eval_trilinear_point(model, A, B, C, 'a*(b - c)', ID="X_649", classes=["center", "incident"])
    central_line(model, X_42, X_649, 42, 649, incident=True)
    return promote_point_to_top(model, X_3572)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3572 on the given reference triangle."""
    model = create_model('X_3572 = INTERSECTION OF LINES P(6)U(6) AND P(8)U(8)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03572(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03572.json"))
    write_center_svg(
        model_acute,
        here / "x-03572.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
