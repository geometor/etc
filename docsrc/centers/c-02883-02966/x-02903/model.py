"""GEOMETOR construction model for X_2903 = ORTHIC-ISOGONAL CONJUGATE OF X_16."""

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


def construct_x_02903(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2903 = ORTHIC-ISOGONAL CONJUGATE OF X_16 on reference triangle ABC."""
    X_4 = orthocenter_of(model, A, B, C, ID="X_4", classes=["center"])
    X_16 = eval_trilinear_point(model, A, B, C, 'sin(A-  pi  /3)', ID="X_16", classes=["center"])
    X_2903 = ceva_conjugate(model, A, B, C, X_4, X_16, ID="X_2903", classes=["selected", "target"])
    X_5 = nine_point_center_of(model, A, B, C, ID="X_5", classes=["center", "incident"])
    X_14 = eval_trilinear_point(model, A, B, C, 'csc(A -  pi  /3)', ID="X_14", classes=["center", "incident"])
    central_line(model, X_5, X_14, 5, 14, incident=True)
    X_15 = eval_trilinear_point(model, A, B, C, 'sin(A +  pi  /3)', ID="X_15", classes=["center", "incident"])
    X_184 = eval_trilinear_point(model, A, B, C, 'a**(2)*cos(A)', ID="X_184", classes=["center", "incident"])
    central_line(model, X_15, X_184, 15, 184, incident=True)
    X_1154 = eval_trilinear_point(model, A, B, C, '(1 - 4*(cos(A))**(2))*cos(B - C)', ID="X_1154", classes=["center", "incident"])
    central_line(model, X_16, X_1154, 16, 1154, incident=True)
    return promote_point_to_top(model, X_2903)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2903 on the given reference triangle."""
    model = create_model('X_2903 = ORTHIC-ISOGONAL CONJUGATE OF X_16')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02903(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02903.json"))
    write_center_svg(
        model_acute,
        here / "x-02903.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
