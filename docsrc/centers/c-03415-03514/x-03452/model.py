"""GEOMETOR construction model for X_3452 = ISOGONAL CONJUGATE OF X_3451."""

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
    feuerbach_point_of,
    gergonne_point_of,
    nine_point_center_of,
    promote_point_to_top,
    reflection_in_point,
    spieker_center_of,
)
from geometor.etc.render import write_center_svg


def construct_x_03452(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3452 = ISOGONAL CONJUGATE OF X_3451 on reference triangle ABC."""
    X_999 = eval_trilinear_point(model, A, B, C, '2 - cos(A)', ID="X_999", classes=["center"])
    X_1125 = eval_trilinear_point(model, A, B, C, '(2*a+b+c)/a', ID="X_1125", classes=["center"])
    X_3452 = reflection_in_point(model, X_999, X_1125, ID="X_3452", classes=["selected", "target"], guide=False)
    X_2 = centroid_of(model, A, B, C, ID="X_2", classes=["center", "incident"])
    X_7 = gergonne_point_of(model, A, B, C, ID="X_7", classes=["center", "incident"])
    central_line(model, X_2, X_7, 2, 7, incident=True)
    X_5 = nine_point_center_of(model, A, B, C, ID="X_5", classes=["center", "incident"])
    X_10 = spieker_center_of(model, A, B, C, ID="X_10", classes=["center", "incident"])
    central_line(model, X_5, X_10, 5, 10, incident=True)
    X_11 = feuerbach_point_of(model, A, B, C, ID="X_11", classes=["center", "incident"])
    X_210 = eval_trilinear_point(model, A, B, C, '(b + c)*(b + c - a)', ID="X_210", classes=["center", "incident"])
    central_line(model, X_11, X_210, 11, 210, incident=True)
    return promote_point_to_top(model, X_3452)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3452 on the given reference triangle."""
    model = create_model('X_3452 = ISOGONAL CONJUGATE OF X_3451')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03452(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03452.json"))
    write_center_svg(
        model_acute,
        here / "x-03452.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
