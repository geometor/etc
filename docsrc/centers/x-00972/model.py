"""GEOMETOR construction model for X(972) = ISOGONAL CONJUGATE OF X(971)."""

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
    reflection_in_point,
)
from geometor.etc.render import write_center_svg


def construct_x_00972(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(972) = ISOGONAL CONJUGATE OF X(971) on reference triangle ABC."""
    X_934 = eval_trilinear_point(model, A, B, C, '1/((b - c)*(b + c - a)**(2))', ID="X(934)", classes=["center"])
    X_3 = circumcenter_of(model, A, B, C, ID="X(3)", classes=["center"])
    X_972 = reflection_in_point(model, X_934, X_3, ID="X(972)", classes=["selected", "target"], guide=False)
    X_40 = eval_trilinear_point(model, A, B, C, 'cos(B) + cos(C) - cos(A) - 1', ID="X(40)", classes=["center", "incident"])
    X_101 = eval_trilinear_point(model, A, B, C, 'a/(b - c)', ID="X(101)", classes=["center", "incident"])
    central_line(model, X_40, X_101, 40, 101, incident=True)
    X_55 = eval_trilinear_point(model, A, B, C, 'a*(b + c - a)', ID="X(55)", classes=["center", "incident"])
    X_108 = eval_trilinear_point(model, A, B, C, 'a/(sec(B) - sec(C))', ID="X(108)", classes=["center", "incident"])
    central_line(model, X_55, X_108, 55, 108, incident=True)
    X_109 = eval_trilinear_point(model, A, B, C, 'a/(cos(B) - cos(C))', ID="X(109)", classes=["center", "incident"])
    X_165 = eval_trilinear_point(model, A, B, C, 'tan(B/2) + tan(C/2) - tan(A/2)', ID="X(165)", classes=["center", "incident"])
    central_line(model, X_109, X_165, 109, 165, incident=True)
    return promote_point_to_top(model, X_972)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(972) on the given reference triangle."""
    model = create_model('X(972) = ISOGONAL CONJUGATE OF X(971)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00972(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00972.json"))
    write_center_svg(
        model_acute,
        here / "x-00972.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
