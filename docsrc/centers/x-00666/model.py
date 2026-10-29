"""GEOMETOR construction model for X(666) = TRILINEAR POLE OF LINE X(2)X(11)."""

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


def construct_x_00666(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(666) = TRILINEAR POLE OF LINE X(2)X(11) on reference triangle ABC."""
    X_665 = eval_trilinear_point(model, A, B, C, 'a*((a - b)**(2)*(a + b - c) - (c - a)**(2)*(c + a - b))', ID="X(665)", classes=["center"])
    X_666 = isogonal_conjugate(model, A, B, C, X_665, ID="X(666)", classes=["selected", "target"])
    X_239 = eval_trilinear_point(model, A, B, C, 'b*c*(a**(2) - b*c)', ID="X(239)", classes=["center", "incident"])
    X_294 = eval_trilinear_point(model, A, B, C, '(b + c - a)/(b**(2)+ c**(2)- a*b - a*c)', ID="X(294)", classes=["center", "incident"])
    central_line(model, X_239, X_294, 239, 294, incident=True)
    X_101 = eval_trilinear_point(model, A, B, C, 'a/(b - c)', ID="X(101)", classes=["center", "incident"])
    X_514 = eval_trilinear_point(model, A, B, C, '(b - c)/a', ID="X(514)", classes=["center", "incident"])
    central_line(model, X_101, X_514, 101, 514, incident=True)
    X_190 = eval_trilinear_point(model, A, B, C, 'b*c/(b - c)', ID="X(190)", classes=["center", "incident"])
    X_522 = eval_trilinear_point(model, A, B, C, '(cos(B) - cos(C))*(csc(A))', ID="X(522)", classes=["center", "incident"])
    central_line(model, X_190, X_522, 190, 522, incident=True)
    return promote_point_to_top(model, X_666)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(666) on the given reference triangle."""
    model = create_model('X(666) = TRILINEAR POLE OF LINE X(2)X(11)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00666(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00666.json"))
    write_center_svg(
        model_acute,
        here / "x-00666.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
