"""GEOMETOR construction model for X(186) = INVERSE-IN-CIRCUMCIRCLE OF X(4)."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    centroid_of,
    circumcenter_of,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00186(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(186) = INVERSE-IN-CIRCUMCIRCLE OF X(4) on reference triangle ABC."""
    X_186 = eval_trilinear_point(model, A, B, C, '4*cos(A) - sec(A)', ID="X(186)", classes=["selected", "target"])
    X_2 = centroid_of(model, A, B, C, ID="X(2)", classes=["center"])
    X_3 = circumcenter_of(model, A, B, C, ID="X(3)", classes=["center"])
    central_line(model, X_2, X_3, 2, 3)
    X_112 = eval_trilinear_point(model, A, B, C, 'a/(sin(2*B) - sin(2*C))', ID="X(112)", classes=["center", "incident"])
    X_187 = eval_trilinear_point(model, A, B, C, 'a*(2*a**(2) - b**(2) - c**(2))', ID="X(187)", classes=["center", "incident"])
    central_line(model, X_112, X_187, 112, 187, incident=True)
    X_93 = eval_trilinear_point(model, A, B, C, 'sec(3*A)', ID="X(93)", classes=["center", "incident"])
    X_252 = point_from_barycentrics(model, A, B, C, 0.46254977, 0.32862274, 0.20882749, ID="X(252)", classes=["center", "incident"])
    central_line(model, X_93, X_252, 93, 252, incident=True)
    return promote_point_to_top(model, X_186)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(186) on the given reference triangle."""
    model = create_model('X(186) = INVERSE-IN-CIRCUMCIRCLE OF X(4)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00186(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00186.json"))
    write_center_svg(
        model_acute,
        here / "x-00186.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
