"""GEOMETOR construction model for X_2500 = RADICAL CENTER OF {CIRCUMCIRCLE, SPIEKER CIRCLE, APOLLONIUS CIRCLE}."""

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


def construct_x_02500(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2500 = RADICAL CENTER OF {CIRCUMCIRCLE, SPIEKER CIRCLE, APOLLONIUS CIRCLE} on reference triangle ABC."""
    X_2500 = eval_trilinear_point(model, A, B, C, '((b - c)*(4*b*c*(b + c)**(2) - 2*a**(2)*(b**(2) + c**(2)) + a*(b + c)*(3*b**(2) - 2*b*c + 3*c**(2)) - 5*a**(3)*(b + c)))', ID="X_2500", classes=["selected", "target"])
    X_512 = eval_trilinear_point(model, A, B, C, 'a*(b**(2) - c**(2))', ID="X_512", classes=["center", "incident"])
    X_650 = eval_trilinear_point(model, A, B, C, 'cos(B) - cos(C)', ID="X_650", classes=["center", "incident"])
    central_line(model, X_512, X_650, 512, 650, incident=True)
    X_522 = eval_trilinear_point(model, A, B, C, '(cos(B) - cos(C))*(csc(A))', ID="X_522", classes=["center", "incident"])
    X_2490 = eval_trilinear_point(model, A, B, C, '(b*c*(b - c)*(4*a**(2) - 3*a*b - 3*a*c + (b + c)**(2)))', ID="X_2490", classes=["center", "incident"])
    central_line(model, X_522, X_2490, 522, 2490, incident=True)
    X_513 = eval_trilinear_point(model, A, B, C, 'b - c', ID="X_513", classes=["center", "incident"])
    X_2532 = eval_trilinear_point(model, A, B, C, '((b - c)*(5*(b + c)*a**(3) + 2*(b**(2) - b*c + c**(2))*a**(2) - 3*(b + c)*(b**(2) + c**(2))*a - 4*b*c*(b + c)**(2)))', ID="X_2532", classes=["center", "incident"])
    central_line(model, X_513, X_2532, 513, 2532, incident=True)
    return promote_point_to_top(model, X_2500)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2500 on the given reference triangle."""
    model = create_model('X_2500 = RADICAL CENTER OF {CIRCUMCIRCLE, SPIEKER CIRCLE, APOLLONIUS CIRCLE}')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02500(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02500.json"))
    write_center_svg(
        model_acute,
        here / "x-02500.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
