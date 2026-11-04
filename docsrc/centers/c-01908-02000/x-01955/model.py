"""GEOMETOR construction model for X_1955 = CROSSDIFFERENCE OF PU(21)."""

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
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_01955(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1955 = CROSSDIFFERENCE OF PU(21) on reference triangle ABC."""
    X_1955 = eval_trilinear_point(model, A, B, C, '(sin(2*B)*sin(2*C) - (sin(2*A))**(2))', ID="X_1955", classes=["selected", "target"])
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center", "incident"])
    X_19 = eval_trilinear_point(model, A, B, C, 'tan(A)', ID="X_19", classes=["center", "incident"])
    central_line(model, X_1, X_19, 1, 19, incident=True)
    X_58 = eval_trilinear_point(model, A, B, C, 'a/(b + c)', ID="X_58", classes=["center", "incident"])
    X_1047 = point_from_barycentrics(model, A, B, C, 0.47678192, 0.53587009, -0.012652005, ID="X_1047", classes=["center", "incident"])
    central_line(model, X_58, X_1047, 58, 1047, incident=True)
    X_47 = eval_trilinear_point(model, A, B, C, 'cos(2*A)', ID="X_47", classes=["center", "incident"])
    X_1740 = eval_trilinear_point(model, A, B, C, '(a**(2)*b**(2) + a**(2)*c**(2) - b**(2)*c**(2))', ID="X_1740", classes=["center", "incident"])
    central_line(model, X_47, X_1740, 47, 1740, incident=True)
    return promote_point_to_top(model, X_1955)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1955 on the given reference triangle."""
    model = create_model('X_1955 = CROSSDIFFERENCE OF PU(21)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01955(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01955.json"))
    write_center_svg(
        model_acute,
        here / "x-01955.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
