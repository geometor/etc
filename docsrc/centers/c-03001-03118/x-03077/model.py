"""GEOMETOR construction model for X_3077 = INTERSECTION OF X_1X_605 AND X_47X_606."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    incenter_of,
    promote_point_to_top,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_03077(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3077 = INTERSECTION OF X_1X_605 AND X_47X_606 on reference triangle ABC."""
    X_3077 = eval_trilinear_point(model, A, B, C, '(cos(A))**(2) - sin(A)', ID="X_3077", classes=["selected", "target"])
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center", "incident"])
    X_255 = eval_trilinear_point(model, A, B, C, '(cos(A))**(2)', ID="X_255", classes=["center", "incident"])
    central_line(model, X_6, X_255, 6, 255, incident=True)
    X_212 = eval_trilinear_point(model, A, B, C, '(cos(A))*(1 + cos(A))', ID="X_212", classes=["center", "incident"])
    X_371 = eval_trilinear_point(model, A, B, C, 'cos(A -  pi  /4)', ID="X_371", classes=["center", "incident"])
    central_line(model, X_212, X_371, 212, 371, incident=True)
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center", "incident"])
    X_605 = eval_trilinear_point(model, A, B, C, 'a*(1 + sin(A))', ID="X_605", classes=["center", "incident"])
    central_line(model, X_1, X_605, 1, 605, incident=True)
    return promote_point_to_top(model, X_3077)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3077 on the given reference triangle."""
    model = create_model('X_3077 = INTERSECTION OF X_1X_605 AND X_47X_606')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03077(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03077.json"))
    write_center_svg(
        model_acute,
        here / "x-03077.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
