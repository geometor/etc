"""GEOMETOR construction model for X(502) = ISOGONAL CONJUGATE OF X(501)."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    isogonal_conjugate,
    point_from_barycentrics,
    promote_point_to_top,
    spieker_center_of,
)
from geometor.etc.render import write_center_svg


def construct_x_00502(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(502) = ISOGONAL CONJUGATE OF X(501) on reference triangle ABC."""
    X_501 = point_from_barycentrics(model, A, B, C, 0.35136356, 0.37986486, 0.26877158, ID="X(501)", classes=["center"])
    X_502 = isogonal_conjugate(model, A, B, C, X_501, ID="X(502)", classes=["selected", "target"])
    X_10 = spieker_center_of(model, A, B, C, ID="X(10)", classes=["center", "incident"])
    X_191 = eval_trilinear_point(model, A, B, C, '(b + c - a)*(b*c + c*a + a*b) + b**(3) + c**(3) - a**(3)', ID="X(191)", classes=["center", "incident"])
    central_line(model, X_10, X_191, 10, 191, incident=True)
    return promote_point_to_top(model, X_502)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(502) on the given reference triangle."""
    model = create_model('X(502) = ISOGONAL CONJUGATE OF X(501)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00502(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00502.json"))
    write_center_svg(
        model_acute,
        here / "x-00502.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
