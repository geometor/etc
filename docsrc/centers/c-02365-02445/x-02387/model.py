"""GEOMETOR construction model for X_2387 = ISOGONAL CONJUGATE OF X_2367."""

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
)
from geometor.etc.render import write_center_svg


def construct_x_02387(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2387 = ISOGONAL CONJUGATE OF X_2367 on reference triangle ABC."""
    X_2367 = point_from_barycentrics(model, A, B, C, 0.52646516, 1.0797677, -0.60623286, ID="X_2367", classes=["center"])
    X_2387 = isogonal_conjugate(model, A, B, C, X_2367, ID="X_2387", classes=["selected", "target"])
    X_32 = eval_trilinear_point(model, A, B, C, 'a**(3)', ID="X_32", classes=["center", "incident"])
    X_184 = eval_trilinear_point(model, A, B, C, 'a**(2)*cos(A)', ID="X_184", classes=["center", "incident"])
    central_line(model, X_32, X_184, 32, 184, incident=True)
    X_30 = eval_trilinear_point(model, A, B, C, 'cos(A) - 2*cos(B)*cos(C)', ID="X_30", classes=["center", "incident"])
    X_511 = eval_trilinear_point(model, A, B, C, 'cos(A +  omega  )', ID="X_511", classes=["center", "incident"])
    central_line(model, X_30, X_511, 30, 511, incident=True)
    return promote_point_to_top(model, X_2387)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2387 on the given reference triangle."""
    model = create_model('X_2387 = ISOGONAL CONJUGATE OF X_2367')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02387(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02387.json"))
    write_center_svg(
        model_acute,
        here / "x-02387.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
