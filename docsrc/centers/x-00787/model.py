"""GEOMETOR construction model for X(787) = o-(- 3, - 1) CIRCUMCIRCLE POINT."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    isogonal_conjugate,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00787(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(787) = o-(- 3, - 1) CIRCUMCIRCLE POINT on reference triangle ABC."""
    X_786 = eval_trilinear_point(model, A, B, C, 'a**(-4)*(b**(-1)- c**(-1)) + a**(-2)*(b**(-3)- c**(-3))', ID="X(786)", classes=["center"])
    X_787 = isogonal_conjugate(model, A, B, C, X_786, ID="X(787)", classes=["selected", "target"])
    X_662 = eval_trilinear_point(model, A, B, C, '1/(cot(B) - cot(C))', ID="X(662)", classes=["center", "incident"])
    X_689 = eval_trilinear_point(model, A, B, C, '1/(a**(3)*(b**(4) - c**(4)))', ID="X(689)", classes=["center", "incident"])
    central_line(model, X_662, X_689, 662, 689, incident=True)
    return promote_point_to_top(model, X_787)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(787) on the given reference triangle."""
    model = create_model('X(787) = o-(- 3, - 1) CIRCUMCIRCLE POINT')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00787(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00787.json"))
    write_center_svg(
        model_acute,
        here / "x-00787.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
