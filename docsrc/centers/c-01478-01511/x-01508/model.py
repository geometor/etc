"""GEOMETOR construction model for X_1508 = 2nd MORLEY-GIBERT POINT."""

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
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_01508(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1508 = 2nd MORLEY-GIBERT POINT on reference triangle ABC."""
    X_1508 = eval_trilinear_point(model, A, B, C, '(2 - sec(A/3) + sec(B/3) + sec(C/3))', ID="X_1508", classes=["selected", "target"])
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center", "incident"])
    X_357 = eval_trilinear_point(model, A, B, C, 'sec(A/3)', ID="X_357", classes=["center", "incident"])
    central_line(model, X_1, X_357, 1, 357, incident=True)
    return promote_point_to_top(model, X_1508)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1508 on the given reference triangle."""
    model = create_model('X_1508 = 2nd MORLEY-GIBERT POINT')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01508(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01508.json"))
    write_center_svg(
        model_acute,
        here / "x-01508.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
