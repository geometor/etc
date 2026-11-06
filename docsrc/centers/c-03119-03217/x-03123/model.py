"""GEOMETOR construction model for X_3123 = DANNEELS PERSPECTOR FOR X_43."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    crosspoint,
    eval_trilinear_point,
    feuerbach_point_of,
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_03123(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3123 = DANNEELS PERSPECTOR FOR X_43 on reference triangle ABC."""
    X_75 = eval_trilinear_point(model, A, B, C, '1/a**(2)', ID="X_75", classes=["center"])
    X_513 = eval_trilinear_point(model, A, B, C, 'b - c', ID="X_513", classes=["center"])
    X_3123 = crosspoint(model, A, B, C, X_75, X_513, ID="X_3123", classes=["selected", "target"])
    X_11 = feuerbach_point_of(model, A, B, C, ID="X_11", classes=["center", "incident"])
    X_244 = eval_trilinear_point(model, A, B, C, '(b - c)**(2)', ID="X_244", classes=["center", "incident"])
    central_line(model, X_11, X_244, 11, 244, incident=True)
    X_38 = eval_trilinear_point(model, A, B, C, 'b**(2) + c**(2)', ID="X_38", classes=["center", "incident"])
    X_1227 = point_from_barycentrics(model, A, B, C, 0.58333333, 1.8875832e-16, 0.41666667, ID="X_1227", classes=["center", "incident"])
    central_line(model, X_38, X_1227, 38, 1227, incident=True)
    X_31 = eval_trilinear_point(model, A, B, C, 'a**(2)', ID="X_31", classes=["center", "incident"])
    X_1633 = eval_trilinear_point(model, A, B, C, '((a**(2) + b**(2) + c**(2) - 2*b*c)/(b - c))', ID="X_1633", classes=["center", "incident"])
    central_line(model, X_31, X_1633, 31, 1633, incident=True)
    return promote_point_to_top(model, X_3123)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3123 on the given reference triangle."""
    model = create_model('X_3123 = DANNEELS PERSPECTOR FOR X_43')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03123(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03123.json"))
    write_center_svg(
        model_acute,
        here / "x-03123.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
