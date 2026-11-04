"""GEOMETOR construction model for X_2922 = TANGENTIAL-ISOGONAL CONJUGATE OF X_10."""

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


def construct_x_02922(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2922 = TANGENTIAL-ISOGONAL CONJUGATE OF X_10 on reference triangle ABC."""
    X_2922 = point_from_barycentrics(model, A, B, C, 0.51364743, 0.47241407, 0.013938504, ID="X_2922", classes=["selected", "target"])
    X_22 = eval_trilinear_point(model, A, B, C, 'a*(b**(4) + c**(4) - a**(4))', ID="X_22", classes=["center", "incident"])
    X_595 = eval_trilinear_point(model, A, B, C, 'r + R*(cos(2*A) - 1)', ID="X_595", classes=["center", "incident"])
    central_line(model, X_22, X_595, 22, 595, incident=True)
    return promote_point_to_top(model, X_2922)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2922 on the given reference triangle."""
    model = create_model('X_2922 = TANGENTIAL-ISOGONAL CONJUGATE OF X_10')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02922(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02922.json"))
    write_center_svg(
        model_acute,
        here / "x-02922.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
