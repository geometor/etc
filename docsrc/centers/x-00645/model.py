"""GEOMETOR construction model for X(645) = BARYCENTRIC MULTIPLIER FOR KIEPERT PARABOLA."""

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
)
from geometor.etc.render import write_center_svg


def construct_x_00645(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(645) = BARYCENTRIC MULTIPLIER FOR KIEPERT PARABOLA on reference triangle ABC."""
    X_645 = eval_trilinear_point(model, A, B, C, '(b + c - a)/(a*(b**(2)- c**(2)))', ID="X(645)", classes=["selected", "target"])
    X_99 = eval_trilinear_point(model, A, B, C, 'b*c/(b**(2) - c**(2))', ID="X(99)", classes=["center", "incident"])
    X_101 = eval_trilinear_point(model, A, B, C, 'a/(b - c)', ID="X(101)", classes=["center", "incident"])
    central_line(model, X_99, X_101, 99, 101, incident=True)
    X_9 = mittenpunkt_of(model, A, B, C, ID="X(9)", classes=["center", "incident"])
    X_261 = eval_trilinear_point(model, A, B, C, '((csc(A))*(sec(B/2 - C/2)))**(2)', ID="X(261)", classes=["center", "incident"])
    central_line(model, X_9, X_261, 9, 261, incident=True)
    X_294 = eval_trilinear_point(model, A, B, C, '(b + c - a)/(b**(2)+ c**(2)- a*b - a*c)', ID="X(294)", classes=["center", "incident"])
    X_314 = eval_trilinear_point(model, A, B, C, 'b**(2)*c**(2)*(b + c - a)/(b + c)', ID="X(314)", classes=["center", "incident"])
    central_line(model, X_294, X_314, 294, 314, incident=True)
    return promote_point_to_top(model, X_645)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(645) on the given reference triangle."""
    model = create_model('X(645) = BARYCENTRIC MULTIPLIER FOR KIEPERT PARABOLA')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00645(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00645.json"))
    write_center_svg(
        model_acute,
        here / "x-00645.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
