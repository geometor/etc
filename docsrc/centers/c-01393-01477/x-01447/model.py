"""GEOMETOR construction model for X_1447 = X_350-BETH CONJUGATE OF X_350."""

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
    gergonne_point_of,
    intersect_lines,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_01447(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1447 = X_350-BETH CONJUGATE OF X_350 on reference triangle ABC."""
    X_2 = centroid_of(model, A, B, C, ID="X_2", classes=["center"])
    X_7 = gergonne_point_of(model, A, B, C, ID="X_7", classes=["center"])
    X_56 = eval_trilinear_point(model, A, B, C, 'a/(b + c - a)', ID="X_56", classes=["center"])
    X_85 = eval_trilinear_point(model, A, B, C, 'b**(2)*c**(2)/(b + c - a)', ID="X_85", classes=["center"])
    central_line(model, X_2, X_7, 2, 7)
    central_line(model, X_56, X_85, 56, 85)
    X_1447 = intersect_lines(model, X_2, X_7, X_56, X_85, ID="X_1447", classes=["selected", "target"])
    X_75 = eval_trilinear_point(model, A, B, C, '1/a**(2)', ID="X_75", classes=["center", "incident"])
    X_183 = eval_trilinear_point(model, A, B, C, 'b**(2)*c**(2)*cos(A-  omega  )', ID="X_183", classes=["center", "incident"])
    central_line(model, X_75, X_183, 75, 183, incident=True)
    return promote_point_to_top(model, X_1447)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1447 on the given reference triangle."""
    model = create_model('X_1447 = X_350-BETH CONJUGATE OF X_350')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01447(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01447.json"))
    write_center_svg(
        model_acute,
        here / "x-01447.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
