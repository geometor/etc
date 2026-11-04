"""GEOMETOR construction model for X_2909 = ORTHIC-ISOGONAL CONJUGATE OF X_32."""

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


def construct_x_02909(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2909 = ORTHIC-ISOGONAL CONJUGATE OF X_32 on reference triangle ABC."""
    X_4 = orthocenter_of(model, A, B, C, ID="X_4", classes=["center"])
    X_32 = eval_trilinear_point(model, A, B, C, 'a**(3)', ID="X_32", classes=["center"])
    X_2909 = ceva_conjugate(model, A, B, C, X_4, X_32, ID="X_2909", classes=["selected", "target"])
    X_5 = nine_point_center_of(model, A, B, C, ID="X_5", classes=["center", "incident"])
    X_182 = eval_trilinear_point(model, A, B, C, 'cos(A-  omega  )', ID="X_182", classes=["center", "incident"])
    central_line(model, X_5, X_182, 5, 182, incident=True)
    X_39 = eval_trilinear_point(model, A, B, C, 'a*(b**(2) + c**(2))', ID="X_39", classes=["center", "incident"])
    X_184 = eval_trilinear_point(model, A, B, C, 'a**(2)*cos(A)', ID="X_184", classes=["center", "incident"])
    central_line(model, X_39, X_184, 39, 184, incident=True)
    X_211 = eval_trilinear_point(model, A, B, C, 'sin(A +  omega  )*(cos(B)*sin(B +  omega  ) + cos(C)*sin(C +  omega  ) - cos(A)*sin(A +  omega  ))', ID="X_211", classes=["center", "incident"])
    X_571 = eval_trilinear_point(model, A, B, C, 'sin(A)*cos(2*A)', ID="X_571", classes=["center", "incident"])
    central_line(model, X_211, X_571, 211, 571, incident=True)
    return promote_point_to_top(model, X_2909)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2909 on the given reference triangle."""
    model = create_model('X_2909 = ORTHIC-ISOGONAL CONJUGATE OF X_32')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02909(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02909.json"))
    write_center_svg(
        model_acute,
        here / "x-02909.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
