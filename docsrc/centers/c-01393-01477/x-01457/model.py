"""GEOMETOR construction model for X_1457 = X_517-BETH CONJUGATE OF X_517."""

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
    orthocenter_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_01457(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1457 = X_517-BETH CONJUGATE OF X_517 on reference triangle ABC."""
    X_106 = eval_trilinear_point(model, A, B, C, 'a/(2*a - b - c)', ID="X_106", classes=["center"])
    X_56 = eval_trilinear_point(model, A, B, C, 'a/(b + c - a)', ID="X_56", classes=["center"])
    X_1457 = ceva_conjugate(model, A, B, C, X_106, X_56, ID="X_1457", classes=["selected", "target"])
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center", "incident"])
    X_4 = orthocenter_of(model, A, B, C, ID="X_4", classes=["center", "incident"])
    central_line(model, X_1, X_4, 1, 4, incident=True)
    X_31 = eval_trilinear_point(model, A, B, C, 'a**(2)', ID="X_31", classes=["center", "incident"])
    central_line(model, X_31, X_56, 31, 56, incident=True)
    X_36 = eval_trilinear_point(model, A, B, C, '1 - 2*cos(A)', ID="X_36", classes=["center", "incident"])
    X_109 = eval_trilinear_point(model, A, B, C, 'a/(cos(B) - cos(C))', ID="X_109", classes=["center", "incident"])
    central_line(model, X_36, X_109, 36, 109, incident=True)
    return promote_point_to_top(model, X_1457)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1457 on the given reference triangle."""
    model = create_model('X_1457 = X_517-BETH CONJUGATE OF X_517')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01457(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01457.json"))
    write_center_svg(
        model_acute,
        here / "x-01457.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
