"""GEOMETOR construction model for X(949) = ISOGONAL CONJUGATE OF X(948)."""

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
    isogonal_conjugate,
    point_from_barycentrics,
    promote_point_to_top,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_00949(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(949) = ISOGONAL CONJUGATE OF X(948) on reference triangle ABC."""
    X_948 = point_from_barycentrics(model, A, B, C, 0.23303835, 0.29498525, 0.4719764, ID="X(948)", classes=["center"])
    X_949 = isogonal_conjugate(model, A, B, C, X_948, ID="X(949)", classes=["selected", "target"])
    X_3 = circumcenter_of(model, A, B, C, ID="X(3)", classes=["center", "incident"])
    X_41 = eval_trilinear_point(model, A, B, C, 'a**(2)*(b + c - a)', ID="X(41)", classes=["center", "incident"])
    central_line(model, X_3, X_41, 3, 41, incident=True)
    X_6 = symmedian_point_of(model, A, B, C, ID="X(6)", classes=["center", "incident"])
    X_77 = eval_trilinear_point(model, A, B, C, '1/(1 + sec(A))', ID="X(77)", classes=["center", "incident"])
    central_line(model, X_6, X_77, 6, 77, incident=True)
    X_2 = centroid_of(model, A, B, C, ID="X(2)", classes=["center", "incident"])
    X_294 = point_from_barycentrics(model, A, B, C, 0.10958904, 0.98630137, -0.095890411, ID="X(294)", classes=["center", "incident"])
    central_line(model, X_2, X_294, 2, 294, incident=True)
    return promote_point_to_top(model, X_949)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(949) on the given reference triangle."""
    model = create_model('X(949) = ISOGONAL CONJUGATE OF X(948)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00949(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00949.json"))
    write_center_svg(
        model_acute,
        here / "x-00949.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
