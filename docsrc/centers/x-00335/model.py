"""GEOMETOR construction model for X(335) = ISOTOMIC CONJUGATE OF X(239)."""

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
    isotomic_conjugate,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00335(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(335) = ISOTOMIC CONJUGATE OF X(239) on reference triangle ABC."""
    X_239 = eval_trilinear_point(model, A, B, C, 'b*c*(a**(2) - b*c)', ID="X(239)", classes=["center"])
    X_335 = isotomic_conjugate(model, A, B, C, X_239, ID="X(335)", classes=["selected", "target"])
    X_2 = centroid_of(model, A, B, C, ID="X(2)", classes=["center", "incident"])
    X_38 = eval_trilinear_point(model, A, B, C, 'b**(2) + c**(2)', ID="X(38)", classes=["center", "incident"])
    central_line(model, X_2, X_38, 2, 38, incident=True)
    X_37 = eval_trilinear_point(model, A, B, C, 'b + c', ID="X(37)", classes=["center", "incident"])
    X_86 = eval_trilinear_point(model, A, B, C, 'b*c/(b + c)', ID="X(86)", classes=["center", "incident"])
    central_line(model, X_37, X_86, 37, 86, incident=True)
    X_7 = gergonne_point_of(model, A, B, C, ID="X(7)", classes=["center", "incident"])
    X_192 = eval_trilinear_point(model, A, B, C, 'b*c*(c*a + a*b - b*c)', ID="X(192)", classes=["center", "incident"])
    central_line(model, X_7, X_192, 7, 192, incident=True)
    return promote_point_to_top(model, X_335)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(335) on the given reference triangle."""
    model = create_model('X(335) = ISOTOMIC CONJUGATE OF X(239)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00335(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00335.json"))
    write_center_svg(
        model_acute,
        here / "x-00335.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
