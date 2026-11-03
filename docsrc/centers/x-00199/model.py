"""GEOMETOR construction model for X_199 = X_10-CEVA CONJUGATE OF X_6."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    centroid_of,
    ceva_conjugate,
    circumcenter_of,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    promote_point_to_top,
    spieker_center_of,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_00199(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_199 = X_10-CEVA CONJUGATE OF X_6 on reference triangle ABC."""
    X_10 = spieker_center_of(model, A, B, C, ID="X_10", classes=["center"])
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center"])
    X_199 = ceva_conjugate(model, A, B, C, X_10, X_6, ID="X_199", classes=["selected", "target"])
    X_2 = centroid_of(model, A, B, C, ID="X_2", classes=["center"])
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center"])
    central_line(model, X_2, X_3, 2, 3)
    X_42 = eval_trilinear_point(model, A, B, C, 'a*(b + c)', ID="X_42", classes=["center", "incident"])
    X_172 = eval_trilinear_point(model, A, B, C, 'a**(3) + a*b*c', ID="X_172", classes=["center", "incident"])
    central_line(model, X_42, X_172, 42, 172, incident=True)
    X_51 = eval_trilinear_point(model, A, B, C, 'a**(2)*cos(B - C)', ID="X_51", classes=["center", "incident"])
    X_572 = eval_trilinear_point(model, A, B, C, 's*cos(A) + r*sin(A)', ID="X_572", classes=["center", "incident"])
    central_line(model, X_51, X_572, 51, 572, incident=True)
    return promote_point_to_top(model, X_199)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_199 on the given reference triangle."""
    model = create_model('X_199 = X_10-CEVA CONJUGATE OF X_6')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00199(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00199.json"))
    write_center_svg(
        model_acute,
        here / "x-00199.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
