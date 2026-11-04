"""GEOMETOR construction model for X_1063 = ISOGONAL CONJUGATE OF X_1062."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    incenter_of,
    isogonal_conjugate,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_01063(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1063 = ISOGONAL CONJUGATE OF X_1062 on reference triangle ABC."""
    X_1062 = eval_trilinear_point(model, A, B, C, '(2 - sec(B)*sec(C))', ID="X_1062", classes=["center"])
    X_1063 = isogonal_conjugate(model, A, B, C, X_1062, ID="X_1063", classes=["selected", "target"])
    X_33 = eval_trilinear_point(model, A, B, C, '1 + sec(A)', ID="X_33", classes=["center", "incident"])
    X_79 = eval_trilinear_point(model, A, B, C, '1/(1 + 2*cos(A))', ID="X_79", classes=["center", "incident"])
    central_line(model, X_33, X_79, 33, 79, incident=True)
    X_34 = eval_trilinear_point(model, A, B, C, '1 - sec(A)', ID="X_34", classes=["center", "incident"])
    X_80 = eval_trilinear_point(model, A, B, C, '1/(1 - 2*cos(A))', ID="X_80", classes=["center", "incident"])
    central_line(model, X_34, X_80, 34, 80, incident=True)
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center", "incident"])
    X_378 = eval_trilinear_point(model, A, B, C, 'sec(A) + 2*cos(A)', ID="X_378", classes=["center", "incident"])
    central_line(model, X_1, X_378, 1, 378, incident=True)
    return promote_point_to_top(model, X_1063)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1063 on the given reference triangle."""
    model = create_model('X_1063 = ISOGONAL CONJUGATE OF X_1062')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01063(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01063.json"))
    write_center_svg(
        model_acute,
        here / "x-01063.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
