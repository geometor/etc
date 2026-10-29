"""GEOMETOR construction model for X(237) = X(3)-LINE CONJUGATE OF X(2)."""

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


def construct_x_00237(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(237) = X(3)-LINE CONJUGATE OF X(2) on reference triangle ABC."""
    X_237 = eval_trilinear_point(model, A, B, C, 'a**(2)*cos(A + omega )', ID="X(237)", classes=["selected", "target"])
    X_2 = centroid_of(model, A, B, C, ID="X(2)", classes=["center"])
    X_3 = circumcenter_of(model, A, B, C, ID="X(3)", classes=["center"])
    central_line(model, X_2, X_3, 2, 3)
    X_39 = eval_trilinear_point(model, A, B, C, 'a*(b**(2) + c**(2))', ID="X(39)", classes=["center", "incident"])
    X_51 = eval_trilinear_point(model, A, B, C, 'a**(2)*cos(B - C)', ID="X(51)", classes=["center", "incident"])
    central_line(model, X_39, X_51, 39, 51, incident=True)
    X_6 = symmedian_point_of(model, A, B, C, ID="X(6)", classes=["center", "incident"])
    X_160 = eval_trilinear_point(model, A, B, C, 'a*((b**(2)+ c**(2))*sin(2*A) + (c**(2)- a**(2))*sin(2*B) + (b**(2)- a**(2))*sin(2*C))', ID="X(160)", classes=["center", "incident"])
    central_line(model, X_6, X_160, 6, 160, incident=True)
    return promote_point_to_top(model, X_237)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(237) on the given reference triangle."""
    model = create_model('X(237) = X(3)-LINE CONJUGATE OF X(2)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00237(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00237.json"))
    write_center_svg(
        model_acute,
        here / "x-00237.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
