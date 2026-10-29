"""GEOMETOR construction model for X(173) = CONGRUENT ISOSCELIZERS POINT."""

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
    mittenpunkt_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00173(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(173) = CONGRUENT ISOSCELIZERS POINT on reference triangle ABC."""
    X_173 = eval_trilinear_point(model, A, B, C, 'cos(B/2) + cos(C/2) - cos(A/2)', ID="X(173)", classes=["selected", "target"])
    X_1 = incenter_of(model, A, B, C, ID="X(1)", classes=["center", "incident"])
    X_168 = eval_trilinear_point(model, A, B, C, 'sin(A) - sin(B) - sin(C) + 2*(cos(A/2) + sin(B/2 - A/2) + sin(C/2 - A/2))', ID="X(168)", classes=["center", "incident"])
    central_line(model, X_1, X_168, 1, 168, incident=True)
    X_9 = mittenpunkt_of(model, A, B, C, ID="X(9)", classes=["center", "incident"])
    X_177 = eval_trilinear_point(model, A, B, C, '(cos(B/2) + cos(C/2))*sec(A/2)', ID="X(177)", classes=["center", "incident"])
    central_line(model, X_9, X_177, 9, 177, incident=True)
    X_57 = eval_trilinear_point(model, A, B, C, '1/(b + c - a)', ID="X(57)", classes=["center", "incident"])
    X_174 = eval_trilinear_point(model, A, B, C, 'sec(A/2)', ID="X(174)", classes=["center", "incident"])
    central_line(model, X_57, X_174, 57, 174, incident=True)
    return promote_point_to_top(model, X_173)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(173) on the given reference triangle."""
    model = create_model('X(173) = CONGRUENT ISOSCELIZERS POINT')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00173(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00173.json"))
    write_center_svg(
        model_acute,
        here / "x-00173.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
