"""GEOMETOR construction model for X_1392 = ISOGONAL CONJUGATE OF X_1388."""

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


def construct_x_01392(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1392 = ISOGONAL CONJUGATE OF X_1388 on reference triangle ABC."""
    X_1388 = eval_trilinear_point(model, A, B, C, '((3*a - 2*b -2*c)/(a - b - c))', ID="X_1388", classes=["center"])
    X_1392 = isogonal_conjugate(model, A, B, C, X_1388, ID="X_1392", classes=["selected", "target"])
    X_80 = eval_trilinear_point(model, A, B, C, '1/(1 - 2*cos(A))', ID="X_80", classes=["center", "incident"])
    X_145 = eval_trilinear_point(model, A, B, C, 'b*c*(3*a - b - c)', ID="X_145", classes=["center", "incident"])
    central_line(model, X_80, X_145, 80, 145, incident=True)
    return promote_point_to_top(model, X_1392)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1392 on the given reference triangle."""
    model = create_model('X_1392 = ISOGONAL CONJUGATE OF X_1388')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01392(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01392.json"))
    write_center_svg(
        model_acute,
        here / "x-01392.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
