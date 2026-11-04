"""GEOMETOR construction model for X_1696 = POINT ELECTRA."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    mittenpunkt_of,
    promote_point_to_top,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_01696(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1696 = POINT ELECTRA on reference triangle ABC."""
    X_1696 = eval_trilinear_point(model, A, B, C, '(b + c - a*cos(A) + r*sin(A))', ID="X_1696", classes=["selected", "target"])
    X_19 = eval_trilinear_point(model, A, B, C, 'tan(A)', ID="X_19", classes=["center", "incident"])
    X_25 = eval_trilinear_point(model, A, B, C, 'sin(A)*tan(A)', ID="X_25", classes=["center", "incident"])
    central_line(model, X_19, X_25, 19, 25, incident=True)
    X_9 = mittenpunkt_of(model, A, B, C, ID="X_9", classes=["center", "incident"])
    X_56 = eval_trilinear_point(model, A, B, C, 'a/(b + c - a)', ID="X_56", classes=["center", "incident"])
    central_line(model, X_9, X_56, 9, 56, incident=True)
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center", "incident"])
    X_1201 = eval_trilinear_point(model, A, B, C, '(a*(b**(2) + c**(2) - 2*b*c + a*b + a*c))', ID="X_1201", classes=["center", "incident"])
    central_line(model, X_6, X_1201, 6, 1201, incident=True)
    return promote_point_to_top(model, X_1696)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1696 on the given reference triangle."""
    model = create_model('X_1696 = POINT ELECTRA')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01696(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01696.json"))
    write_center_svg(
        model_acute,
        here / "x-01696.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
