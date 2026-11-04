"""GEOMETOR construction model for X_2380 = CIR(X_532)."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_barycentric_point,
    eval_trilinear_point,
    isogonal_conjugate,
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_02380(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2380 = CIR(X_532) on reference triangle ABC."""
    X_532 = point_from_barycentrics(model, A, B, C, -0.64045027, -0.11837216, 0.75882243, ID="X_532", classes=["center"])
    X_2380 = isogonal_conjugate(model, A, B, C, X_532, ID="X_2380", classes=["selected", "target"])
    X_14 = eval_trilinear_point(model, A, B, C, 'csc(A -  pi  /3)', ID="X_14", classes=["center", "incident"])
    X_99 = eval_trilinear_point(model, A, B, C, 'b*c/(b**(2) - c**(2))', ID="X_99", classes=["center", "incident"])
    central_line(model, X_14, X_99, 14, 99, incident=True)
    X_61 = eval_trilinear_point(model, A, B, C, 'sin(A +  pi  /6)', ID="X_61", classes=["center", "incident"])
    X_110 = eval_trilinear_point(model, A, B, C, 'csc(B - C)', ID="X_110", classes=["center", "incident"])
    central_line(model, X_61, X_110, 61, 110, incident=True)
    X_18 = eval_trilinear_point(model, A, B, C, 'csc(A -  pi  /6)', ID="X_18", classes=["center", "incident"])
    X_930 = eval_barycentric_point(model, A, B, C, '1/((b**(2) - c**(2))*(a**(4) + b**(4) + c**(4) - 2*a**(2)*b**(2) - 2*a**(2)*c**(2) - b**(2)*c**(2)))', ID="X_930", classes=["center", "incident"])
    central_line(model, X_18, X_930, 18, 930, incident=True)
    return promote_point_to_top(model, X_2380)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2380 on the given reference triangle."""
    model = create_model('X_2380 = CIR(X_532)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02380(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02380.json"))
    write_center_svg(
        model_acute,
        here / "x-02380.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
