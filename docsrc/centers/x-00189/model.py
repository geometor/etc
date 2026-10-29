"""GEOMETOR construction model for X(189) = CYCLOCEVIAN CONJUGATE OF X(8)."""

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
    gergonne_point_of,
    nagel_point_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00189(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(189) = CYCLOCEVIAN CONJUGATE OF X(8) on reference triangle ABC."""
    X_189 = eval_trilinear_point(model, A, B, C, 'b*c/(cos(B) + cos(C) - cos(A) - 1)', ID="X(189)", classes=["selected", "target"])
    X_8 = nagel_point_of(model, A, B, C, ID="X(8)", classes=["center", "incident"])
    X_20 = eval_trilinear_point(model, A, B, C, 'cos(A) - cos(B)*cos(C)', ID="X(20)", classes=["center", "incident"])
    central_line(model, X_8, X_20, 8, 20, incident=True)
    X_2 = centroid_of(model, A, B, C, ID="X(2)", classes=["center", "incident"])
    X_77 = eval_trilinear_point(model, A, B, C, '1/(1 + sec(A))', ID="X(77)", classes=["center", "incident"])
    central_line(model, X_2, X_77, 2, 77, incident=True)
    X_7 = gergonne_point_of(model, A, B, C, ID="X(7)", classes=["center", "incident"])
    X_92 = eval_trilinear_point(model, A, B, C, 'csc(2*A)', ID="X(92)", classes=["center", "incident"])
    central_line(model, X_7, X_92, 7, 92, incident=True)
    return promote_point_to_top(model, X_189)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(189) on the given reference triangle."""
    model = create_model('X(189) = CYCLOCEVIAN CONJUGATE OF X(8)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00189(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00189.json"))
    write_center_svg(
        model_acute,
        here / "x-00189.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
