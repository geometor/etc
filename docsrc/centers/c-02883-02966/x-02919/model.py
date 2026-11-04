"""GEOMETOR construction model for X_2919 = TANGENTIAL-ISOGONAL CONJUGATE OF X_7."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_02919(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2919 = TANGENTIAL-ISOGONAL CONJUGATE OF X_7 on reference triangle ABC."""
    X_2919 = point_from_barycentrics(model, A, B, C, 0.66849341, 0.56905682, -0.23755023, ID="X_2919", classes=["selected", "target"])
    X_22 = eval_trilinear_point(model, A, B, C, 'a*(b**(4) + c**(4) - a**(4))', ID="X_22", classes=["center", "incident"])
    X_1615 = point_from_barycentrics(model, A, B, C, 0.68037975, 0.66075949, -0.34113924, ID="X_1615", classes=["center", "incident"])
    central_line(model, X_22, X_1615, 22, 1615, incident=True)
    return promote_point_to_top(model, X_2919)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2919 on the given reference triangle."""
    model = create_model('X_2919 = TANGENTIAL-ISOGONAL CONJUGATE OF X_7')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02919(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02919.json"))
    write_center_svg(
        model_acute,
        here / "x-02919.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
