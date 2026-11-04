"""GEOMETOR construction model for X_2425 = ISOGONAL CONJUGATE OF X_2399."""

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
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_02425(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2425 = ISOGONAL CONJUGATE OF X_2399 on reference triangle ABC."""
    X_2399 = point_from_barycentrics(model, A, B, C, -0.98113208, 1.7169811, 0.26415094, ID="X_2399", classes=["center"])
    X_2425 = isogonal_conjugate(model, A, B, C, X_2399, ID="X_2425", classes=["selected", "target"])
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center", "incident"])
    X_41 = eval_trilinear_point(model, A, B, C, 'a**(2)*(b + c - a)', ID="X_41", classes=["center", "incident"])
    central_line(model, X_6, X_41, 6, 41, incident=True)
    X_2149 = eval_trilinear_point(model, A, B, C, '(sin(A))/(1 - cos(B - C))', ID="X_2149", classes=["center", "incident"])
    X_2427 = point_from_barycentrics(model, A, B, C, -0.83333333, 0.2, 1.6333333, ID="X_2427", classes=["center", "incident"])
    central_line(model, X_2149, X_2427, 2149, 2427, incident=True)
    return promote_point_to_top(model, X_2425)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2425 on the given reference triangle."""
    model = create_model('X_2425 = ISOGONAL CONJUGATE OF X_2399')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02425(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02425.json"))
    write_center_svg(
        model_acute,
        here / "x-02425.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
