"""GEOMETOR construction model for X_1300 = COLLINGS TRANSFORM OF X_136."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    centroid_of,
    cevapoint,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    orthocenter_of,
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_01300(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1300 = COLLINGS TRANSFORM OF X_136 on reference triangle ABC."""
    X_4 = orthocenter_of(model, A, B, C, ID="X_4", classes=["center"])
    X_186 = eval_trilinear_point(model, A, B, C, '4*cos(A) - sec(A)', ID="X_186", classes=["center"])
    X_1300 = cevapoint(model, A, B, C, X_4, X_186, ID="X_1300", classes=["selected", "target"])
    X_110 = eval_trilinear_point(model, A, B, C, 'csc(B - C)', ID="X_110", classes=["center", "incident"])
    central_line(model, X_4, X_110, 4, 110, incident=True)
    X_24 = eval_trilinear_point(model, A, B, C, 'sec(A)*cos(2*A)', ID="X_24", classes=["center", "incident"])
    X_107 = eval_trilinear_point(model, A, B, C, '1/(cos(A)*(sin(2*B) - sin(2*C)))', ID="X_107", classes=["center", "incident"])
    central_line(model, X_24, X_107, 24, 107, incident=True)
    X_2 = centroid_of(model, A, B, C, ID="X_2", classes=["center", "incident"])
    X_131 = point_from_barycentrics(model, A, B, C, 0.57236082, 0.12379803, 0.30384114, ID="X_131", classes=["center", "incident"])
    central_line(model, X_2, X_131, 2, 131, incident=True)
    return promote_point_to_top(model, X_1300)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1300 on the given reference triangle."""
    model = create_model('X_1300 = COLLINGS TRANSFORM OF X_136')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01300(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01300.json"))
    write_center_svg(
        model_acute,
        here / "x-01300.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
