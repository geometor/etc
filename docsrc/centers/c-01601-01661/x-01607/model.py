"""GEOMETOR construction model for X_1607 = TCC-PERSPECTOR OF X_17."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    circumcenter_of,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    intersect_lines,
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_01607(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1607 = TCC-PERSPECTOR OF X_17 on reference triangle ABC."""
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center"])
    X_619 = point_from_barycentrics(model, A, B, C, 0.419776, -0.015055849, 0.59527985, ID="X_619", classes=["center"])
    X_26 = eval_trilinear_point(model, A, B, C, 'a*(b**(2)*cos(2*B) + c**(2)*cos(2*C) - a**(2)*cos(2*A))', ID="X_26", classes=["center"])
    X_1605 = point_from_barycentrics(model, A, B, C, 0.24200161, 0.21576869, 0.54222969, ID="X_1605", classes=["center"])
    central_line(model, X_3, X_619, 3, 619)
    central_line(model, X_26, X_1605, 26, 1605)
    X_1607 = intersect_lines(model, X_3, X_619, X_26, X_1605, ID="X_1607", classes=["selected", "target"])
    return promote_point_to_top(model, X_1607)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1607 on the given reference triangle."""
    model = create_model('X_1607 = TCC-PERSPECTOR OF X_17')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01607(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01607.json"))
    write_center_svg(
        model_acute,
        here / "x-01607.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
