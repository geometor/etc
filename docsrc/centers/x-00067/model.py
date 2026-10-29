"""GEOMETOR construction model for X(67) = ISOGONAL CONJUGATE OF X(23)."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    circumcircle,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    isogonal_conjugate,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00067(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(67) = ISOGONAL CONJUGATE OF X(23) on reference triangle ABC."""
    circumcircle(model, A, B, C)
    X_23 = eval_trilinear_point(model, A, B, C, 'a*(b**(4) + c**(4) - a**(4) - b**(2)*c**(2))', ID="X(23)", classes=["center"])
    X_67 = isogonal_conjugate(model, A, B, C, X_23, ID="X(67)", classes=["selected", "target"])
    return promote_point_to_top(model, X_67)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(67) on the given reference triangle."""
    model = create_model('X(67) = ISOGONAL CONJUGATE OF X(23)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00067(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00067.json"))
    write_center_svg(
        model_acute,
        here / "x-00067.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
