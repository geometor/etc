"""GEOMETOR construction model for X(662) = TRILINEAR POLE OF LINE X(1)X(21)."""

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
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00662(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(662) = TRILINEAR POLE OF LINE X(1)X(21) on reference triangle ABC."""
    X_661 = eval_trilinear_point(model, A, B, C, 'cot(B) - cot(C)', ID="X(661)", classes=["center"])
    X_662 = isogonal_conjugate(model, A, B, C, X_661, ID="X(662)", classes=["selected", "target"])
    X_48 = eval_trilinear_point(model, A, B, C, 'tan(B) + tan(C)', ID="X(48)", classes=["center", "incident"])
    X_75 = eval_trilinear_point(model, A, B, C, '1/a**(2)', ID="X(75)", classes=["center", "incident"])
    central_line(model, X_48, X_75, 48, 75, incident=True)
    X_81 = eval_trilinear_point(model, A, B, C, '1/(b + c)', ID="X(81)", classes=["center", "incident"])
    X_88 = eval_trilinear_point(model, A, B, C, '1/(b + c - 2*a)', ID="X(88)", classes=["center", "incident"])
    central_line(model, X_81, X_88, 81, 88, incident=True)
    X_99 = eval_trilinear_point(model, A, B, C, 'b*c/(b**(2) - c**(2))', ID="X(99)", classes=["center", "incident"])
    X_101 = eval_trilinear_point(model, A, B, C, 'a/(b - c)', ID="X(101)", classes=["center", "incident"])
    central_line(model, X_99, X_101, 99, 101, incident=True)
    return promote_point_to_top(model, X_662)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(662) on the given reference triangle."""
    model = create_model('X(662) = TRILINEAR POLE OF LINE X(1)X(21)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00662(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00662.json"))
    write_center_svg(
        model_acute,
        here / "x-00662.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
