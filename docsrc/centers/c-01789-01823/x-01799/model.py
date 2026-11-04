"""GEOMETOR construction model for X_1799 = INVERSE MIMOSA TRANSFORM OF X_75."""

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
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_01799(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1799 = INVERSE MIMOSA TRANSFORM OF X_75 on reference triangle ABC."""
    X_1799 = eval_trilinear_point(model, A, B, C, 'cot(A)*csc(A +  omega  )', ID="X_1799", classes=["selected", "target"])
    X_2 = centroid_of(model, A, B, C, ID="X_2", classes=["center", "incident"])
    X_32 = eval_trilinear_point(model, A, B, C, 'a**(3)', ID="X_32", classes=["center", "incident"])
    central_line(model, X_2, X_32, 2, 32, incident=True)
    X_22 = eval_trilinear_point(model, A, B, C, 'a*(b**(4) + c**(4) - a**(4))', ID="X_22", classes=["center", "incident"])
    X_76 = eval_trilinear_point(model, A, B, C, '1/a**(3)', ID="X_76", classes=["center", "incident"])
    central_line(model, X_22, X_76, 22, 76, incident=True)
    X_25 = eval_trilinear_point(model, A, B, C, 'sin(A)*tan(A)', ID="X_25", classes=["center", "incident"])
    X_183 = eval_trilinear_point(model, A, B, C, 'b**(2)*c**(2)*cos(A-  omega  )', ID="X_183", classes=["center", "incident"])
    central_line(model, X_25, X_183, 25, 183, incident=True)
    return promote_point_to_top(model, X_1799)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1799 on the given reference triangle."""
    model = create_model('X_1799 = INVERSE MIMOSA TRANSFORM OF X_75')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01799(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01799.json"))
    write_center_svg(
        model_acute,
        here / "x-01799.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
