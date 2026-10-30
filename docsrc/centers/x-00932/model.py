"""GEOMETOR construction model for X(932) = X(190)-CROSS CONJUGATE OF X(100)."""

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
    intersect_lines,
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00932(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(932) = X(190)-CROSS CONJUGATE OF X(100) on reference triangle ABC."""
    X_87 = eval_trilinear_point(model, A, B, C, '1/(a*b + a*c - b*c)', ID="X(87)", classes=["center"])
    X_106 = eval_trilinear_point(model, A, B, C, 'a/(2*a - b - c)', ID="X(106)", classes=["center"])
    X_105 = eval_trilinear_point(model, A, B, C, '1/(b**(2) + c**(2) - a*(b + c))', ID="X(105)", classes=["center"])
    X_330 = eval_trilinear_point(model, A, B, C, 'b*c/(a*b + a*c - b*c)', ID="X(330)", classes=["center"])
    central_line(model, X_87, X_106, 87, 106)
    central_line(model, X_105, X_330, 105, 330)
    X_932 = intersect_lines(model, X_87, X_106, X_105, X_330, ID="X(932)", classes=["selected", "target"])
    X_1 = incenter_of(model, A, B, C, ID="X(1)", classes=["center", "incident"])
    X_727 = point_from_barycentrics(model, A, B, C, -0.11487719, 0.83400838, 0.2808688, ID="X(727)", classes=["center", "incident"])
    central_line(model, X_1, X_727, 1, 727, incident=True)
    return promote_point_to_top(model, X_932)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(932) on the given reference triangle."""
    model = create_model('X(932) = X(190)-CROSS CONJUGATE OF X(100)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00932(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00932.json"))
    write_center_svg(
        model_acute,
        here / "x-00932.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
