"""GEOMETOR construction model for X_2378 = CIR(X_530)."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    isogonal_conjugate,
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_02378(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2378 = CIR(X_530) on reference triangle ABC."""
    X_530 = point_from_barycentrics(model, A, B, C, -0.59263559, -0.1900846, 0.78272019, ID="X_530", classes=["center"])
    X_2378 = isogonal_conjugate(model, A, B, C, X_530, ID="X_2378", classes=["selected", "target"])
    X_15 = eval_trilinear_point(model, A, B, C, 'sin(A +  pi  /3)', ID="X_15", classes=["center", "incident"])
    X_110 = eval_trilinear_point(model, A, B, C, 'csc(B - C)', ID="X_110", classes=["center", "incident"])
    central_line(model, X_15, X_110, 15, 110, incident=True)
    X_99 = eval_trilinear_point(model, A, B, C, 'b*c/(b**(2) - c**(2))', ID="X_99", classes=["center", "incident"])
    X_298 = eval_trilinear_point(model, A, B, C, '(csc(A))**(2)*sin(A +  pi  /3)', ID="X_298", classes=["center", "incident"])
    central_line(model, X_99, X_298, 99, 298, incident=True)
    X_14 = eval_trilinear_point(model, A, B, C, 'csc(A -  pi  /3)', ID="X_14", classes=["center", "incident"])
    X_476 = eval_trilinear_point(model, A, B, C, '1/((1 + 2*cos(2*A))*sin(B - C))', ID="X_476", classes=["center", "incident"])
    central_line(model, X_14, X_476, 14, 476, incident=True)
    return promote_point_to_top(model, X_2378)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2378 on the given reference triangle."""
    model = create_model('X_2378 = CIR(X_530)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02378(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02378.json"))
    write_center_svg(
        model_acute,
        here / "x-02378.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
