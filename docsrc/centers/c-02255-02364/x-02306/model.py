"""GEOMETOR construction model for X_2306 = X_2-ISOCONJUGATE OF X_1250."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    centroid_of,
    ceva_conjugate,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    incenter_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_02306(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2306 = X_2-ISOCONJUGATE OF X_1250 on reference triangle ABC."""
    X_1081 = eval_trilinear_point(model, A, B, C, 'sec(A/2)*csc(A/2 -  pi  /3)', ID="X_1081", classes=["center"])
    X_1251 = eval_trilinear_point(model, A, B, C, '(sin(A)*csc(A/2)*sec(A/2 +  pi  /6))', ID="X_1251", classes=["center"])
    X_2306 = ceva_conjugate(model, A, B, C, X_1081, X_1251, ID="X_2306", classes=["selected", "target"])
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center", "incident"])
    X_15 = eval_trilinear_point(model, A, B, C, 'sin(A +  pi  /3)', ID="X_15", classes=["center", "incident"])
    central_line(model, X_1, X_15, 1, 15, incident=True)
    X_13 = eval_trilinear_point(model, A, B, C, 'csc(A +  pi  /3)', ID="X_13", classes=["center", "incident"])
    X_79 = eval_trilinear_point(model, A, B, C, '1/(1 + 2*cos(A))', ID="X_79", classes=["center", "incident"])
    central_line(model, X_13, X_79, 13, 79, incident=True)
    X_2 = centroid_of(model, A, B, C, ID="X_2", classes=["center", "incident"])
    central_line(model, X_2, X_1081, 2, 1081, incident=True)
    return promote_point_to_top(model, X_2306)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2306 on the given reference triangle."""
    model = create_model('X_2306 = X_2-ISOCONJUGATE OF X_1250')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02306(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02306.json"))
    write_center_svg(
        model_acute,
        here / "x-02306.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
