"""GEOMETOR construction model for X(406) = EULER LINE INTERCEPT OF LINE X(10)X(33)."""

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
)
from geometor.etc.render import write_center_svg


def construct_x_00406(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(406) = EULER LINE INTERCEPT OF LINE X(10)X(33) on reference triangle ABC."""
    X_406 = eval_trilinear_point(model, A, B, C, 'b*c*(a + b + c) + a*b*c*sec(A)', ID="X(406)", classes=["selected", "target"])
    X_2 = centroid_of(model, A, B, C, ID="X(2)", classes=["center"])
    X_3 = circumcenter_of(model, A, B, C, ID="X(3)", classes=["center"])
    central_line(model, X_2, X_3, 2, 3)
    X_10 = spieker_center_of(model, A, B, C, ID="X(10)", classes=["center", "incident"])
    X_33 = eval_trilinear_point(model, A, B, C, '1 + sec(A)', ID="X(33)", classes=["center", "incident"])
    central_line(model, X_10, X_33, 10, 33, incident=True)
    X_37 = eval_trilinear_point(model, A, B, C, 'b + c', ID="X(37)", classes=["center", "incident"])
    X_158 = point_from_barycentrics(model, A, B, C, 0.04776757, 0.099240104, 0.85299233, ID="X(158)", classes=["center", "incident"])
    central_line(model, X_37, X_158, 37, 158, incident=True)
    return promote_point_to_top(model, X_406)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(406) on the given reference triangle."""
    model = create_model('X(406) = EULER LINE INTERCEPT OF LINE X(10)X(33)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00406(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00406.json"))
    write_center_svg(
        model_acute,
        here / "x-00406.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
