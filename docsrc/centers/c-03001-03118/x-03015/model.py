"""GEOMETOR construction model for X_3015 = (GERGONNE LINE)∩(FERMAT AXIS)."""

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
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_03015(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3015 = (GERGONNE LINE)∩(FERMAT AXIS) on reference triangle ABC."""
    X_3015 = eval_trilinear_point(model, A, B, C, '((1 + cos(B))*sin(A - B)*(1 + 2*cos(2*C)) + (1 + cos(C))*sin(A - C)*(1 + 2*cos(2*B)))', ID="X_3015", classes=["selected", "target"])
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center", "incident"])
    X_13 = eval_trilinear_point(model, A, B, C, 'csc(A +  pi  /3)', ID="X_13", classes=["center", "incident"])
    central_line(model, X_6, X_13, 6, 13, incident=True)
    X_241 = eval_trilinear_point(model, A, B, C, '(cos(B/2))**(4) - ((cos(A/2))**(2))*((cos(B/2))**(2) +(cos(C/2))**(2)) + (cos(C/2))**(4)', ID="X_241", classes=["center", "incident"])
    X_514 = eval_trilinear_point(model, A, B, C, '(b - c)/a', ID="X_514", classes=["center", "incident"])
    central_line(model, X_241, X_514, 241, 514, incident=True)
    return promote_point_to_top(model, X_3015)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3015 on the given reference triangle."""
    model = create_model('X_3015 = (GERGONNE LINE)∩(FERMAT AXIS)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03015(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03015.json"))
    write_center_svg(
        model_acute,
        here / "x-03015.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
