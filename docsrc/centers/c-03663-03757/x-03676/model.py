"""GEOMETOR construction model for X_3676 = X_650com(INTOUCH TRIANGLE)."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_barycentric_point,
    eval_trilinear_point,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_03676(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3676 = X_650com(INTOUCH TRIANGLE) on reference triangle ABC."""
    X_3676 = eval_barycentric_point(model, A, B, C, '(b - c)/(b + c - a)', ID="X_3676", classes=["selected", "target"])
    X_57 = eval_trilinear_point(model, A, B, C, '1/(b + c - a)', ID="X_57", classes=["center", "incident"])
    X_649 = eval_trilinear_point(model, A, B, C, 'a*(b - c)', ID="X_649", classes=["center", "incident"])
    central_line(model, X_57, X_649, 57, 649, incident=True)
    X_241 = eval_trilinear_point(model, A, B, C, '(cos(B/2))**(4) - ((cos(A/2))**(2))*((cos(B/2))**(2) +(cos(C/2))**(2)) + (cos(C/2))**(4)', ID="X_241", classes=["center", "incident"])
    X_514 = eval_trilinear_point(model, A, B, C, '(b - c)/a', ID="X_514", classes=["center", "incident"])
    central_line(model, X_241, X_514, 241, 514, incident=True)
    X_109 = eval_trilinear_point(model, A, B, C, 'a/(cos(B) - cos(C))', ID="X_109", classes=["center", "incident"])
    X_658 = eval_trilinear_point(model, A, B, C, '1/((1 + cos(A))*(cos(B) - cos(C)))', ID="X_658", classes=["center", "incident"])
    central_line(model, X_109, X_658, 109, 658, incident=True)
    return promote_point_to_top(model, X_3676)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3676 on the given reference triangle."""
    model = create_model('X_3676 = X_650com(INTOUCH TRIANGLE)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03676(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03676.json"))
    write_center_svg(
        model_acute,
        here / "x-03676.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
