"""GEOMETOR construction model for X_2381 = CIR(X_533)."""

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


def construct_x_02381(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2381 = CIR(X_533) on reference triangle ABC."""
    X_533 = point_from_barycentrics(model, A, B, C, 0.76482932, -0.13487259, -0.62995674, ID="X_533", classes=["center"])
    X_2381 = isogonal_conjugate(model, A, B, C, X_533, ID="X_2381", classes=["selected", "target"])
    X_13 = eval_trilinear_point(model, A, B, C, 'csc(A +  pi  /3)', ID="X_13", classes=["center", "incident"])
    X_99 = eval_trilinear_point(model, A, B, C, 'b*c/(b**(2) - c**(2))', ID="X_99", classes=["center", "incident"])
    central_line(model, X_13, X_99, 13, 99, incident=True)
    X_62 = eval_trilinear_point(model, A, B, C, 'sin(A -  pi  /6)', ID="X_62", classes=["center", "incident"])
    X_110 = eval_trilinear_point(model, A, B, C, 'csc(B - C)', ID="X_110", classes=["center", "incident"])
    central_line(model, X_62, X_110, 62, 110, incident=True)
    X_17 = eval_trilinear_point(model, A, B, C, 'csc(A +  pi  /6)', ID="X_17", classes=["center", "incident"])
    X_930 = eval_barycentric_point(model, A, B, C, '1/((b**(2) - c**(2))*(a**(4) + b**(4) + c**(4) - 2*a**(2)*b**(2) - 2*a**(2)*c**(2) - b**(2)*c**(2)))', ID="X_930", classes=["center", "incident"])
    central_line(model, X_17, X_930, 17, 930, incident=True)
    return promote_point_to_top(model, X_2381)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2381 on the given reference triangle."""
    model = create_model('X_2381 = CIR(X_533)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02381(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02381.json"))
    write_center_svg(
        model_acute,
        here / "x-02381.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
