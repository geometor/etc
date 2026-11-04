"""GEOMETOR construction model for X_1440 = X_309-BETH CONJUGATE OF X_309."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    centroid_of,
    cevapoint,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    gergonne_point_of,
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_01440(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1440 = X_309-BETH CONJUGATE OF X_309 on reference triangle ABC."""
    X_84 = eval_trilinear_point(model, A, B, C, '1/(cos(B) + cos(C) - cos(A) - 1)', ID="X_84", classes=["center"])
    X_1422 = point_from_barycentrics(model, A, B, C, -0.022661722, -0.056036259, 1.078698, ID="X_1422", classes=["center"])
    X_1440 = cevapoint(model, A, B, C, X_84, X_1422, ID="X_1440", classes=["selected", "target"])
    X_2 = centroid_of(model, A, B, C, ID="X_2", classes=["center", "incident"])
    X_77 = eval_trilinear_point(model, A, B, C, '1/(1 + sec(A))', ID="X_77", classes=["center", "incident"])
    central_line(model, X_2, X_77, 2, 77, incident=True)
    X_7 = gergonne_point_of(model, A, B, C, ID="X_7", classes=["center", "incident"])
    central_line(model, X_7, X_84, 7, 84, incident=True)
    X_75 = eval_trilinear_point(model, A, B, C, '1/a**(2)', ID="X_75", classes=["center", "incident"])
    X_280 = eval_trilinear_point(model, A, B, C, '((csc(A/2))**(2))/(-1 - cos(A) + cos(B) + cos(C))', ID="X_280", classes=["center", "incident"])
    central_line(model, X_75, X_280, 75, 280, incident=True)
    return promote_point_to_top(model, X_1440)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1440 on the given reference triangle."""
    model = create_model('X_1440 = X_309-BETH CONJUGATE OF X_309')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01440(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01440.json"))
    write_center_svg(
        model_acute,
        here / "x-01440.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
