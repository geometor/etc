"""GEOMETOR construction model for X_3205 = X_54-CEVA CONJUGATE OF X_61."""

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
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_03205(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3205 = X_54-CEVA CONJUGATE OF X_61 on reference triangle ABC."""
    X_54 = eval_trilinear_point(model, A, B, C, 'sec(B - C)', ID="X_54", classes=["center"])
    X_61 = eval_trilinear_point(model, A, B, C, 'sin(A +  pi  /6)', ID="X_61", classes=["center"])
    X_3205 = ceva_conjugate(model, A, B, C, X_54, X_61, ID="X_3205", classes=["selected", "target"])
    X_14 = eval_trilinear_point(model, A, B, C, 'csc(A -  pi  /3)', ID="X_14", classes=["center", "incident"])
    central_line(model, X_14, X_54, 14, 54, incident=True)
    X_49 = eval_trilinear_point(model, A, B, C, 'cos(3*A)', ID="X_49", classes=["center", "incident"])
    central_line(model, X_49, X_61, 49, 61, incident=True)
    X_17 = eval_trilinear_point(model, A, B, C, 'csc(A +  pi  /6)', ID="X_17", classes=["center", "incident"])
    X_110 = eval_trilinear_point(model, A, B, C, 'csc(B - C)', ID="X_110", classes=["center", "incident"])
    central_line(model, X_17, X_110, 17, 110, incident=True)
    return promote_point_to_top(model, X_3205)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3205 on the given reference triangle."""
    model = create_model('X_3205 = X_54-CEVA CONJUGATE OF X_61')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03205(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03205.json"))
    write_center_svg(
        model_acute,
        here / "x-03205.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
