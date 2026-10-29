"""GEOMETOR construction model for X(596) = ISOGONAL CONJUGATE OF X(595)."""

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
    spieker_center_of,
)
from geometor.etc.render import write_center_svg


def construct_x_00596(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(596) = ISOGONAL CONJUGATE OF X(595) on reference triangle ABC."""
    X_595 = eval_trilinear_point(model, A, B, C, 'r + R*(cos(2*A) - 1)', ID="X(595)", classes=["center"])
    X_596 = isogonal_conjugate(model, A, B, C, X_595, ID="X(596)", classes=["selected", "target"])
    X_10 = spieker_center_of(model, A, B, C, ID="X(10)", classes=["center", "incident"])
    X_38 = eval_trilinear_point(model, A, B, C, 'b**(2) + c**(2)', ID="X(38)", classes=["center", "incident"])
    central_line(model, X_10, X_38, 10, 38, incident=True)
    X_37 = eval_trilinear_point(model, A, B, C, 'b + c', ID="X(37)", classes=["center", "incident"])
    X_39 = eval_trilinear_point(model, A, B, C, 'a*(b**(2) + c**(2))', ID="X(39)", classes=["center", "incident"])
    central_line(model, X_37, X_39, 37, 39, incident=True)
    X_58 = eval_trilinear_point(model, A, B, C, 'a/(b + c)', ID="X(58)", classes=["center", "incident"])
    X_82 = eval_trilinear_point(model, A, B, C, '1/(b**(2) + c**(2))', ID="X(82)", classes=["center", "incident"])
    central_line(model, X_58, X_82, 58, 82, incident=True)
    return promote_point_to_top(model, X_596)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(596) on the given reference triangle."""
    model = create_model('X(596) = ISOGONAL CONJUGATE OF X(595)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00596(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00596.json"))
    write_center_svg(
        model_acute,
        here / "x-00596.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
