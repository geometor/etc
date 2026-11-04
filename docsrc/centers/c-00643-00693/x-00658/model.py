"""GEOMETOR construction model for X_658 = TRILINEAR POLE OF LINE X_1X_7."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    feuerbach_point_of,
    gergonne_point_of,
    isogonal_conjugate,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00658(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_658 = TRILINEAR POLE OF LINE X_1X_7 on reference triangle ABC."""
    X_657 = eval_trilinear_point(model, A, B, C, '(1 + cos(A))*(cos(B) - cos(C))', ID="X_657", classes=["center"])
    X_658 = isogonal_conjugate(model, A, B, C, X_657, ID="X_658", classes=["selected", "target"])
    X_7 = gergonne_point_of(model, A, B, C, ID="X_7", classes=["center", "incident"])
    X_11 = feuerbach_point_of(model, A, B, C, ID="X_11", classes=["center", "incident"])
    central_line(model, X_7, X_11, 7, 11, incident=True)
    X_88 = eval_trilinear_point(model, A, B, C, '1/(b + c - 2*a)', ID="X_88", classes=["center", "incident"])
    X_279 = eval_trilinear_point(model, A, B, C, 'csc(A)*(tan(A/2))**(2)', ID="X_279", classes=["center", "incident"])
    central_line(model, X_88, X_279, 88, 279, incident=True)
    X_57 = eval_trilinear_point(model, A, B, C, '1/(b + c - a)', ID="X_57", classes=["center", "incident"])
    X_673 = eval_trilinear_point(model, A, B, C, 'b*c/(b**(2) + c**(2) - a*(b + c))', ID="X_673", classes=["center", "incident"])
    central_line(model, X_57, X_673, 57, 673, incident=True)
    return promote_point_to_top(model, X_658)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_658 on the given reference triangle."""
    model = create_model('X_658 = TRILINEAR POLE OF LINE X_1X_7')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00658(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00658.json"))
    write_center_svg(
        model_acute,
        here / "x-00658.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
