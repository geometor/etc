"""GEOMETOR construction model for X_2629 = CROSSSUM PU(74)."""

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
    incenter_of,
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_02629(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2629 = CROSSSUM PU(74) on reference triangle ABC."""
    X_656 = eval_trilinear_point(model, A, B, C, 'tan(B) - tan(C)', ID="X_656", classes=["center"])
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center"])
    X_2629 = ceva_conjugate(model, A, B, C, X_656, X_1, ID="X_2629", classes=["selected", "target"])
    X_162 = eval_trilinear_point(model, A, B, C, '1/(sin(2*B) - sin(2*C))', ID="X_162", classes=["center", "incident"])
    central_line(model, X_1, X_162, 1, 162, incident=True)
    X_191 = eval_trilinear_point(model, A, B, C, '(b + c - a)*(b*c + c*a + a*b) + b**(3) + c**(3) - a**(3)', ID="X_191", classes=["center", "incident"])
    X_1047 = point_from_barycentrics(model, A, B, C, 0.47678192, 0.53587009, -0.012652005, ID="X_1047", classes=["center", "incident"])
    central_line(model, X_191, X_1047, 191, 1047, incident=True)
    X_293 = eval_trilinear_point(model, A, B, C, 'cos(A)*sec(A +  omega  )', ID="X_293", classes=["center", "incident"])
    X_1707 = eval_trilinear_point(model, A, B, C, '3*a**(2) - b**(2) - c**(2)', ID="X_1707", classes=["center", "incident"])
    central_line(model, X_293, X_1707, 293, 1707, incident=True)
    return promote_point_to_top(model, X_2629)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2629 on the given reference triangle."""
    model = create_model('X_2629 = CROSSSUM PU(74)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02629(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02629.json"))
    write_center_svg(
        model_acute,
        here / "x-02629.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
