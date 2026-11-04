"""GEOMETOR construction model for X_1393 = X_5-BETH CONJUGATE OF X_5."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    centroid_of,
    construct_baseline_triangle,
    create_model,
    crosspoint,
    eval_trilinear_point,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_01393(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1393 = X_5-BETH CONJUGATE OF X_5 on reference triangle ABC."""
    X_57 = eval_trilinear_point(model, A, B, C, '1/(b + c - a)', ID="X_57", classes=["center"])
    X_273 = eval_trilinear_point(model, A, B, C, 'sec(A)*(sec(A/2))**(2)', ID="X_273", classes=["center"])
    X_1393 = crosspoint(model, A, B, C, X_57, X_273, ID="X_1393", classes=["selected", "target"])
    X_12 = eval_trilinear_point(model, A, B, C, '1 + cos(B - C)', ID="X_12", classes=["center", "incident"])
    X_38 = eval_trilinear_point(model, A, B, C, 'b**(2) + c**(2)', ID="X_38", classes=["center", "incident"])
    central_line(model, X_12, X_38, 12, 38, incident=True)
    X_28 = eval_trilinear_point(model, A, B, C, '(tan(A))/(b + c)', ID="X_28", classes=["center", "incident"])
    X_34 = eval_trilinear_point(model, A, B, C, '1 - sec(A)', ID="X_34", classes=["center", "incident"])
    central_line(model, X_28, X_34, 28, 34, incident=True)
    X_2 = centroid_of(model, A, B, C, ID="X_2", classes=["center", "incident"])
    X_201 = eval_trilinear_point(model, A, B, C, '(cos(A))*(1 + cos(B - C))', ID="X_201", classes=["center", "incident"])
    central_line(model, X_2, X_201, 2, 201, incident=True)
    return promote_point_to_top(model, X_1393)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1393 on the given reference triangle."""
    model = create_model('X_1393 = X_5-BETH CONJUGATE OF X_5')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01393(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01393.json"))
    write_center_svg(
        model_acute,
        here / "x-01393.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
