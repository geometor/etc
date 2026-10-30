"""GEOMETOR construction model for X(638) = ANTICOMPLEMENT OF X(372)."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    anticomplement,
    central_line,
    centroid_of,
    circumcenter_of,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    orthocenter_of,
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00638(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(638) = ANTICOMPLEMENT OF X(372) on reference triangle ABC."""
    X_372 = eval_trilinear_point(model, A, B, C, 'cos(A + pi /4)', ID="X(372)", classes=["center"])
    X_638 = anticomplement(model, A, B, C, X_372, ID="X(638)", classes=["selected", "target"])
    X_4 = orthocenter_of(model, A, B, C, ID="X(4)", classes=["center", "incident"])
    X_69 = eval_trilinear_point(model, A, B, C, '(cos(A))/a**(2)', ID="X(69)", classes=["center", "incident"])
    central_line(model, X_4, X_69, 4, 69, incident=True)
    X_2 = centroid_of(model, A, B, C, ID="X(2)", classes=["center", "incident"])
    central_line(model, X_2, X_372, 2, 372, incident=True)
    X_3 = circumcenter_of(model, A, B, C, ID="X(3)", classes=["center", "incident"])
    X_490 = point_from_barycentrics(model, A, B, C, 0.61185907, 0.42830629, -0.040165363, ID="X(490)", classes=["center", "incident"])
    central_line(model, X_3, X_490, 3, 490, incident=True)
    return promote_point_to_top(model, X_638)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(638) on the given reference triangle."""
    model = create_model('X(638) = ANTICOMPLEMENT OF X(372)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00638(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00638.json"))
    write_center_svg(
        model_acute,
        here / "x-00638.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
