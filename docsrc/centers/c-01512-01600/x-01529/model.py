"""GEOMETOR construction model for X_1529 = ORTHOJOIN OF X_25."""

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


def construct_x_01529(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1529 = ORTHOJOIN OF X_25 on reference triangle ABC."""
    X_2 = centroid_of(model, A, B, C, ID="X_2", classes=["center"])
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center"])
    X_132 = point_from_barycentrics(model, A, B, C, 0.11002416, 0.049913231, 0.84006261, ID="X_132", classes=["center"])
    X_1503 = eval_trilinear_point(model, A, B, C, 'sin(A)*tan(omega)  - 2*cos(B)*cos(C)', ID="X_1503", classes=["center"])
    central_line(model, X_2, X_3, 2, 3)
    central_line(model, X_132, X_1503, 132, 1503)
    X_1529 = intersect_lines(model, X_2, X_3, X_132, X_1503, ID="X_1529", classes=["selected", "target"])
    return promote_point_to_top(model, X_1529)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1529 on the given reference triangle."""
    model = create_model('X_1529 = ORTHOJOIN OF X_25')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01529(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01529.json"))
    write_center_svg(
        model_acute,
        here / "x-01529.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
