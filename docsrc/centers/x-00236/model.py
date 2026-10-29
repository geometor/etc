"""GEOMETOR construction model for X(236) = X(2)-CEVA CONJUGATE OF X(188)."""

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
    mittenpunkt_of,
    nagel_point_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00236(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(236) = X(2)-CEVA CONJUGATE OF X(188) on reference triangle ABC."""
    X_236 = eval_trilinear_point(model, A, B, C, '(csc(A/2))*(cos(B/2) + cos(C/2) - cos(A/2))', ID="X(236)", classes=["selected", "target"])
    X_2 = centroid_of(model, A, B, C, ID="X(2)", classes=["center", "incident"])
    X_174 = eval_trilinear_point(model, A, B, C, 'sec(A/2)', ID="X(174)", classes=["center", "incident"])
    central_line(model, X_2, X_174, 2, 174, incident=True)
    X_9 = mittenpunkt_of(model, A, B, C, ID="X(9)", classes=["center", "incident"])
    X_173 = eval_trilinear_point(model, A, B, C, 'cos(B/2) + cos(C/2) - cos(A/2)', ID="X(173)", classes=["center", "incident"])
    central_line(model, X_9, X_173, 9, 173, incident=True)
    X_8 = nagel_point_of(model, A, B, C, ID="X(8)", classes=["center", "incident"])
    X_178 = eval_trilinear_point(model, A, B, C, '(cos(B/2) + cos(C/2))*csc(A)', ID="X(178)", classes=["center", "incident"])
    central_line(model, X_8, X_178, 8, 178, incident=True)
    return promote_point_to_top(model, X_236)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(236) on the given reference triangle."""
    model = create_model('X(236) = X(2)-CEVA CONJUGATE OF X(188)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00236(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00236.json"))
    write_center_svg(
        model_acute,
        here / "x-00236.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
