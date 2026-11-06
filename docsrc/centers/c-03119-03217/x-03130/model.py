"""GEOMETOR construction model for X_3130 = X_14-CEVA CONJUGATE OF X_6."""

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
)
from geometor.etc.render import write_center_svg


def construct_x_03130(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3130 = X_14-CEVA CONJUGATE OF X_6 on reference triangle ABC."""
    X_2993 = point_from_barycentrics(model, A, B, C, 0.34130203, 0.94673925, -0.28804128, ID="X_2993", classes=["center"])
    X_3130 = isogonal_conjugate(model, A, B, C, X_2993, ID="X_3130", classes=["selected", "target"])
    X_2 = centroid_of(model, A, B, C, ID="X_2", classes=["center"])
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center"])
    central_line(model, X_2, X_3, 2, 3)
    X_51 = eval_trilinear_point(model, A, B, C, 'a**(2)*cos(B - C)', ID="X_51", classes=["center", "incident"])
    X_61 = eval_trilinear_point(model, A, B, C, 'sin(A +  pi  /6)', ID="X_61", classes=["center", "incident"])
    central_line(model, X_51, X_61, 51, 61, incident=True)
    X_62 = eval_trilinear_point(model, A, B, C, 'sin(A -  pi  /6)', ID="X_62", classes=["center", "incident"])
    X_184 = eval_trilinear_point(model, A, B, C, 'a**(2)*cos(A)', ID="X_184", classes=["center", "incident"])
    central_line(model, X_62, X_184, 62, 184, incident=True)
    return promote_point_to_top(model, X_3130)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3130 on the given reference triangle."""
    model = create_model('X_3130 = X_14-CEVA CONJUGATE OF X_6')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03130(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03130.json"))
    write_center_svg(
        model_acute,
        here / "x-03130.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
