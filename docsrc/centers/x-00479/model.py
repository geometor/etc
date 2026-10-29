"""GEOMETOR construction model for X(479) = X(269)-CROSS CONJUGATE OF X(279)."""

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
    gergonne_point_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00479(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(479) = X(269)-CROSS CONJUGATE OF X(279) on reference triangle ABC."""
    X_479 = eval_trilinear_point(model, A, B, C, '(tan(A/2)*sec(A/2))**(2)', ID="X(479)", classes=["selected", "target"])
    X_57 = eval_trilinear_point(model, A, B, C, '1/(b + c - a)', ID="X(57)", classes=["center", "incident"])
    X_279 = eval_barycentric_point(model, A, B, C, '(a + b - c)**(2)*(a - b + c)**(2)', ID="X(279)", classes=["center", "incident"])
    central_line(model, X_57, X_279, 57, 279, incident=True)
    X_7 = gergonne_point_of(model, A, B, C, ID="X(7)", classes=["center", "incident"])
    X_354 = eval_trilinear_point(model, A, B, C, '(b - c)**(2) - a*b - a*c', ID="X(354)", classes=["center", "incident"])
    central_line(model, X_7, X_354, 7, 354, incident=True)
    X_269 = eval_trilinear_point(model, A, B, C, '(a**(2) - (b - c)**(2))**(2)', ID="X(269)", classes=["center", "incident"])
    X_614 = eval_trilinear_point(model, A, B, C, '(cot(B/2))**(2) + (cot(C/2))**(2)', ID="X(614)", classes=["center", "incident"])
    central_line(model, X_269, X_614, 269, 614, incident=True)
    return promote_point_to_top(model, X_479)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(479) on the given reference triangle."""
    model = create_model('X(479) = X(269)-CROSS CONJUGATE OF X(279)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00479(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00479.json"))
    write_center_svg(
        model_acute,
        here / "x-00479.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
