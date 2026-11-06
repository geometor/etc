"""GEOMETOR construction model for X_3360 = SS(a → bc) OF X_20."""

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
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_03360(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3360 = SS(a → bc) OF X_20 on reference triangle ABC."""
    X_1613 = eval_trilinear_point(model, A, B, C, '(a*(b**(2)*c**(2) - c**(2)*a**(2) - a**(2)*b**(2)))', ID="X_1613", classes=["center"])
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center"])
    X_3360 = ceva_conjugate(model, A, B, C, X_1613, X_6, ID="X_3360", classes=["selected", "target"])
    X_194 = eval_trilinear_point(model, A, B, C, 'b*c*(a**(2)*b**(2) + a**(2)*c**(2) - b**(2)*c**(2))', ID="X_194", classes=["center", "incident"])
    central_line(model, X_6, X_194, 6, 194, incident=True)
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center", "incident"])
    X_2162 = point_from_barycentrics(model, A, B, C, 0.35035055, 0.31361109, 0.33603836, ID="X_2162", classes=["center", "incident"])
    central_line(model, X_1, X_2162, 1, 2162, incident=True)
    X_159 = eval_trilinear_point(model, A, B, C, '(a*((a**(2) + b**(2) + c**(2))*sin(2*A) + (c**(2) - b**(2) - a**(2))*sin(2*B) + (b**(2) - c**(2) - a**(2))*sin(2*C)))', ID="X_159", classes=["center", "incident"])
    X_2076 = eval_trilinear_point(model, A, B, C, '(sin(A) - 2*cos(A)*sin(2*omega) )', ID="X_2076", classes=["center", "incident"])
    central_line(model, X_159, X_2076, 159, 2076, incident=True)
    return promote_point_to_top(model, X_3360)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3360 on the given reference triangle."""
    model = create_model('X_3360 = SS(a → bc) OF X_20')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03360(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03360.json"))
    write_center_svg(
        model_acute,
        here / "x-03360.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
