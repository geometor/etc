"""GEOMETOR construction model for X(375) = CENTROID OF THE PEDAL TRIANGLE OF X(10)."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    midpoint,
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00375(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(375) = CENTROID OF THE PEDAL TRIANGLE OF X(10) on reference triangle ABC."""
    X_51 = eval_trilinear_point(model, A, B, C, 'a**(2)*cos(B - C)', ID="X(51)", classes=["center"])
    X_210 = eval_trilinear_point(model, A, B, C, '(b + c)*(b + c - a)', ID="X(210)", classes=["center"])
    X_375 = midpoint(model, X_51, X_210, ID="X(375)", classes=["selected", "target"], guide=False)
    X_44 = eval_trilinear_point(model, A, B, C, 'b + c - 2*a', ID="X(44)", classes=["center", "incident"])
    X_181 = eval_trilinear_point(model, A, B, C, 'a*(b + c)**(2)/(b + c - a)', ID="X(181)", classes=["center", "incident"])
    central_line(model, X_44, X_181, 44, 181, incident=True)
    central_line(model, X_51, X_210, 51, 210, incident=True)
    X_354 = eval_trilinear_point(model, A, B, C, '(b - c)**(2) - a*b - a*c', ID="X(354)", classes=["center", "incident"])
    X_373 = point_from_barycentrics(model, A, B, C, 0.28382464, 0.3169161, 0.39925926, ID="X(373)", classes=["center", "incident"])
    central_line(model, X_354, X_373, 354, 373, incident=True)
    return promote_point_to_top(model, X_375)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(375) on the given reference triangle."""
    model = create_model('X(375) = CENTROID OF THE PEDAL TRIANGLE OF X(10)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00375(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00375.json"))
    write_center_svg(
        model_acute,
        here / "x-00375.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
