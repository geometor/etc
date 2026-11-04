"""GEOMETOR construction model for X_1336 = ISOGONAL CONJUGATE OF X_1335."""

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
)
from geometor.etc.render import write_center_svg


def construct_x_01336(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1336 = ISOGONAL CONJUGATE OF X_1335 on reference triangle ABC."""
    X_1335 = eval_trilinear_point(model, A, B, C, '(1 - sin(A))', ID="X_1335", classes=["center"])
    X_1336 = isogonal_conjugate(model, A, B, C, X_1335, ID="X_1336", classes=["selected", "target"])
    X_37 = eval_trilinear_point(model, A, B, C, 'b + c', ID="X_37", classes=["center", "incident"])
    X_158 = eval_trilinear_point(model, A, B, C, '(sec(A))**(2)', ID="X_158", classes=["center", "incident"])
    central_line(model, X_37, X_158, 37, 158, incident=True)
    X_57 = eval_trilinear_point(model, A, B, C, '1/(b + c - a)', ID="X_57", classes=["center", "incident"])
    X_481 = eval_trilinear_point(model, A, B, C, '1 - 2*sec(A/2)*cos(B/2)*cos(C/2)', ID="X_481", classes=["center", "incident"])
    central_line(model, X_57, X_481, 57, 481, incident=True)
    X_2 = centroid_of(model, A, B, C, ID="X_2", classes=["center", "incident"])
    X_585 = eval_trilinear_point(model, A, B, C, '((2*area*(1/b + 1/c - 1/a) + b + c - a)/a)', ID="X_585", classes=["center", "incident"])
    central_line(model, X_2, X_585, 2, 585, incident=True)
    return promote_point_to_top(model, X_1336)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1336 on the given reference triangle."""
    model = create_model('X_1336 = ISOGONAL CONJUGATE OF X_1335')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01336(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01336.json"))
    write_center_svg(
        model_acute,
        here / "x-01336.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
