"""GEOMETOR construction model for X(1000) = ISOGONAL CONJUGATE OF X(999)."""

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
    nagel_point_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_01000(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(1000) = ISOGONAL CONJUGATE OF X(999) on reference triangle ABC."""
    X_999 = eval_trilinear_point(model, A, B, C, '2 - cos(A)', ID="X(999)", classes=["center"])
    X_1000 = isogonal_conjugate(model, A, B, C, X_999, ID="X(1000)", classes=["selected", "target"])
    X_55 = eval_trilinear_point(model, A, B, C, 'a*(b + c - a)', ID="X(55)", classes=["center", "incident"])
    X_104 = eval_trilinear_point(model, A, B, C, '1/(-1 + cos(B) + cos(C))', ID="X(104)", classes=["center", "incident"])
    central_line(model, X_55, X_104, 55, 104, incident=True)
    X_21 = eval_trilinear_point(model, A, B, C, '1/(cos(B) + cos(C))', ID="X(21)", classes=["center", "incident"])
    X_145 = eval_trilinear_point(model, A, B, C, 'b*c*(3*a - b - c)', ID="X(145)", classes=["center", "incident"])
    central_line(model, X_21, X_145, 21, 145, incident=True)
    X_8 = nagel_point_of(model, A, B, C, ID="X(8)", classes=["center", "incident"])
    X_392 = eval_trilinear_point(model, A, B, C, '(b + c)*(b**(2) + c**(2) - a**(2)) + 4*a*b*c', ID="X(392)", classes=["center", "incident"])
    central_line(model, X_8, X_392, 8, 392, incident=True)
    return promote_point_to_top(model, X_1000)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(1000) on the given reference triangle."""
    model = create_model('X(1000) = ISOGONAL CONJUGATE OF X(999)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01000(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01000.json"))
    write_center_svg(
        model_acute,
        here / "x-01000.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
