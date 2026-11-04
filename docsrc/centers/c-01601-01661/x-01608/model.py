"""GEOMETOR construction model for X_1608 = TCC-PERSPECTOR OF X_18."""

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


def construct_x_01608(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1608 = TCC-PERSPECTOR OF X_18 on reference triangle ABC."""
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center"])
    X_618 = point_from_barycentrics(model, A, B, C, 0.38507388, 0.34992883, 0.26499729, ID="X_618", classes=["center"])
    X_26 = eval_trilinear_point(model, A, B, C, 'a*(b**(2)*cos(2*B) + c**(2)*cos(2*C) - a**(2)*cos(2*A))', ID="X_26", classes=["center"])
    X_1606 = point_from_barycentrics(model, A, B, C, 0.46878519, 1.3979153, -0.86670046, ID="X_1606", classes=["center"])
    central_line(model, X_3, X_618, 3, 618)
    central_line(model, X_26, X_1606, 26, 1606)
    X_1608 = intersect_lines(model, X_3, X_618, X_26, X_1606, ID="X_1608", classes=["selected", "target"])
    return promote_point_to_top(model, X_1608)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1608 on the given reference triangle."""
    model = create_model('X_1608 = TCC-PERSPECTOR OF X_18')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01608(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01608.json"))
    write_center_svg(
        model_acute,
        here / "x-01608.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
