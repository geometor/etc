"""GEOMETOR construction model for X(319) = ISOTOMIC CONJUGATE OF X(79)."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    gergonne_point_of,
    nagel_point_of,
    promote_point_to_top,
    spieker_center_of,
)
from geometor.etc.render import write_center_svg


def construct_x_00319(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(319) = ISOTOMIC CONJUGATE OF X(79) on reference triangle ABC."""
    X_319 = eval_trilinear_point(model, A, B, C, '(1 + 2*cos(A))/a**(2)', ID="X(319)", classes=["selected", "target"])
    X_7 = gergonne_point_of(model, A, B, C, ID="X(7)", classes=["center", "incident"])
    X_8 = nagel_point_of(model, A, B, C, ID="X(8)", classes=["center", "incident"])
    central_line(model, X_7, X_8, 7, 8, incident=True)
    X_10 = spieker_center_of(model, A, B, C, ID="X(10)", classes=["center", "incident"])
    X_86 = eval_trilinear_point(model, A, B, C, 'b*c/(b + c)', ID="X(86)", classes=["center", "incident"])
    central_line(model, X_10, X_86, 10, 86, incident=True)
    X_141 = eval_trilinear_point(model, A, B, C, 'b*c*(b**(2) + c**(2))', ID="X(141)", classes=["center", "incident"])
    X_239 = eval_trilinear_point(model, A, B, C, 'b*c*(a**(2) - b*c)', ID="X(239)", classes=["center", "incident"])
    central_line(model, X_141, X_239, 141, 239, incident=True)
    return promote_point_to_top(model, X_319)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(319) on the given reference triangle."""
    model = create_model('X(319) = ISOTOMIC CONJUGATE OF X(79)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00319(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00319.json"))
    write_center_svg(
        model_acute,
        here / "x-00319.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
