"""GEOMETOR construction model for X_2581 = X_6-ISOCONJUGATE OF X_2575."""

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


def construct_x_02581(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2581 = X_6-ISOCONJUGATE OF X_2575 on reference triangle ABC."""
    X_2579 = point_from_barycentrics(model, A, B, C, -1.2817064, -2.9239046, 5.205611, ID="X_2579", classes=["center"])
    X_2581 = isogonal_conjugate(model, A, B, C, X_2579, ID="X_2581", classes=["selected", "target"])
    X_19 = eval_trilinear_point(model, A, B, C, 'tan(A)', ID="X_19", classes=["center", "incident"])
    X_27 = eval_trilinear_point(model, A, B, C, '(sec(A))/(b + c)', ID="X_27", classes=["center", "incident"])
    central_line(model, X_19, X_27, 19, 27, incident=True)
    X_100 = eval_trilinear_point(model, A, B, C, '1/(b - c)', ID="X_100", classes=["center", "incident"])
    X_1114 = eval_trilinear_point(model, A, B, C, '(R + d)*cos(A) - 2*R*cos(B)*cos(C)', ID="X_1114", classes=["center", "incident"])
    central_line(model, X_100, X_1114, 100, 1114, incident=True)
    X_162 = eval_trilinear_point(model, A, B, C, '1/(sin(2*B) - sin(2*C))', ID="X_162", classes=["center", "incident"])
    X_1823 = point_from_barycentrics(model, A, B, C, 0.72123578, 0.4152025, -0.13643829, ID="X_1823", classes=["center", "incident"])
    central_line(model, X_162, X_1823, 162, 1823, incident=True)
    return promote_point_to_top(model, X_2581)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2581 on the given reference triangle."""
    model = create_model('X_2581 = X_6-ISOCONJUGATE OF X_2575')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02581(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02581.json"))
    write_center_svg(
        model_acute,
        here / "x-02581.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
