"""GEOMETOR construction model for X_3216 = X_58-CEVA CONJUGATE OF X_1."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    centroid_of,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    incenter_of,
    midpoint,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_03216(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3216 = X_58-CEVA CONJUGATE OF X_1 on reference triangle ABC."""
    X_1201 = eval_trilinear_point(model, A, B, C, '(a*(b**(2) + c**(2) - 2*b*c + a*b + a*c))', ID="X_1201", classes=["center"])
    X_3214 = eval_trilinear_point(model, A, B, C, '((b + c)*(a**(2) + a*b + a*c - 2*b*c))', ID="X_3214", classes=["center"])
    X_3216 = midpoint(model, X_1201, X_3214, ID="X_3216", classes=["selected", "target"], guide=False)
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center", "incident"])
    X_2 = centroid_of(model, A, B, C, ID="X_2", classes=["center", "incident"])
    central_line(model, X_1, X_2, 1, 2, incident=True)
    X_35 = eval_trilinear_point(model, A, B, C, '1 + 2*cos(A)', ID="X_35", classes=["center", "incident"])
    X_238 = eval_trilinear_point(model, A, B, C, 'a**(2) - b*c', ID="X_238", classes=["center", "incident"])
    central_line(model, X_35, X_238, 35, 238, incident=True)
    X_58 = eval_trilinear_point(model, A, B, C, 'a/(b + c)', ID="X_58", classes=["center", "incident"])
    X_404 = eval_trilinear_point(model, A, B, C, '(b*c*(a + b + c) - a*(b**(2) + c**(2) - a**(2)))', ID="X_404", classes=["center", "incident"])
    central_line(model, X_58, X_404, 58, 404, incident=True)
    return promote_point_to_top(model, X_3216)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3216 on the given reference triangle."""
    model = create_model('X_3216 = X_58-CEVA CONJUGATE OF X_1')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03216(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03216.json"))
    write_center_svg(
        model_acute,
        here / "x-03216.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
