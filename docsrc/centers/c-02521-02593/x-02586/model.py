"""GEOMETOR construction model for X_2586 = X_3-ISOCONJUGATE OF X_2574."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    incenter_of,
    isogonal_conjugate,
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_02586(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2586 = X_3-ISOCONJUGATE OF X_2574 on reference triangle ABC."""
    X_2584 = point_from_barycentrics(model, A, B, C, 3.3911992, -2.2826338, -0.10856545, ID="X_2584", classes=["center"])
    X_2586 = isogonal_conjugate(model, A, B, C, X_2584, ID="X_2586", classes=["selected", "target"])
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center", "incident"])
    X_29 = eval_trilinear_point(model, A, B, C, '(sec(A))/(cos(B) + cos(C))', ID="X_29", classes=["center", "incident"])
    central_line(model, X_1, X_29, 1, 29, incident=True)
    X_108 = eval_trilinear_point(model, A, B, C, 'a/(sec(B) - sec(C))', ID="X_108", classes=["center", "incident"])
    X_1113 = eval_trilinear_point(model, A, B, C, '(R - d)*cos(A) - 2*R*cos(B)*cos(C)', ID="X_1113", classes=["center", "incident"])
    central_line(model, X_108, X_1113, 108, 1113, incident=True)
    X_162 = eval_trilinear_point(model, A, B, C, '1/(sin(2*B) - sin(2*C))', ID="X_162", classes=["center", "incident"])
    X_1822 = point_from_barycentrics(model, A, B, C, -0.19858607, 0.24538924, 0.95319683, ID="X_1822", classes=["center", "incident"])
    central_line(model, X_162, X_1822, 162, 1822, incident=True)
    return promote_point_to_top(model, X_2586)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2586 on the given reference triangle."""
    model = create_model('X_2586 = X_3-ISOCONJUGATE OF X_2574')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02586(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02586.json"))
    write_center_svg(
        model_acute,
        here / "x-02586.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
