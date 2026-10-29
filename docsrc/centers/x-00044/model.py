"""GEOMETOR construction model for X(44) = -LINE CONJUGATE OF X(1)."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    centroid_of,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    incenter_of,
    promote_point_to_top,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_00044(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(44) = -LINE CONJUGATE OF X(1) on reference triangle ABC."""
    X_1 = incenter_of(model, A, B, C, ID="X(1)", classes=["center"])
    X_6 = symmedian_point_of(model, A, B, C, ID="X(6)", classes=["center"])
    central_line(model, X_1, X_6, 1, 6)
    X_2 = centroid_of(model, A, B, C, ID="X(2)", classes=["center"])
    X_89 = eval_trilinear_point(model, A, B, C, '1/(2*b + 2*c - a)', ID="X(89)", classes=["center"])
    central_line(model, X_2, X_89, 2, 89)
    X_44 = eval_trilinear_point(model, A, B, C, 'b + c - 2*a', ID="X(44)", classes=["selected", "target"])
    return promote_point_to_top(model, X_44)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(44) on the given reference triangle."""
    model = create_model('X(44) = -LINE CONJUGATE OF X(1)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00044(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00044.json"))
    write_center_svg(
        model_acute,
        here / "x-00044.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
