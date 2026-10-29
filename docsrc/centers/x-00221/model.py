"""GEOMETOR construction model for X(221) = X(1)-CEVA CONJUGATE OF X(56)."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    incenter_of,
    promote_point_to_top,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_00221(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(221) = X(1)-CEVA CONJUGATE OF X(56) on reference triangle ABC."""
    X_221 = eval_trilinear_point(model, A, B, C, '(1 - cos(A))*(1 + cos(A) - cos(B) - cos(C))', ID="X(221)", classes=["selected", "target"])
    X_6 = symmedian_point_of(model, A, B, C, ID="X(6)", classes=["center", "incident"])
    X_19 = eval_trilinear_point(model, A, B, C, 'tan(A)', ID="X(19)", classes=["center", "incident"])
    central_line(model, X_6, X_19, 6, 19, incident=True)
    X_1 = incenter_of(model, A, B, C, ID="X(1)", classes=["center", "incident"])
    X_84 = eval_trilinear_point(model, A, B, C, '1/(cos(B) + cos(C) - cos(A) - 1)', ID="X(84)", classes=["center", "incident"])
    central_line(model, X_1, X_84, 1, 84, incident=True)
    X_31 = eval_trilinear_point(model, A, B, C, 'a**(2)', ID="X(31)", classes=["center", "incident"])
    X_56 = eval_trilinear_point(model, A, B, C, 'a/(b + c - a)', ID="X(56)", classes=["center", "incident"])
    central_line(model, X_31, X_56, 31, 56, incident=True)
    return promote_point_to_top(model, X_221)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(221) on the given reference triangle."""
    model = create_model('X(221) = X(1)-CEVA CONJUGATE OF X(56)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00221(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00221.json"))
    write_center_svg(
        model_acute,
        here / "x-00221.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
