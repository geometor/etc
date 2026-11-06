"""GEOMETOR construction model for X_3183 = X_20-CEVA CONJUGATE OF X_4."""

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
    orthocenter_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_03183(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3183 = X_20-CEVA CONJUGATE OF X_4 on reference triangle ABC."""
    X_4 = orthocenter_of(model, A, B, C, ID="X_4", classes=["center"])
    X_64 = eval_trilinear_point(model, A, B, C, '1/(cos(A) - cos(B)*cos(C))', ID="X_64", classes=["center"])
    X_19 = eval_trilinear_point(model, A, B, C, 'tan(A)', ID="X_19", classes=["center"])
    X_84 = eval_trilinear_point(model, A, B, C, '1/(cos(B) + cos(C) - cos(A) - 1)', ID="X_84", classes=["center"])
    central_line(model, X_4, X_64, 4, 64)
    central_line(model, X_19, X_84, 19, 84)
    X_3183 = intersect_lines(model, X_4, X_64, X_19, X_84, ID="X_3183", classes=["selected", "target"])
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center", "incident"])
    X_196 = eval_trilinear_point(model, A, B, C, '((cos(B) + cos(C) - cos(A) - 1)*sec(A)*tan(A/2))', ID="X_196", classes=["center", "incident"])
    central_line(model, X_1, X_196, 1, 196, incident=True)
    return promote_point_to_top(model, X_3183)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3183 on the given reference triangle."""
    model = create_model('X_3183 = X_20-CEVA CONJUGATE OF X_4')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03183(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03183.json"))
    write_center_svg(
        model_acute,
        here / "x-03183.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
