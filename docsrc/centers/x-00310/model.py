"""GEOMETOR construction model for X(310) = ISOTOMIC CONJUGATE OF X(42)."""

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
    isotomic_conjugate,
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00310(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(310) = ISOTOMIC CONJUGATE OF X(42) on reference triangle ABC."""
    X_42 = eval_trilinear_point(model, A, B, C, 'a*(b + c)', ID="X(42)", classes=["center"])
    X_310 = isotomic_conjugate(model, A, B, C, X_42, ID="X(310)", classes=["selected", "target"])
    X_2 = centroid_of(model, A, B, C, ID="X(2)", classes=["center", "incident"])
    X_39 = eval_trilinear_point(model, A, B, C, 'a*(b**(2) + c**(2))', ID="X(39)", classes=["center", "incident"])
    central_line(model, X_2, X_39, 2, 39, incident=True)
    X_38 = eval_trilinear_point(model, A, B, C, 'b**(2) + c**(2)', ID="X(38)", classes=["center", "incident"])
    X_75 = eval_trilinear_point(model, A, B, C, '1/a**(2)', ID="X(75)", classes=["center", "incident"])
    central_line(model, X_38, X_75, 38, 75, incident=True)
    X_261 = point_from_barycentrics(model, A, B, C, 0.38781404, 0.34135715, 0.27082881, ID="X(261)", classes=["center", "incident"])
    X_272 = point_from_barycentrics(model, A, B, C, 1.2803179, -0.19131188, -0.08900606, ID="X(272)", classes=["center", "incident"])
    central_line(model, X_261, X_272, 261, 272, incident=True)
    return promote_point_to_top(model, X_310)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(310) on the given reference triangle."""
    model = create_model('X(310) = ISOTOMIC CONJUGATE OF X(42)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00310(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00310.json"))
    write_center_svg(
        model_acute,
        here / "x-00310.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
