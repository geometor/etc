"""GEOMETOR construction model for X(48) = CROSSPOINT OF X(1) AND X(63)."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    circumcenter_of,
    circumcircle,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    incenter_of,
    promote_point_to_top,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_00048(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(48) = CROSSPOINT OF X(1) AND X(63) on reference triangle ABC."""
    circumcircle(model, A, B, C)
    X_1 = incenter_of(model, A, B, C, ID="X(1)", classes=["center"])
    X_19 = eval_trilinear_point(model, A, B, C, 'tan(A)', ID="X(19)", classes=["center"])
    central_line(model, X_1, X_19, 1, 19)
    X_6 = symmedian_point_of(model, A, B, C, ID="X(6)", classes=["center"])
    X_41 = eval_trilinear_point(model, A, B, C, 'a**(2)*(b + c - a)', ID="X(41)", classes=["center"])
    central_line(model, X_6, X_41, 6, 41)
    X_3 = circumcenter_of(model, A, B, C, ID="X(3)", classes=["center"])
    X_71 = eval_trilinear_point(model, A, B, C, '(b + c)*cos(A)', ID="X(71)", classes=["center"])
    central_line(model, X_3, X_71, 3, 71)
    X_48 = eval_trilinear_point(model, A, B, C, 'tan(B) + tan(C)', ID="X(48)", classes=["selected", "target"])
    return promote_point_to_top(model, X_48)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(48) on the given reference triangle."""
    model = create_model('X(48) = CROSSPOINT OF X(1) AND X(63)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00048(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00048.json"))
    write_center_svg(
        model_acute,
        here / "x-00048.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
