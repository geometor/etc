"""GEOMETOR construction model for X_3955 = X_1848com[INVERSE(n(ORTHIC TRIANGLE))]."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    circumcenter_of,
    construct_baseline_triangle,
    create_model,
    eval_barycentric_point,
    eval_trilinear_point,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_03955(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3955 = X_1848com[INVERSE(n(ORTHIC TRIANGLE))] on reference triangle ABC."""
    X_3955 = eval_barycentric_point(model, A, B, C, '(a**(2)*(a**(2) + b*c)*(b**(2) + c**(2) - a**(2)))', ID="X_3955", classes=["selected", "target"])
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center", "incident"])
    X_73 = eval_trilinear_point(model, A, B, C, 'sec(B) + sec(C)', ID="X_73", classes=["center", "incident"])
    central_line(model, X_3, X_73, 3, 73, incident=True)
    X_57 = eval_trilinear_point(model, A, B, C, '1/(b + c - a)', ID="X_57", classes=["center", "incident"])
    X_182 = eval_trilinear_point(model, A, B, C, 'cos(A-  omega  )', ID="X_182", classes=["center", "incident"])
    central_line(model, X_57, X_182, 57, 182, incident=True)
    X_63 = eval_trilinear_point(model, A, B, C, 'cot(A)', ID="X_63", classes=["center", "incident"])
    X_184 = eval_trilinear_point(model, A, B, C, 'a**(2)*cos(A)', ID="X_184", classes=["center", "incident"])
    central_line(model, X_63, X_184, 63, 184, incident=True)
    return promote_point_to_top(model, X_3955)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3955 on the given reference triangle."""
    model = create_model('X_3955 = X_1848com[INVERSE(n(ORTHIC TRIANGLE))]')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03955(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03955.json"))
    write_center_svg(
        model_acute,
        here / "x-03955.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
