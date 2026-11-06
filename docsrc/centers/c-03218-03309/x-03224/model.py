"""GEOMETOR construction model for X_3224 = ISOGONAL CONJUGATE OF X_194."""

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
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_03224(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3224 = ISOGONAL CONJUGATE OF X_194 on reference triangle ABC."""
    X_194 = eval_trilinear_point(model, A, B, C, 'b*c*(a**(2)*b**(2) + a**(2)*c**(2) - b**(2)*c**(2))', ID="X_194", classes=["center"])
    X_3224 = isogonal_conjugate(model, A, B, C, X_194, ID="X_3224", classes=["selected", "target"])
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center", "incident"])
    central_line(model, X_6, X_194, 6, 194, incident=True)
    X_43 = eval_trilinear_point(model, A, B, C, 'a*b + a*c - b*c', ID="X_43", classes=["center", "incident"])
    X_213 = eval_trilinear_point(model, A, B, C, '(b + c)*a**(2)', ID="X_213", classes=["center", "incident"])
    central_line(model, X_43, X_213, 43, 213, incident=True)
    X_32 = eval_trilinear_point(model, A, B, C, 'a**(3)', ID="X_32", classes=["center", "incident"])
    X_1613 = eval_trilinear_point(model, A, B, C, '(a*(b**(2)*c**(2) - c**(2)*a**(2) - a**(2)*b**(2)))', ID="X_1613", classes=["center", "incident"])
    central_line(model, X_32, X_1613, 32, 1613, incident=True)
    return promote_point_to_top(model, X_3224)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3224 on the given reference triangle."""
    model = create_model('X_3224 = ISOGONAL CONJUGATE OF X_194')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03224(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03224.json"))
    write_center_svg(
        model_acute,
        here / "x-03224.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
