"""GEOMETOR construction model for X_1978 = TRILINEAR PRODUCT OF PU(41)."""

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


def construct_x_01978(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1978 = TRILINEAR PRODUCT OF PU(41) on reference triangle ABC."""
    X_1919 = eval_trilinear_point(model, A, B, C, '(a**(3)*(b - c))', ID="X_1919", classes=["center"])
    X_1978 = isogonal_conjugate(model, A, B, C, X_1919, ID="X_1978", classes=["selected", "target"])
    X_75 = eval_trilinear_point(model, A, B, C, '1/a**(2)', ID="X_75", classes=["center", "incident"])
    X_244 = eval_trilinear_point(model, A, B, C, '(b - c)**(2)', ID="X_244", classes=["center", "incident"])
    central_line(model, X_75, X_244, 75, 244, incident=True)
    X_310 = eval_trilinear_point(model, A, B, C, 'b**(3)*c**(3)/(b + c)', ID="X_310", classes=["center", "incident"])
    X_321 = eval_trilinear_point(model, A, B, C, '(b + c)*b**(2)*c**(2)', ID="X_321", classes=["center", "incident"])
    central_line(model, X_310, X_321, 310, 321, incident=True)
    X_101 = eval_trilinear_point(model, A, B, C, 'a/(b - c)', ID="X_101", classes=["center", "incident"])
    X_689 = eval_trilinear_point(model, A, B, C, '1/(a**(3)*(b**(4) - c**(4)))', ID="X_689", classes=["center", "incident"])
    central_line(model, X_101, X_689, 101, 689, incident=True)
    return promote_point_to_top(model, X_1978)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1978 on the given reference triangle."""
    model = create_model('X_1978 = TRILINEAR PRODUCT OF PU(41)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01978(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01978.json"))
    write_center_svg(
        model_acute,
        here / "x-01978.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
