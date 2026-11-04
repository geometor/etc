"""GEOMETOR construction model for X_202 = X_1-CEVA CONJUGATE OF X_15."""

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
    feuerbach_point_of,
    incenter_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00202(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_202 = X_1-CEVA CONJUGATE OF X_15 on reference triangle ABC."""
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center"])
    X_15 = eval_trilinear_point(model, A, B, C, 'sin(A +  pi  /3)', ID="X_15", classes=["center"])
    X_202 = ceva_conjugate(model, A, B, C, X_1, X_15, ID="X_202", classes=["selected", "target"])
    X_11 = feuerbach_point_of(model, A, B, C, ID="X_11", classes=["center", "incident"])
    X_13 = eval_trilinear_point(model, A, B, C, 'csc(A +  pi  /3)', ID="X_13", classes=["center", "incident"])
    central_line(model, X_11, X_13, 11, 13, incident=True)
    X_12 = eval_trilinear_point(model, A, B, C, '1 + cos(B - C)', ID="X_12", classes=["center", "incident"])
    X_18 = eval_trilinear_point(model, A, B, C, 'csc(A -  pi  /6)', ID="X_18", classes=["center", "incident"])
    central_line(model, X_12, X_18, 12, 18, incident=True)
    X_36 = eval_trilinear_point(model, A, B, C, '1 - 2*cos(A)', ID="X_36", classes=["center", "incident"])
    central_line(model, X_15, X_36, 15, 36, incident=True)
    return promote_point_to_top(model, X_202)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_202 on the given reference triangle."""
    model = create_model('X_202 = X_1-CEVA CONJUGATE OF X_15')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00202(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00202.json"))
    write_center_svg(
        model_acute,
        here / "x-00202.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
