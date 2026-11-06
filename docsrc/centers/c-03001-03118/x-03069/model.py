"""GEOMETOR construction model for X_3069 = INTERSECTION OF X_2X_6 AND X_4X_372."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    centroid_of,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    isogonal_conjugate,
    orthocenter_of,
    point_from_barycentrics,
    promote_point_to_top,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_03069(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3069 = INTERSECTION OF X_2X_6 AND X_4X_372 on reference triangle ABC."""
    X_494 = eval_trilinear_point(model, A, B, C, '1/(sin(A) - sin(B)*sin(C))', ID="X_494", classes=["center"])
    X_3069 = isogonal_conjugate(model, A, B, C, X_494, ID="X_3069", classes=["selected", "target"])
    X_2 = centroid_of(model, A, B, C, ID="X_2", classes=["center", "incident"])
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center", "incident"])
    central_line(model, X_2, X_6, 2, 6, incident=True)
    X_4 = orthocenter_of(model, A, B, C, ID="X_4", classes=["center", "incident"])
    X_372 = eval_trilinear_point(model, A, B, C, 'cos(A +  pi  /4)', ID="X_372", classes=["center", "incident"])
    central_line(model, X_4, X_372, 4, 372, incident=True)
    X_32 = eval_trilinear_point(model, A, B, C, 'a**(3)', ID="X_32", classes=["center", "incident"])
    X_637 = point_from_barycentrics(model, A, B, C, 0.40143148, 0.29769606, 0.30087247, ID="X_637", classes=["center", "incident"])
    central_line(model, X_32, X_637, 32, 637, incident=True)
    return promote_point_to_top(model, X_3069)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3069 on the given reference triangle."""
    model = create_model('X_3069 = INTERSECTION OF X_2X_6 AND X_4X_372')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03069(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03069.json"))
    write_center_svg(
        model_acute,
        here / "x-03069.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
