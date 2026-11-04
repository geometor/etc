"""GEOMETOR construction model for X_1803 = INVERSE MIMOSA TRANSFORM OF X_218."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_barycentric_point,
    eval_trilinear_point,
    intersect_lines,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_01803(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1803 = INVERSE MIMOSA TRANSFORM OF X_218 on reference triangle ABC."""
    X_41 = eval_trilinear_point(model, A, B, C, 'a**(2)*(b + c - a)', ID="X_41", classes=["center"])
    X_57 = eval_trilinear_point(model, A, B, C, '1/(b + c - a)', ID="X_57", classes=["center"])
    X_35 = eval_trilinear_point(model, A, B, C, '1 + 2*cos(A)', ID="X_35", classes=["center"])
    X_103 = eval_trilinear_point(model, A, B, C, 'a/((a - b)*cot(C) + (a - c)*cot(B))', ID="X_103", classes=["center"])
    central_line(model, X_41, X_57, 41, 57)
    central_line(model, X_35, X_103, 35, 103)
    X_1803 = intersect_lines(model, X_41, X_57, X_35, X_103, ID="X_1803", classes=["selected", "target"])
    X_58 = eval_trilinear_point(model, A, B, C, 'a/(b + c)', ID="X_58", classes=["center", "incident"])
    X_1458 = eval_barycentric_point(model, A, B, C, 'a**(2)*(b**(2) + c**(2) - a*b - a*c)/(a - b - c)', ID="X_1458", classes=["center", "incident"])
    central_line(model, X_58, X_1458, 58, 1458, incident=True)
    return promote_point_to_top(model, X_1803)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1803 on the given reference triangle."""
    model = create_model('X_1803 = INVERSE MIMOSA TRANSFORM OF X_218')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01803(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01803.json"))
    write_center_svg(
        model_acute,
        here / "x-01803.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
