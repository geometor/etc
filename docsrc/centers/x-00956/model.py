"""GEOMETOR construction model for X(956) = INTERSECTION OF LINES X(1)X(6) AND X(3)X(8)."""

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
    incenter_of,
    nagel_point_of,
    promote_point_to_top,
    spieker_center_of,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_00956(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(956) = INTERSECTION OF LINES X(1)X(6) AND X(3)X(8) on reference triangle ABC."""
    X_956 = eval_trilinear_point(model, A, B, C, 'a**(3)- a*(b - c)**(2)- 2*b*c*(b + c)', ID="X(956)", classes=["selected", "target"])
    X_1 = incenter_of(model, A, B, C, ID="X(1)", classes=["center", "incident"])
    X_6 = symmedian_point_of(model, A, B, C, ID="X(6)", classes=["center", "incident"])
    central_line(model, X_1, X_6, 1, 6, incident=True)
    X_3 = circumcenter_of(model, A, B, C, ID="X(3)", classes=["center", "incident"])
    X_8 = nagel_point_of(model, A, B, C, ID="X(8)", classes=["center", "incident"])
    central_line(model, X_3, X_8, 3, 8, incident=True)
    X_10 = spieker_center_of(model, A, B, C, ID="X(10)", classes=["center", "incident"])
    X_56 = eval_trilinear_point(model, A, B, C, 'a/(b + c - a)', ID="X(56)", classes=["center", "incident"])
    central_line(model, X_10, X_56, 10, 56, incident=True)
    return promote_point_to_top(model, X_956)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(956) on the given reference triangle."""
    model = create_model('X(956) = INTERSECTION OF LINES X(1)X(6) AND X(3)X(8)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00956(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00956.json"))
    write_center_svg(
        model_acute,
        here / "x-00956.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
