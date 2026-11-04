"""GEOMETOR construction model for X_2050 = {X_3,X_5}-HARMONIC CONJUGATE OF X_2049."""

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
    feuerbach_point_of,
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_02050(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2050 = {X_3,X_5}-HARMONIC CONJUGATE OF X_2049 on reference triangle ABC."""
    X_2050 = eval_trilinear_point(model, A, B, C, '((s**(2) - r**(2))*cos(A) - (s**(2) + r**(2))*cos(B - C))', ID="X_2050", classes=["selected", "target"])
    X_2 = centroid_of(model, A, B, C, ID="X_2", classes=["center"])
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center"])
    central_line(model, X_2, X_3, 2, 3)
    X_11 = feuerbach_point_of(model, A, B, C, ID="X_11", classes=["center", "incident"])
    X_1460 = point_from_barycentrics(model, A, B, C, 0.16086235, 0.28656716, 0.55257048, ID="X_1460", classes=["center", "incident"])
    central_line(model, X_11, X_1460, 11, 1460, incident=True)
    X_171 = eval_trilinear_point(model, A, B, C, 'a**(2) + b*c', ID="X_171", classes=["center", "incident"])
    X_1699 = eval_trilinear_point(model, A, B, C, '2*cos(B - C) - cos(A) + cos(B) + cos(C) - 1', ID="X_1699", classes=["center", "incident"])
    central_line(model, X_171, X_1699, 171, 1699, incident=True)
    return promote_point_to_top(model, X_2050)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2050 on the given reference triangle."""
    model = create_model('X_2050 = {X_3,X_5}-HARMONIC CONJUGATE OF X_2049')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02050(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02050.json"))
    write_center_svg(
        model_acute,
        here / "x-02050.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
