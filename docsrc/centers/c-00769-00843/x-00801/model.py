"""GEOMETOR construction model for X_801 = ISOGONAL CONJUGATE OF X_800."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    isogonal_conjugate,
    orthocenter_of,
    promote_point_to_top,
    spieker_center_of,
)
from geometor.etc.render import write_center_svg


def construct_x_00801(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_801 = ISOGONAL CONJUGATE OF X_800 on reference triangle ABC."""
    X_800 = eval_trilinear_point(model, A, B, C, 'sin(A)*((cos(B))**(2) + (cos(C))**(2))', ID="X_800", classes=["center"])
    X_801 = isogonal_conjugate(model, A, B, C, X_800, ID="X_801", classes=["selected", "target"])
    X_10 = spieker_center_of(model, A, B, C, ID="X_10", classes=["center", "incident"])
    X_775 = eval_trilinear_point(model, A, B, C, '(1/((cos(B))**(2) + (cos(C))**(2)))', ID="X_775", classes=["center", "incident"])
    central_line(model, X_10, X_775, 10, 775, incident=True)
    X_4 = orthocenter_of(model, A, B, C, ID="X_4", classes=["center", "incident"])
    X_1092 = eval_trilinear_point(model, A, B, C, '((cos(A))**(3))', ID="X_1092", classes=["center", "incident"])
    central_line(model, X_4, X_1092, 4, 1092, incident=True)
    return promote_point_to_top(model, X_801)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_801 on the given reference triangle."""
    model = create_model('X_801 = ISOGONAL CONJUGATE OF X_800')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00801(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00801.json"))
    write_center_svg(
        model_acute,
        here / "x-00801.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
