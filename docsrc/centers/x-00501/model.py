"""GEOMETOR construction model for X(501) = MIQUEL ASSOCIATE OF INCENTER."""

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
    intersect_lines,
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00501(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(501) = MIQUEL ASSOCIATE OF INCENTER on reference triangle ABC."""
    X_36 = eval_trilinear_point(model, A, B, C, '1 - 2*cos(A)', ID="X(36)", classes=["center"])
    X_58 = eval_trilinear_point(model, A, B, C, 'a/(b + c)', ID="X(58)", classes=["center"])
    X_35 = eval_trilinear_point(model, A, B, C, '1 + 2*cos(A)', ID="X(35)", classes=["center"])
    X_110 = eval_trilinear_point(model, A, B, C, 'csc(B - C)', ID="X(110)", classes=["center"])
    central_line(model, X_36, X_58, 36, 58)
    central_line(model, X_35, X_110, 35, 110)
    X_501 = intersect_lines(model, X_36, X_58, X_35, X_110, ID="X(501)", classes=["selected", "target"])
    X_1 = incenter_of(model, A, B, C, ID="X(1)", classes=["center", "incident"])
    X_229 = point_from_barycentrics(model, A, B, C, 0.21061481, 0.29086323, 0.49852195, ID="X(229)", classes=["center", "incident"])
    central_line(model, X_1, X_229, 1, 229, incident=True)
    return promote_point_to_top(model, X_501)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(501) on the given reference triangle."""
    model = create_model('X(501) = MIQUEL ASSOCIATE OF INCENTER')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00501(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00501.json"))
    write_center_svg(
        model_acute,
        here / "x-00501.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
