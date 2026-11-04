"""GEOMETOR construction model for X_1940 = CROSSSUM OF PU(16)."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    ceva_conjugate,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    orthocenter_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_01940(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1940 = CROSSSUM OF PU(16) on reference triangle ABC."""
    X_1937 = eval_trilinear_point(model, A, B, C, '(1/((cos(A))**(2) - cos(B)*cos(C)))', ID="X_1937", classes=["center"])
    X_243 = eval_trilinear_point(model, A, B, C, '(sec(A))*((cos(A))**(2) - cos(B)*cos(C))', ID="X_243", classes=["center"])
    X_1940 = ceva_conjugate(model, A, B, C, X_1937, X_243, ID="X_1940", classes=["selected", "target"])
    X_4 = orthocenter_of(model, A, B, C, ID="X_4", classes=["center", "incident"])
    X_46 = eval_trilinear_point(model, A, B, C, 'cos(B) + cos(C) - cos(A)', ID="X_46", classes=["center", "incident"])
    central_line(model, X_4, X_46, 4, 46, incident=True)
    X_29 = eval_trilinear_point(model, A, B, C, '(sec(A))/(cos(B) + cos(C))', ID="X_29", classes=["center", "incident"])
    X_65 = eval_trilinear_point(model, A, B, C, 'cos(B) + cos(C)', ID="X_65", classes=["center", "incident"])
    central_line(model, X_29, X_65, 29, 65, incident=True)
    X_34 = eval_trilinear_point(model, A, B, C, '1 - sec(A)', ID="X_34", classes=["center", "incident"])
    X_87 = eval_trilinear_point(model, A, B, C, '1/(a*b + a*c - b*c)', ID="X_87", classes=["center", "incident"])
    central_line(model, X_34, X_87, 34, 87, incident=True)
    return promote_point_to_top(model, X_1940)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1940 on the given reference triangle."""
    model = create_model('X_1940 = CROSSSUM OF PU(16)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01940(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01940.json"))
    write_center_svg(
        model_acute,
        here / "x-01940.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
