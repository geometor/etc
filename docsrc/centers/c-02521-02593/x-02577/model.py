"""GEOMETOR construction model for X_2577 = X_2-ISOCONJUGATE OF X_2575."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    incenter_of,
    intersect_lines,
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_02577(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2577 = X_2-ISOCONJUGATE OF X_2575 on reference triangle ABC."""
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center"])
    X_19 = eval_trilinear_point(model, A, B, C, 'tan(A)', ID="X_19", classes=["center"])
    X_101 = eval_trilinear_point(model, A, B, C, 'a/(b - c)', ID="X_101", classes=["center"])
    X_1114 = eval_trilinear_point(model, A, B, C, '(R + d)*cos(A) - 2*R*cos(B)*cos(C)', ID="X_1114", classes=["center"])
    central_line(model, X_1, X_19, 1, 19)
    central_line(model, X_101, X_1114, 101, 1114)
    X_2577 = intersect_lines(model, X_1, X_19, X_101, X_1114, ID="X_2577", classes=["selected", "target"])
    X_163 = eval_trilinear_point(model, A, B, C, '(sin(2*A))/(sin(2*B) - sin(2*C))', ID="X_163", classes=["center", "incident"])
    X_1823 = point_from_barycentrics(model, A, B, C, 0.72123578, 0.4152025, -0.13643829, ID="X_1823", classes=["center", "incident"])
    central_line(model, X_163, X_1823, 163, 1823, incident=True)
    return promote_point_to_top(model, X_2577)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2577 on the given reference triangle."""
    model = create_model('X_2577 = X_2-ISOCONJUGATE OF X_2575')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02577(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02577.json"))
    write_center_svg(
        model_acute,
        here / "x-02577.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
