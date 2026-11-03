"""GEOMETOR construction model for X_172 = TRILINEAR PRODUCT X_6*X_171."""

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


def construct_x_00172(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_172 = TRILINEAR PRODUCT X_6*X_171 on reference triangle ABC."""
    X_172 = eval_trilinear_point(model, A, B, C, 'a**(3) + a*b*c', ID="X_172", classes=["selected", "target"])
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center", "incident"])
    X_32 = eval_trilinear_point(model, A, B, C, 'a**(3)', ID="X_32", classes=["center", "incident"])
    central_line(model, X_1, X_32, 1, 32, incident=True)
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center", "incident"])
    X_41 = eval_trilinear_point(model, A, B, C, 'a**(2)*(b + c - a)', ID="X_41", classes=["center", "incident"])
    central_line(model, X_6, X_41, 6, 41, incident=True)
    X_21 = eval_trilinear_point(model, A, B, C, '1/(cos(B) + cos(C))', ID="X_21", classes=["center", "incident"])
    X_37 = eval_trilinear_point(model, A, B, C, 'b + c', ID="X_37", classes=["center", "incident"])
    central_line(model, X_21, X_37, 21, 37, incident=True)
    return promote_point_to_top(model, X_172)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_172 on the given reference triangle."""
    model = create_model('X_172 = TRILINEAR PRODUCT X_6*X_171')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00172(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00172.json"))
    write_center_svg(
        model_acute,
        here / "x-00172.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
