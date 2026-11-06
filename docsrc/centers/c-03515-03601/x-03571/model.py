"""GEOMETOR construction model for X_3571 = INTERSECTION OF LINES P(6)P(8) AND U(6)U(8)."""

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


def construct_x_03571(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3571 = INTERSECTION OF LINES P(6)P(8) AND U(6)U(8) on reference triangle ABC."""
    X_3571 = eval_trilinear_point(model, A, B, C, 'a**(4)*b*c + a**(2)*(b**(4) - b**(3)*c - 2*b**(2)*c**(2) - b*c**(3) + c**(4)) + b**(3)*c**(3)', ID="X_3571", classes=["selected", "target"])
    X_9 = mittenpunkt_of(model, A, B, C, ID="X_9", classes=["center", "incident"])
    X_43 = eval_trilinear_point(model, A, B, C, 'a*b + a*c - b*c', ID="X_43", classes=["center", "incident"])
    central_line(model, X_9, X_43, 9, 43, incident=True)
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center", "incident"])
    X_512 = eval_trilinear_point(model, A, B, C, 'a*(b**(2) - c**(2))', ID="X_512", classes=["center", "incident"])
    central_line(model, X_1, X_512, 1, 512, incident=True)
    X_1621 = eval_trilinear_point(model, A, B, C, '(a**(2) - b*c - c*a - a*b)', ID="X_1621", classes=["center", "incident"])
    X_1964 = eval_trilinear_point(model, A, B, C, 'a**(2)*(b**(2) + c**(2))', ID="X_1964", classes=["center", "incident"])
    central_line(model, X_1621, X_1964, 1621, 1964, incident=True)
    return promote_point_to_top(model, X_3571)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3571 on the given reference triangle."""
    model = create_model('X_3571 = INTERSECTION OF LINES P(6)P(8) AND U(6)U(8)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03571(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03571.json"))
    write_center_svg(
        model_acute,
        here / "x-03571.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
