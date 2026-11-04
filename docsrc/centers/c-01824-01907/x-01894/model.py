"""GEOMETOR construction model for X_1894 = ZOSMA TRANSFORM OF X_993."""

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
    eval_trilinear_point,
    intersect_lines,
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_01894(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1894 = ZOSMA TRANSFORM OF X_993 on reference triangle ABC."""
    X_2 = centroid_of(model, A, B, C, ID="X_2", classes=["center"])
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center"])
    X_19 = eval_trilinear_point(model, A, B, C, 'tan(A)', ID="X_19", classes=["center"])
    X_53 = eval_trilinear_point(model, A, B, C, 'tan(A)*cos(B - C)', ID="X_53", classes=["center"])
    central_line(model, X_2, X_3, 2, 3)
    central_line(model, X_19, X_53, 19, 53)
    X_1894 = intersect_lines(model, X_2, X_3, X_19, X_53, ID="X_1894", classes=["selected", "target"])
    X_225 = eval_trilinear_point(model, A, B, C, '(sec(A))*(cos(B) + cos(C))', ID="X_225", classes=["center", "incident"])
    X_1829 = point_from_barycentrics(model, A, B, C, 0.10770975, 0.19863946, 0.69365079, ID="X_1829", classes=["center", "incident"])
    central_line(model, X_225, X_1829, 225, 1829, incident=True)
    return promote_point_to_top(model, X_1894)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1894 on the given reference triangle."""
    model = create_model('X_1894 = ZOSMA TRANSFORM OF X_993')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01894(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01894.json"))
    write_center_svg(
        model_acute,
        here / "x-01894.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
