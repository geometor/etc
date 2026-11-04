"""GEOMETOR construction model for X_213 = X_6-CEVA CONJUGATE OF X_42."""

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


def construct_x_00213(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_213 = X_6-CEVA CONJUGATE OF X_42 on reference triangle ABC."""
    X_213 = eval_trilinear_point(model, A, B, C, '(b + c)*a**(2)', ID="X_213", classes=["selected", "target"])
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center", "incident"])
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center", "incident"])
    central_line(model, X_1, X_6, 1, 6, incident=True)
    X_31 = eval_trilinear_point(model, A, B, C, 'a**(2)', ID="X_31", classes=["center", "incident"])
    X_32 = eval_trilinear_point(model, A, B, C, 'a**(3)', ID="X_32", classes=["center", "incident"])
    central_line(model, X_31, X_32, 31, 32, incident=True)
    X_58 = eval_trilinear_point(model, A, B, C, 'a/(b + c)', ID="X_58", classes=["center", "incident"])
    X_101 = eval_trilinear_point(model, A, B, C, 'a/(b - c)', ID="X_101", classes=["center", "incident"])
    central_line(model, X_58, X_101, 58, 101, incident=True)
    return promote_point_to_top(model, X_213)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_213 on the given reference triangle."""
    model = create_model('X_213 = X_6-CEVA CONJUGATE OF X_42')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00213(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00213.json"))
    write_center_svg(
        model_acute,
        here / "x-00213.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
