"""GEOMETOR construction model for X(675) = TRILINEAR POLE OF LINE X(6)X(514)."""

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
    isogonal_conjugate,
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00675(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(675) = TRILINEAR POLE OF LINE X(6)X(514) on reference triangle ABC."""
    X_674 = point_from_barycentrics(model, A, B, C, 0.6144277, 0.15846732, -0.77289502, ID="X(674)", classes=["center"])
    X_675 = isogonal_conjugate(model, A, B, C, X_674, ID="X(675)", classes=["selected", "target"])
    X_2 = centroid_of(model, A, B, C, ID="X(2)", classes=["center", "incident"])
    X_101 = eval_trilinear_point(model, A, B, C, 'a/(b - c)', ID="X(101)", classes=["center", "incident"])
    central_line(model, X_2, X_101, 2, 101, incident=True)
    X_7 = gergonne_point_of(model, A, B, C, ID="X(7)", classes=["center", "incident"])
    X_109 = eval_trilinear_point(model, A, B, C, 'a/(cos(B) - cos(C))', ID="X(109)", classes=["center", "incident"])
    central_line(model, X_7, X_109, 7, 109, incident=True)
    X_27 = eval_trilinear_point(model, A, B, C, '(sec(A))/(b + c)', ID="X(27)", classes=["center", "incident"])
    X_112 = eval_trilinear_point(model, A, B, C, 'a/(sin(2*B) - sin(2*C))', ID="X(112)", classes=["center", "incident"])
    central_line(model, X_27, X_112, 27, 112, incident=True)
    return promote_point_to_top(model, X_675)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(675) on the given reference triangle."""
    model = create_model('X(675) = TRILINEAR POLE OF LINE X(6)X(514)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00675(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00675.json"))
    write_center_svg(
        model_acute,
        here / "x-00675.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
