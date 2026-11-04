"""GEOMETOR construction model for X_2049 = EULER LINE INTERCEPT OF LINE X_6X_10."""

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
    point_from_barycentrics,
    promote_point_to_top,
    spieker_center_of,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_02049(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2049 = EULER LINE INTERCEPT OF LINE X_6X_10 on reference triangle ABC."""
    X_2049 = eval_trilinear_point(model, A, B, C, '((s**(2) - r**(2))*cos(A) + (s**(2) + r**(2))*cos(B - C))', ID="X_2049", classes=["selected", "target"])
    X_2 = centroid_of(model, A, B, C, ID="X_2", classes=["center"])
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center"])
    central_line(model, X_2, X_3, 2, 3)
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center", "incident"])
    X_10 = spieker_center_of(model, A, B, C, ID="X_10", classes=["center", "incident"])
    central_line(model, X_6, X_10, 6, 10, incident=True)
    X_12 = eval_trilinear_point(model, A, B, C, '1 + cos(B - C)', ID="X_12", classes=["center", "incident"])
    X_1460 = point_from_barycentrics(model, A, B, C, 0.16086235, 0.28656716, 0.55257048, ID="X_1460", classes=["center", "incident"])
    central_line(model, X_12, X_1460, 12, 1460, incident=True)
    return promote_point_to_top(model, X_2049)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2049 on the given reference triangle."""
    model = create_model('X_2049 = EULER LINE INTERCEPT OF LINE X_6X_10')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02049(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02049.json"))
    write_center_svg(
        model_acute,
        here / "x-02049.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
