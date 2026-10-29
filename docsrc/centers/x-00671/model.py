"""GEOMETOR construction model for X(671) = TRILINEAR POLE OF LINE X(2)X(523)."""

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
    spieker_center_of,
)
from geometor.etc.render import write_center_svg


def construct_x_00671(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(671) = TRILINEAR POLE OF LINE X(2)X(523) on reference triangle ABC."""
    X_187 = eval_trilinear_point(model, A, B, C, 'a*(2*a**(2) - b**(2) - c**(2))', ID="X(187)", classes=["center"])
    X_671 = isogonal_conjugate(model, A, B, C, X_187, ID="X(671)", classes=["selected", "target"])
    X_2 = centroid_of(model, A, B, C, ID="X(2)", classes=["center", "incident"])
    X_99 = eval_trilinear_point(model, A, B, C, 'b*c/(b**(2) - c**(2))', ID="X(99)", classes=["center", "incident"])
    central_line(model, X_2, X_99, 2, 99, incident=True)
    X_30 = eval_trilinear_point(model, A, B, C, 'cos(A) - 2*cos(B)*cos(C)', ID="X(30)", classes=["center", "incident"])
    X_98 = eval_trilinear_point(model, A, B, C, 'sec(A + omega )', ID="X(98)", classes=["center", "incident"])
    central_line(model, X_30, X_98, 30, 98, incident=True)
    X_10 = spieker_center_of(model, A, B, C, ID="X(10)", classes=["center", "incident"])
    X_190 = eval_trilinear_point(model, A, B, C, 'b*c/(b - c)', ID="X(190)", classes=["center", "incident"])
    central_line(model, X_10, X_190, 10, 190, incident=True)
    return promote_point_to_top(model, X_671)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(671) on the given reference triangle."""
    model = create_model('X(671) = TRILINEAR POLE OF LINE X(2)X(523)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00671(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00671.json"))
    write_center_svg(
        model_acute,
        here / "x-00671.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
