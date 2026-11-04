"""GEOMETOR construction model for X_1606 = TCC-PERSPECTOR OF X_14."""

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


def construct_x_01606(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1606 = TCC-PERSPECTOR OF X_14 on reference triangle ABC."""
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center"])
    X_619 = point_from_barycentrics(model, A, B, C, 0.419776, -0.015055849, 0.59527985, ID="X_619", classes=["center"])
    X_26 = eval_trilinear_point(model, A, B, C, 'a*(b**(2)*cos(2*B) + c**(2)*cos(2*C) - a**(2)*cos(2*A))', ID="X_26", classes=["center"])
    X_1608 = point_from_barycentrics(model, A, B, C, 1.1810413, 1.0963146, -1.2773558, ID="X_1608", classes=["center"])
    central_line(model, X_3, X_619, 3, 619)
    central_line(model, X_26, X_1608, 26, 1608)
    X_1606 = intersect_lines(model, X_3, X_619, X_26, X_1608, ID="X_1606", classes=["selected", "target"])
    return promote_point_to_top(model, X_1606)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1606 on the given reference triangle."""
    model = create_model('X_1606 = TCC-PERSPECTOR OF X_14')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01606(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01606.json"))
    write_center_svg(
        model_acute,
        here / "x-01606.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
