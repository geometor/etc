"""GEOMETOR construction model for X(836) = CROSSPOINT OF X(1) AND X(394)."""

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
    intersect_lines,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00836(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(836) = CROSSPOINT OF X(1) AND X(394) on reference triangle ABC."""
    X_37 = eval_trilinear_point(model, A, B, C, 'b + c', ID="X(37)", classes=["center"])
    X_73 = eval_trilinear_point(model, A, B, C, 'sec(B) + sec(C)', ID="X(73)", classes=["center"])
    X_1 = incenter_of(model, A, B, C, ID="X(1)", classes=["center"])
    X_393 = eval_trilinear_point(model, A, B, C, 'sec(A) - csc(B)*csc(C)', ID="X(393)", classes=["center"])
    central_line(model, X_37, X_73, 37, 73)
    central_line(model, X_1, X_393, 1, 393)
    X_836 = intersect_lines(model, X_37, X_73, X_1, X_393, ID="X(836)", classes=["selected", "target"])
    return promote_point_to_top(model, X_836)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(836) on the given reference triangle."""
    model = create_model('X(836) = CROSSPOINT OF X(1) AND X(394)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00836(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00836.json"))
    write_center_svg(
        model_acute,
        here / "x-00836.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
