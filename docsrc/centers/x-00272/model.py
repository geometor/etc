"""GEOMETOR construction model for X(272) = ISOGONAL CONJUGATE OF X(209)."""

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
    isogonal_conjugate,
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00272(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(272) = ISOGONAL CONJUGATE OF X(209) on reference triangle ABC."""
    X_209 = point_from_barycentrics(model, A, B, C, -0.027151211, 0.26165414, 0.76549708, ID="X(209)", classes=["center"])
    X_272 = isogonal_conjugate(model, A, B, C, X_209, ID="X(272)", classes=["selected", "target"])
    X_7 = gergonne_point_of(model, A, B, C, ID="X(7)", classes=["center", "incident"])
    X_58 = eval_trilinear_point(model, A, B, C, 'a/(b + c)', ID="X(58)", classes=["center", "incident"])
    central_line(model, X_7, X_58, 7, 58, incident=True)
    X_21 = eval_trilinear_point(model, A, B, C, '1/(cos(B) + cos(C))', ID="X(21)", classes=["center", "incident"])
    X_75 = eval_trilinear_point(model, A, B, C, '1/a**(2)', ID="X(75)", classes=["center", "incident"])
    central_line(model, X_21, X_75, 21, 75, incident=True)
    X_60 = eval_trilinear_point(model, A, B, C, '1/(1 + cos(B - C))', ID="X(60)", classes=["center", "incident"])
    X_86 = eval_trilinear_point(model, A, B, C, 'b*c/(b + c)', ID="X(86)", classes=["center", "incident"])
    central_line(model, X_60, X_86, 60, 86, incident=True)
    return promote_point_to_top(model, X_272)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(272) on the given reference triangle."""
    model = create_model('X(272) = ISOGONAL CONJUGATE OF X(209)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00272(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00272.json"))
    write_center_svg(
        model_acute,
        here / "x-00272.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
