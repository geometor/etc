"""GEOMETOR construction model for X(352) = INVERSE-IN-CIRCUMCIRCLE OF X(353)."""

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
    promote_point_to_top,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_00352(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(352) = INVERSE-IN-CIRCUMCIRCLE OF X(353) on reference triangle ABC."""
    X_352 = eval_trilinear_point(model, A, B, C, 'a*(-a**(4)- b**(4)- c**(4)- 5*b**(2)*c**(2)+ 4*a**(2)*b**(2)+ 4*a**(2)*c**(2))', ID="X(352)", classes=["selected", "target"])
    X_2 = centroid_of(model, A, B, C, ID="X(2)", classes=["center", "incident"])
    X_6 = symmedian_point_of(model, A, B, C, ID="X(6)", classes=["center", "incident"])
    central_line(model, X_2, X_6, 2, 6, incident=True)
    X_110 = eval_trilinear_point(model, A, B, C, 'csc(B - C)', ID="X(110)", classes=["center", "incident"])
    X_187 = eval_trilinear_point(model, A, B, C, 'a*(2*a**(2) - b**(2) - c**(2))', ID="X(187)", classes=["center", "incident"])
    central_line(model, X_110, X_187, 110, 187, incident=True)
    X_3 = circumcenter_of(model, A, B, C, ID="X(3)", classes=["center", "incident"])
    X_353 = eval_trilinear_point(model, A, B, C, 'a*(4*a**(4)- 2*b**(4)- 2*c**(4)- b**(2)*c**(2)- 4*a**(2)*b**(2)-4*a**(2)*c**(2))', ID="X(353)", classes=["center", "incident"])
    central_line(model, X_3, X_353, 3, 353, incident=True)
    return promote_point_to_top(model, X_352)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(352) on the given reference triangle."""
    model = create_model('X(352) = INVERSE-IN-CIRCUMCIRCLE OF X(353)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00352(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00352.json"))
    write_center_svg(
        model_acute,
        here / "x-00352.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
