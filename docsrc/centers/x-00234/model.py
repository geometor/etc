"""GEOMETOR construction model for X(234) = X(7)-CEVA CONJUGATE OF X(177)."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    centroid_of,
    ceva_conjugate,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    gergonne_point_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00234(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(234) = X(7)-CEVA CONJUGATE OF X(177) on reference triangle ABC."""
    X_7 = gergonne_point_of(model, A, B, C, ID="X(7)", classes=["center"])
    X_177 = eval_trilinear_point(model, A, B, C, '(cos(B/2) + cos(C/2))*sec(A/2)', ID="X(177)", classes=["center"])
    X_234 = ceva_conjugate(model, A, B, C, X_7, X_177, ID="X(234)", classes=["selected", "target"])
    X_2 = centroid_of(model, A, B, C, ID="X(2)", classes=["center", "incident"])
    X_178 = eval_trilinear_point(model, A, B, C, '(cos(B/2) + cos(C/2))*csc(A)', ID="X(178)", classes=["center", "incident"])
    central_line(model, X_2, X_178, 2, 178, incident=True)
    X_174 = eval_trilinear_point(model, A, B, C, 'sec(A/2)', ID="X(174)", classes=["center", "incident"])
    central_line(model, X_7, X_174, 7, 174, incident=True)
    X_57 = eval_trilinear_point(model, A, B, C, '1/(b + c - a)', ID="X(57)", classes=["center", "incident"])
    X_362 = eval_trilinear_point(model, A, B, C, 'b*cos(B/2) + c*cos(C/2) - a*cos(A/2)', ID="X(362)", classes=["center", "incident"])
    central_line(model, X_57, X_362, 57, 362, incident=True)
    return promote_point_to_top(model, X_234)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(234) on the given reference triangle."""
    model = create_model('X(234) = X(7)-CEVA CONJUGATE OF X(177)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00234(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00234.json"))
    write_center_svg(
        model_acute,
        here / "x-00234.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
