"""GEOMETOR construction model for X_3375 = TAN(A - π/3) POINT."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_03375(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3375 = TAN(A - π/3) POINT on reference triangle ABC."""
    X_3375 = eval_trilinear_point(model, A, B, C, '(tan(A -  pi  /3))', ID="X_3375", classes=["selected", "target"])
    X_17 = eval_trilinear_point(model, A, B, C, 'csc(A +  pi  /6)', ID="X_17", classes=["center", "incident"])
    X_1652 = eval_trilinear_point(model, A, B, C, '(sqrt(3/4) - sin(A +  pi  /3) + sin(B +  pi  /3) + sin(C +  pi  /3))', ID="X_1652", classes=["center", "incident"])
    central_line(model, X_17, X_1652, 17, 1652, incident=True)
    X_19 = eval_trilinear_point(model, A, B, C, 'tan(A)', ID="X_19", classes=["center", "incident"])
    X_2290 = eval_trilinear_point(model, A, B, C, 'sin(3*A)*cos(B - C)', ID="X_2290", classes=["center", "incident"])
    central_line(model, X_19, X_2290, 19, 2290, incident=True)
    return promote_point_to_top(model, X_3375)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3375 on the given reference triangle."""
    model = create_model('X_3375 = TAN(A - π/3) POINT')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03375(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03375.json"))
    write_center_svg(
        model_acute,
        here / "x-03375.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
