"""GEOMETOR construction model for X_2497 = RADICAL CENTER OF {CIRCUMCIRCLE, INCIRCLE, GALLATLY CIRCLE}."""

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


def construct_x_02497(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2497 = RADICAL CENTER OF {CIRCUMCIRCLE, INCIRCLE, GALLATLY CIRCLE} on reference triangle ABC."""
    X_2497 = eval_trilinear_point(model, A, B, C, '(a*(b - c)*((b + c)*(b**(2)*c**(2)*(b - c)**(2) + a**(4)*(b**(2) + c**(2)) +a**(2)*(b**(2) - b*c + c**(2))**(2)) - 2*a**(3)*(b**(4) + b**(2)*c**(2) + c**(4))))', ID="X_2497", classes=["selected", "target"])
    X_513 = eval_trilinear_point(model, A, B, C, 'b - c', ID="X_513", classes=["center", "incident"])
    X_676 = eval_trilinear_point(model, A, B, C, '(b*c*(b - c)*(b**(3) + c**(3) - 2*a**(3) + (b + c)*(a**(2) - b*c)))', ID="X_676", classes=["center", "incident"])
    central_line(model, X_513, X_676, 513, 676, incident=True)
    X_512 = eval_trilinear_point(model, A, B, C, 'a*(b**(2) - c**(2))', ID="X_512", classes=["center", "incident"])
    X_2021 = eval_trilinear_point(model, A, B, C, '3*sin(A -  omega  ) - 2*sin(A +  omega  ) + sin(A + 3*omega  )', ID="X_2021", classes=["center", "incident"])
    central_line(model, X_512, X_2021, 512, 2021, incident=True)
    return promote_point_to_top(model, X_2497)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2497 on the given reference triangle."""
    model = create_model('X_2497 = RADICAL CENTER OF {CIRCUMCIRCLE, INCIRCLE, GALLATLY CIRCLE}')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02497(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02497.json"))
    write_center_svg(
        model_acute,
        here / "x-02497.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
