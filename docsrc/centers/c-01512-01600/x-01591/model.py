"""GEOMETOR construction model for X_1591 = POINT CHARA III."""

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
)
from geometor.etc.render import write_center_svg


def construct_x_01591(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1591 = POINT CHARA III on reference triangle ABC."""
    X_1591 = eval_trilinear_point(model, A, B, C, '(csc(A) + cos(B - C))', ID="X_1591", classes=["selected", "target"])
    X_2 = centroid_of(model, A, B, C, ID="X_2", classes=["center"])
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center"])
    central_line(model, X_2, X_3, 2, 3)
    X_394 = eval_trilinear_point(model, A, B, C, 'cos(A)*cot(A)', ID="X_394", classes=["center", "incident"])
    X_485 = eval_trilinear_point(model, A, B, C, 'sec(A - pi /4)', ID="X_485", classes=["center", "incident"])
    central_line(model, X_394, X_485, 394, 485, incident=True)
    X_343 = eval_trilinear_point(model, A, B, C, 'cot(A)*cos(B - C)', ID="X_343", classes=["center", "incident"])
    X_639 = point_from_barycentrics(model, A, B, C, 0.35035787, 0.32442401, 0.32521812, ID="X_639", classes=["center", "incident"])
    central_line(model, X_343, X_639, 343, 639, incident=True)
    return promote_point_to_top(model, X_1591)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1591 on the given reference triangle."""
    model = create_model('X_1591 = POINT CHARA III')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01591(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01591.json"))
    write_center_svg(
        model_acute,
        here / "x-01591.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
