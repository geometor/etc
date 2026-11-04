"""GEOMETOR construction model for X_2913 = ORTHIC-ISOGONAL CONJUGATE OF X_62."""

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
    nine_point_center_of,
    orthocenter_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_02913(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2913 = ORTHIC-ISOGONAL CONJUGATE OF X_62 on reference triangle ABC."""
    X_4 = orthocenter_of(model, A, B, C, ID="X_4", classes=["center"])
    X_62 = eval_trilinear_point(model, A, B, C, 'sin(A -  pi  /6)', ID="X_62", classes=["center"])
    X_2913 = ceva_conjugate(model, A, B, C, X_4, X_62, ID="X_2913", classes=["selected", "target"])
    X_5 = nine_point_center_of(model, A, B, C, ID="X_5", classes=["center", "incident"])
    X_15 = eval_trilinear_point(model, A, B, C, 'sin(A +  pi  /3)', ID="X_15", classes=["center", "incident"])
    central_line(model, X_5, X_15, 5, 15, incident=True)
    X_143 = eval_trilinear_point(model, A, B, C, '(sec(A))*(cos(2*C - 2*A) + cos(2*A - 2*B))', ID="X_143", classes=["center", "incident"])
    central_line(model, X_62, X_143, 62, 143, incident=True)
    X_61 = eval_trilinear_point(model, A, B, C, 'sin(A +  pi  /6)', ID="X_61", classes=["center", "incident"])
    X_184 = eval_trilinear_point(model, A, B, C, 'a**(2)*cos(A)', ID="X_184", classes=["center", "incident"])
    central_line(model, X_61, X_184, 61, 184, incident=True)
    return promote_point_to_top(model, X_2913)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2913 on the given reference triangle."""
    model = create_model('X_2913 = ORTHIC-ISOGONAL CONJUGATE OF X_62')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02913(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02913.json"))
    write_center_svg(
        model_acute,
        here / "x-02913.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
