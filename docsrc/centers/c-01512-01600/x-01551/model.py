"""GEOMETOR construction model for X_1551 = ORTHOJOIN OF X_111."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    centroid_of,
    circumcenter_of,
    construct_baseline_triangle,
    create_model,
    eval_barycentric_point,
    intersect_lines,
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_01551(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1551 = ORTHOJOIN OF X_111 on reference triangle ABC."""
    X_2 = centroid_of(model, A, B, C, ID="X_2", classes=["center"])
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center"])
    X_542 = eval_barycentric_point(model, A, B, C, '2*a**(6) - 2*a**(4)*(b**(2) + c**(2)) + a**(2)*(b**(4) + c**(4)) - (b**(2) - c**(2))**(2)*(b**(2) + c**(2))', ID="X_542", classes=["center"])
    X_1550 = point_from_barycentrics(model, A, B, C, 0.0088389953, 0.81060307, 0.18055794, ID="X_1550", classes=["center"])
    central_line(model, X_2, X_3, 2, 3)
    central_line(model, X_542, X_1550, 542, 1550)
    X_1551 = intersect_lines(model, X_2, X_3, X_542, X_1550, ID="X_1551", classes=["selected", "target"])
    return promote_point_to_top(model, X_1551)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1551 on the given reference triangle."""
    model = create_model('X_1551 = ORTHOJOIN OF X_111')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01551(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01551.json"))
    write_center_svg(
        model_acute,
        here / "x-01551.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
