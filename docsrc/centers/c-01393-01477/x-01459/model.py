"""GEOMETOR construction model for X_1459 = X_521-BETH CONJUGATE OF X_521."""

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
    reflection_in_point,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_01459(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1459 = X_521-BETH CONJUGATE OF X_521 on reference triangle ABC."""
    X_656 = eval_trilinear_point(model, A, B, C, 'tan(B) - tan(C)', ID="X_656", classes=["center"])
    X_905 = eval_trilinear_point(model, A, B, C, '(b - c)*cot(A)', ID="X_905", classes=["center"])
    X_1459 = reflection_in_point(model, X_656, X_905, ID="X_1459", classes=["selected", "target"], guide=False)
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center", "incident"])
    X_522 = eval_trilinear_point(model, A, B, C, '(cos(B) - cos(C))*(csc(A))', ID="X_522", classes=["center", "incident"])
    central_line(model, X_1, X_522, 1, 522, incident=True)
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center", "incident"])
    X_657 = eval_trilinear_point(model, A, B, C, '(1 + cos(A))*(cos(B) - cos(C))', ID="X_657", classes=["center", "incident"])
    central_line(model, X_6, X_657, 6, 657, incident=True)
    X_242 = eval_trilinear_point(model, A, B, C, '((sec(A))*((sin(A))**(2) - sin(B)*sin(C)))', ID="X_242", classes=["center", "incident"])
    X_514 = eval_trilinear_point(model, A, B, C, '(b - c)/a', ID="X_514", classes=["center", "incident"])
    central_line(model, X_242, X_514, 242, 514, incident=True)
    return promote_point_to_top(model, X_1459)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1459 on the given reference triangle."""
    model = create_model('X_1459 = X_521-BETH CONJUGATE OF X_521')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01459(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01459.json"))
    write_center_svg(
        model_acute,
        here / "x-01459.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
