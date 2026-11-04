"""GEOMETOR construction model for X_1578 = POINT ALTERF I."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    circumcenter_of,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    promote_point_to_top,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_01578(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1578 = POINT ALTERF I on reference triangle ABC."""
    X_1578 = eval_trilinear_point(model, A, B, C, 'sin(A) + sec(B)*sec(C)', ID="X_1578", classes=["selected", "target"])
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center", "incident"])
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center", "incident"])
    central_line(model, X_3, X_6, 3, 6, incident=True)
    X_394 = eval_trilinear_point(model, A, B, C, 'cos(A)*cot(A)', ID="X_394", classes=["center", "incident"])
    X_488 = eval_trilinear_point(model, A, B, C, '((cos(A))*(1 + csc(A)*sin(B)*sin(C)))', ID="X_488", classes=["center", "incident"])
    central_line(model, X_394, X_488, 394, 488, incident=True)
    X_485 = eval_trilinear_point(model, A, B, C, 'sec(A -  pi  /4)', ID="X_485", classes=["center", "incident"])
    X_1368 = eval_trilinear_point(model, A, B, C, 'b*c*(b**(2)/(a**(2) - b**(2) + c**(2)) + c**(2)/(a**(2) + b**(2) - c**(2)))', ID="X_1368", classes=["center", "incident"])
    central_line(model, X_485, X_1368, 485, 1368, incident=True)
    return promote_point_to_top(model, X_1578)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1578 on the given reference triangle."""
    model = create_model('X_1578 = POINT ALTERF I')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01578(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01578.json"))
    write_center_svg(
        model_acute,
        here / "x-01578.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
