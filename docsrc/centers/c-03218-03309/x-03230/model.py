"""GEOMETOR construction model for X_3230 = ISOGONAL CONJUGATE OF X_3227."""

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


def construct_x_03230(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3230 = ISOGONAL CONJUGATE OF X_3227 on reference triangle ABC."""
    X_3230 = eval_trilinear_point(model, A, B, C, '(a*(2*b*c - a*b - a*c))', ID="X_3230", classes=["selected", "target"])
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center", "incident"])
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center", "incident"])
    central_line(model, X_1, X_6, 1, 6, incident=True)
    X_106 = eval_trilinear_point(model, A, B, C, 'a/(2*a - b - c)', ID="X_106", classes=["center", "incident"])
    X_292 = eval_trilinear_point(model, A, B, C, 'a/(a**(2) - b*c)', ID="X_292", classes=["center", "incident"])
    central_line(model, X_106, X_292, 106, 292, incident=True)
    X_187 = eval_trilinear_point(model, A, B, C, 'a*(2*a**(2) - b**(2) - c**(2))', ID="X_187", classes=["center", "incident"])
    X_237 = eval_trilinear_point(model, A, B, C, 'a**(2)*cos(A +  omega  )', ID="X_237", classes=["center", "incident"])
    central_line(model, X_187, X_237, 187, 237, incident=True)
    return promote_point_to_top(model, X_3230)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3230 on the given reference triangle."""
    model = create_model('X_3230 = ISOGONAL CONJUGATE OF X_3227')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03230(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03230.json"))
    write_center_svg(
        model_acute,
        here / "x-03230.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
