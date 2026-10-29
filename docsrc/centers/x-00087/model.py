"""GEOMETOR construction model for X(87) = -CROSS CONJUGATE OF X(1)."""

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


def construct_x_00087(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(87) = -CROSS CONJUGATE OF X(1) on reference triangle ABC."""
    X_6 = symmedian_point_of(model, A, B, C, ID="X(6)", classes=["center"])
    X_43 = eval_trilinear_point(model, A, B, C, 'a*b + a*c - b*c', ID="X(43)", classes=["center"])
    central_line(model, X_6, X_43, 6, 43)
    X_87 = isogonal_conjugate(model, A, B, C, X_43, ID="X(87)", classes=["selected", "target"])
    return promote_point_to_top(model, X_87)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(87) on the given reference triangle."""
    model = create_model('X(87) = -CROSS CONJUGATE OF X(1)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00087(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00087.json"))
    write_center_svg(
        model_acute,
        here / "x-00087.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
