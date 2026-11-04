"""GEOMETOR construction model for X_2580 = X_6-ISOCONJUGATE OF X_2574."""

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


def construct_x_02580(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2580 = X_6-ISOCONJUGATE OF X_2574 on reference triangle ABC."""
    X_2578 = point_from_barycentrics(model, A, B, C, -4.4869799, 4.7687517, 0.71822818, ID="X_2578", classes=["center"])
    X_2580 = isogonal_conjugate(model, A, B, C, X_2578, ID="X_2580", classes=["selected", "target"])
    X_19 = eval_trilinear_point(model, A, B, C, 'tan(A)', ID="X_19", classes=["center", "incident"])
    X_27 = eval_trilinear_point(model, A, B, C, '(sec(A))/(b + c)', ID="X_27", classes=["center", "incident"])
    central_line(model, X_19, X_27, 19, 27, incident=True)
    X_100 = eval_trilinear_point(model, A, B, C, '1/(b - c)', ID="X_100", classes=["center", "incident"])
    X_1113 = eval_trilinear_point(model, A, B, C, '(R - d)*cos(A) - 2*R*cos(B)*cos(C)', ID="X_1113", classes=["center", "incident"])
    central_line(model, X_100, X_1113, 100, 1113, incident=True)
    X_162 = eval_trilinear_point(model, A, B, C, '1/(sin(2*B) - sin(2*C))', ID="X_162", classes=["center", "incident"])
    X_1822 = point_from_barycentrics(model, A, B, C, -0.19858607, 0.24538924, 0.95319683, ID="X_1822", classes=["center", "incident"])
    central_line(model, X_162, X_1822, 162, 1822, incident=True)
    return promote_point_to_top(model, X_2580)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2580 on the given reference triangle."""
    model = create_model('X_2580 = X_6-ISOCONJUGATE OF X_2574')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02580(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02580.json"))
    write_center_svg(
        model_acute,
        here / "x-02580.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
