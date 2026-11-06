"""GEOMETOR construction model for X_3731 = X_391com(EXCENTRAL TRIANGLE)."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_barycentric_point,
    eval_trilinear_point,
    incenter_of,
    promote_point_to_top,
    spieker_center_of,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_03731(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3731 = X_391com(EXCENTRAL TRIANGLE) on reference triangle ABC."""
    X_3731 = eval_barycentric_point(model, A, B, C, 'a*(a - 3*b - 3*c)', ID="X_3731", classes=["selected", "target"])
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center", "incident"])
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center", "incident"])
    central_line(model, X_1, X_6, 1, 6, incident=True)
    X_35 = eval_trilinear_point(model, A, B, C, '1 + 2*cos(A)', ID="X_35", classes=["center", "incident"])
    X_198 = eval_trilinear_point(model, A, B, C, '(a*(cos(B) + cos(C) - cos(A) - 1))', ID="X_198", classes=["center", "incident"])
    central_line(model, X_35, X_198, 35, 198, incident=True)
    X_10 = spieker_center_of(model, A, B, C, ID="X_10", classes=["center", "incident"])
    X_346 = eval_trilinear_point(model, A, B, C, 'b*c*(b + c - a)**(2)', ID="X_346", classes=["center", "incident"])
    central_line(model, X_10, X_346, 10, 346, incident=True)
    return promote_point_to_top(model, X_3731)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3731 on the given reference triangle."""
    model = create_model('X_3731 = X_391com(EXCENTRAL TRIANGLE)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03731(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03731.json"))
    write_center_svg(
        model_acute,
        here / "x-03731.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
