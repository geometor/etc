"""GEOMETOR construction model for X_2957 = EXCENTRAL-ISOGONAL CONJUGATE OF X_100."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    ceva_conjugate,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    feuerbach_point_of,
    incenter_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_02957(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2957 = EXCENTRAL-ISOGONAL CONJUGATE OF X_100 on reference triangle ABC."""
    X_11 = feuerbach_point_of(model, A, B, C, ID="X_11", classes=["center"])
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center"])
    X_2957 = ceva_conjugate(model, A, B, C, X_11, X_1, ID="X_2957", classes=["selected", "target"])
    X_59 = eval_trilinear_point(model, A, B, C, '1/(1 - cos(B - C))', ID="X_59", classes=["center", "incident"])
    central_line(model, X_1, X_59, 1, 59, incident=True)
    X_238 = eval_trilinear_point(model, A, B, C, 'a**(2) - b*c', ID="X_238", classes=["center", "incident"])
    X_517 = eval_trilinear_point(model, A, B, C, '-1 + cos(B) + cos(C)', ID="X_517", classes=["center", "incident"])
    central_line(model, X_238, X_517, 238, 517, incident=True)
    X_484 = eval_trilinear_point(model, A, B, C, '1 + 2*(cos(A) - cos(B) - cos(C))', ID="X_484", classes=["center", "incident"])
    X_516 = eval_trilinear_point(model, A, B, C, 'b*c*((a - b)*cot(C) + (a - c)*cot(B))', ID="X_516", classes=["center", "incident"])
    central_line(model, X_484, X_516, 484, 516, incident=True)
    return promote_point_to_top(model, X_2957)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2957 on the given reference triangle."""
    model = create_model('X_2957 = EXCENTRAL-ISOGONAL CONJUGATE OF X_100')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02957(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02957.json"))
    write_center_svg(
        model_acute,
        here / "x-02957.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
