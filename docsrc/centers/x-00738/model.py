"""GEOMETOR construction model for X(738) = ISOGONAL CONJUGATE OF X(728)."""

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
    mittenpunkt_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00738(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(738) = ISOGONAL CONJUGATE OF X(728) on reference triangle ABC."""
    X_728 = eval_trilinear_point(model, A, B, C, '(cot(A/2))**(3)', ID="X(728)", classes=["center"])
    X_738 = isogonal_conjugate(model, A, B, C, X_728, ID="X(738)", classes=["selected", "target"])
    X_56 = eval_trilinear_point(model, A, B, C, 'a/(b + c - a)', ID="X(56)", classes=["center", "incident"])
    X_269 = eval_trilinear_point(model, A, B, C, '(a**(2) - (b - c)**(2))**(2)', ID="X(269)", classes=["center", "incident"])
    central_line(model, X_56, X_269, 56, 269, incident=True)
    X_57 = eval_trilinear_point(model, A, B, C, '1/(b + c - a)', ID="X(57)", classes=["center", "incident"])
    X_279 = eval_barycentric_point(model, A, B, C, '(a + b - c)**(2)*(a - b + c)**(2)', ID="X(279)", classes=["center", "incident"])
    central_line(model, X_57, X_279, 57, 279, incident=True)
    X_9 = mittenpunkt_of(model, A, B, C, ID="X(9)", classes=["center", "incident"])
    X_348 = eval_trilinear_point(model, A, B, C, 'cot(A)*(sec(A/2))**(2)', ID="X(348)", classes=["center", "incident"])
    central_line(model, X_9, X_348, 9, 348, incident=True)
    return promote_point_to_top(model, X_738)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(738) on the given reference triangle."""
    model = create_model('X(738) = ISOGONAL CONJUGATE OF X(728)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00738(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00738.json"))
    write_center_svg(
        model_acute,
        here / "x-00738.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
