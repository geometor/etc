"""GEOMETOR construction model for X_2513 = RADICAL CENTER OF {CIRCUMCIRCLE, GALLATLY CIRCLE, (X_4,2R)}."""

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


def construct_x_02513(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2513 = RADICAL CENTER OF {CIRCUMCIRCLE, GALLATLY CIRCLE, (X_4,2R)} on reference triangle ABC."""
    X_2513 = eval_trilinear_point(model, A, B, C, '(a*(b**(2) - c**(2))*(a**(2)*(2*b**(4) + 3*b**(2)*c**(2) + 2*c**(4)) + b**(2)*c**(2)*(b**(2) + c**(2))))', ID="X_2513", classes=["selected", "target"])
    X_325 = eval_trilinear_point(model, A, B, C, '(csc(A))**(2)', ID="X_325", classes=["center", "incident"])
    X_523 = eval_trilinear_point(model, A, B, C, 'sin(B -C)', ID="X_523", classes=["center", "incident"])
    central_line(model, X_325, X_523, 325, 523, incident=True)
    X_647 = eval_trilinear_point(model, A, B, C, 'a*(b**(2) - c**(2))*(b**(2) + c**(2) - a**(2))', ID="X_647", classes=["center", "incident"])
    X_688 = eval_trilinear_point(model, A, B, C, '(a**(3)*(b**(4) - c**(4)))', ID="X_688", classes=["center", "incident"])
    central_line(model, X_647, X_688, 647, 688, incident=True)
    X_512 = eval_trilinear_point(model, A, B, C, 'a*(b**(2) - c**(2))', ID="X_512", classes=["center", "incident"])
    X_2021 = eval_trilinear_point(model, A, B, C, '3*sin(A -  omega  ) - 2*sin(A +  omega  ) + sin(A + 3*omega  )', ID="X_2021", classes=["center", "incident"])
    central_line(model, X_512, X_2021, 512, 2021, incident=True)
    return promote_point_to_top(model, X_2513)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2513 on the given reference triangle."""
    model = create_model('X_2513 = RADICAL CENTER OF {CIRCUMCIRCLE, GALLATLY CIRCLE, (X_4,2R)}')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02513(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02513.json"))
    write_center_svg(
        model_acute,
        here / "x-02513.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
