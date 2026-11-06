"""GEOMETOR construction model for X_3002 = (BROCARD AXIS)∩(GERGONNE LINE)."""

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
    intersect_lines,
    promote_point_to_top,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_03002(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3002 = (BROCARD AXIS)∩(GERGONNE LINE) on reference triangle ABC."""
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center"])
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center"])
    X_241 = eval_trilinear_point(model, A, B, C, '(cos(B/2))**(4) - ((cos(A/2))**(2))*((cos(B/2))**(2) +(cos(C/2))**(2)) + (cos(C/2))**(4)', ID="X_241", classes=["center"])
    X_514 = eval_trilinear_point(model, A, B, C, '(b - c)/a', ID="X_514", classes=["center"])
    central_line(model, X_3, X_6, 3, 6)
    central_line(model, X_241, X_514, 241, 514)
    X_3002 = intersect_lines(model, X_3, X_6, X_241, X_514, ID="X_3002", classes=["selected", "target"])
    X_36 = eval_trilinear_point(model, A, B, C, '1 - 2*cos(A)', ID="X_36", classes=["center", "incident"])
    X_1951 = eval_trilinear_point(model, A, B, C, 'a*((cos(A))**(2) - cos(B)*cos(C))', ID="X_1951", classes=["center", "incident"])
    central_line(model, X_36, X_1951, 36, 1951, incident=True)
    return promote_point_to_top(model, X_3002)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3002 on the given reference triangle."""
    model = create_model('X_3002 = (BROCARD AXIS)∩(GERGONNE LINE)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03002(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03002.json"))
    write_center_svg(
        model_acute,
        here / "x-03002.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
