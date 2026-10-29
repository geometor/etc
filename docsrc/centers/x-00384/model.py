"""GEOMETOR construction model for X(384) = THE CONWAY POINT: EULER LINE INTERCEPT OF LINE X(32)X(76)."""

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
)
from geometor.etc.render import write_center_svg


def construct_x_00384(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(384) = THE CONWAY POINT: EULER LINE INTERCEPT OF LINE X(32)X(76) on reference triangle ABC."""
    X_384 = eval_trilinear_point(model, A, B, C, 'b*c*(a**(4) + b**(2)*c**(2))', ID="X(384)", classes=["selected", "target"])
    X_2 = centroid_of(model, A, B, C, ID="X(2)", classes=["center"])
    X_3 = circumcenter_of(model, A, B, C, ID="X(3)", classes=["center"])
    central_line(model, X_2, X_3, 2, 3)
    X_32 = eval_trilinear_point(model, A, B, C, 'a**(3)', ID="X(32)", classes=["center", "incident"])
    X_76 = eval_trilinear_point(model, A, B, C, '1/a**(3)', ID="X(76)", classes=["center", "incident"])
    central_line(model, X_32, X_76, 32, 76, incident=True)
    X_39 = eval_trilinear_point(model, A, B, C, 'a*(b**(2) + c**(2))', ID="X(39)", classes=["center", "incident"])
    X_83 = eval_trilinear_point(model, A, B, C, 'b*c/(b**(2) + c**(2))', ID="X(83)", classes=["center", "incident"])
    central_line(model, X_39, X_83, 39, 83, incident=True)
    return promote_point_to_top(model, X_384)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(384) on the given reference triangle."""
    model = create_model('X(384) = THE CONWAY POINT: EULER LINE INTERCEPT OF LINE X(32)X(76)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00384(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00384.json"))
    write_center_svg(
        model_acute,
        here / "x-00384.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
