"""GEOMETOR construction model for X_2436 = ISOGONAL CONJUGATE OF X_2410."""

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
    isogonal_conjugate,
    point_from_barycentrics,
    promote_point_to_top,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_02436(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2436 = ISOGONAL CONJUGATE OF X_2410 on reference triangle ABC."""
    X_2410 = point_from_barycentrics(model, A, B, C, -0.036475453, 2.0347099, -0.99823447, ID="X_2410", classes=["center"])
    X_2436 = isogonal_conjugate(model, A, B, C, X_2410, ID="X_2436", classes=["selected", "target"])
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center", "incident"])
    X_1637 = eval_barycentric_point(model, A, B, C, 'tan(A)*(tan(B) - tan(C))*(tan(B) + tan(C) - 2*tan(A))', ID="X_1637", classes=["center", "incident"])
    central_line(model, X_6, X_1637, 6, 1637, incident=True)
    X_323 = eval_trilinear_point(model, A, B, C, 'sin(3*A)*(csc(A))**(2)', ID="X_323", classes=["center", "incident"])
    X_2411 = point_from_barycentrics(model, A, B, C, 0.98172677, -0.017599034, 0.035872262, ID="X_2411", classes=["center", "incident"])
    central_line(model, X_323, X_2411, 323, 2411, incident=True)
    return promote_point_to_top(model, X_2436)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2436 on the given reference triangle."""
    model = create_model('X_2436 = ISOGONAL CONJUGATE OF X_2410')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02436(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02436.json"))
    write_center_svg(
        model_acute,
        here / "x-02436.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
