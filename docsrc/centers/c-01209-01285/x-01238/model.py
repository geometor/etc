"""GEOMETOR construction model for X_1238 = ISOTOMIC CONJUGATE OF X_1179."""

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
    isotomic_conjugate,
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_01238(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1238 = ISOTOMIC CONJUGATE OF X_1179 on reference triangle ABC."""
    X_1179 = point_from_barycentrics(model, A, B, C, 0.088343284, 0.17113976, 0.74051696, ID="X_1179", classes=["center"])
    X_1238 = isotomic_conjugate(model, A, B, C, X_1179, ID="X_1238", classes=["selected", "target"])
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center", "incident"])
    X_69 = eval_trilinear_point(model, A, B, C, '(cos(A))/a**(2)', ID="X_69", classes=["center", "incident"])
    central_line(model, X_3, X_69, 3, 69, incident=True)
    X_311 = eval_trilinear_point(model, A, B, C, '(csc(A))**(2)*cos(B - C)', ID="X_311", classes=["center", "incident"])
    X_325 = eval_trilinear_point(model, A, B, C, '(csc(A))**(2)', ID="X_325", classes=["center", "incident"])
    central_line(model, X_311, X_325, 311, 325, incident=True)
    X_1232 = point_from_barycentrics(model, A, B, C, 0.47795093, 0.32307014, 0.19897893, ID="X_1232", classes=["center", "incident"])
    X_1273 = point_from_barycentrics(model, A, B, C, 1.9099368, 0.24319357, -1.1531304, ID="X_1273", classes=["center", "incident"])
    central_line(model, X_1232, X_1273, 1232, 1273, incident=True)
    return promote_point_to_top(model, X_1238)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1238 on the given reference triangle."""
    model = create_model('X_1238 = ISOTOMIC CONJUGATE OF X_1179')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01238(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01238.json"))
    write_center_svg(
        model_acute,
        here / "x-01238.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
