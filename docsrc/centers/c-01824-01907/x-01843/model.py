"""GEOMETOR construction model for X_1843 = ZOSMA TRANSFORM OF X_75."""

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
    orthocenter_of,
    promote_point_to_top,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_01843(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1843 = ZOSMA TRANSFORM OF X_75 on reference triangle ABC."""
    X_1799 = eval_trilinear_point(model, A, B, C, 'cot(A)*csc(A + omega )', ID="X_1799", classes=["center"])
    X_1843 = isogonal_conjugate(model, A, B, C, X_1799, ID="X_1843", classes=["selected", "target"])
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center", "incident"])
    X_25 = eval_trilinear_point(model, A, B, C, 'sin(A)*tan(A)', ID="X_25", classes=["center", "incident"])
    central_line(model, X_6, X_25, 6, 25, incident=True)
    X_4 = orthocenter_of(model, A, B, C, ID="X_4", classes=["center", "incident"])
    X_69 = eval_trilinear_point(model, A, B, C, '(cos(A))/a**(2)', ID="X_69", classes=["center", "incident"])
    central_line(model, X_4, X_69, 4, 69, incident=True)
    X_24 = eval_trilinear_point(model, A, B, C, 'sec(A)*cos(2*A)', ID="X_24", classes=["center", "incident"])
    X_182 = eval_trilinear_point(model, A, B, C, 'cos(A- omega )', ID="X_182", classes=["center", "incident"])
    central_line(model, X_24, X_182, 24, 182, incident=True)
    return promote_point_to_top(model, X_1843)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1843 on the given reference triangle."""
    model = create_model('X_1843 = ZOSMA TRANSFORM OF X_75')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01843(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01843.json"))
    write_center_svg(
        model_acute,
        here / "x-01843.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
