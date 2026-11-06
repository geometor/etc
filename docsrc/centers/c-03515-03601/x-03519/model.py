"""GEOMETOR construction model for X_3519 = ISOGONAL CONJUGATE OF X_3518."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    anticomplement,
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    orthocenter_of,
    promote_point_to_top,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_03519(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3519 = ISOGONAL CONJUGATE OF X_3518 on reference triangle ABC."""
    X_1493 = eval_trilinear_point(model, A, B, C, '(csc(B +  pi  /6)*csc(C -  pi  /6) + csc(C +  pi  /6)*csc(B -  pi  /6))', ID="X_1493", classes=["center"])
    X_3519 = anticomplement(model, A, B, C, X_1493, ID="X_3519", classes=["selected", "target"])
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center", "incident"])
    X_17 = eval_trilinear_point(model, A, B, C, 'csc(A +  pi  /6)', ID="X_17", classes=["center", "incident"])
    central_line(model, X_6, X_17, 6, 17, incident=True)
    X_4 = orthocenter_of(model, A, B, C, ID="X_4", classes=["center", "incident"])
    X_93 = eval_trilinear_point(model, A, B, C, 'sec(3*A)', ID="X_93", classes=["center", "incident"])
    central_line(model, X_4, X_93, 4, 93, incident=True)
    X_54 = eval_trilinear_point(model, A, B, C, 'sec(B - C)', ID="X_54", classes=["center", "incident"])
    X_140 = eval_trilinear_point(model, A, B, C, '2*cos(A) + cos(B - C)', ID="X_140", classes=["center", "incident"])
    central_line(model, X_54, X_140, 54, 140, incident=True)
    return promote_point_to_top(model, X_3519)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3519 on the given reference triangle."""
    model = create_model('X_3519 = ISOGONAL CONJUGATE OF X_3518')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03519(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03519.json"))
    write_center_svg(
        model_acute,
        here / "x-03519.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
