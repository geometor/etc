"""GEOMETOR construction model for X_3203 = X_54-CEVA CONJUGATE OF X_39."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    crosspoint,
    eval_trilinear_point,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_03203(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3203 = X_54-CEVA CONJUGATE OF X_39 on reference triangle ABC."""
    X_1342 = eval_trilinear_point(model, A, B, C, 'sin(A) + cos(A)*cot( omega  /2)', ID="X_1342", classes=["center"])
    X_1343 = eval_trilinear_point(model, A, B, C, 'sin(A) - cos(A)*tan( omega  /2)', ID="X_1343", classes=["center"])
    X_3203 = crosspoint(model, A, B, C, X_1342, X_1343, ID="X_3203", classes=["selected", "target"])
    X_83 = eval_trilinear_point(model, A, B, C, 'b*c/(b**(2) + c**(2))', ID="X_83", classes=["center", "incident"])
    X_110 = eval_trilinear_point(model, A, B, C, 'csc(B - C)', ID="X_110", classes=["center", "incident"])
    central_line(model, X_83, X_110, 83, 110, incident=True)
    X_32 = eval_trilinear_point(model, A, B, C, 'a**(3)', ID="X_32", classes=["center", "incident"])
    X_184 = eval_trilinear_point(model, A, B, C, 'a**(2)*cos(A)', ID="X_184", classes=["center", "incident"])
    central_line(model, X_32, X_184, 32, 184, incident=True)
    X_140 = eval_trilinear_point(model, A, B, C, '2*cos(A) + cos(B - C)', ID="X_140", classes=["center", "incident"])
    X_141 = eval_trilinear_point(model, A, B, C, 'b*c*(b**(2) + c**(2))', ID="X_141", classes=["center", "incident"])
    central_line(model, X_140, X_141, 140, 141, incident=True)
    return promote_point_to_top(model, X_3203)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3203 on the given reference triangle."""
    model = create_model('X_3203 = X_54-CEVA CONJUGATE OF X_39')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03203(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03203.json"))
    write_center_svg(
        model_acute,
        here / "x-03203.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
