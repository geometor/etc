"""GEOMETOR construction model for X_3504 = INTERSECTION OF LINES X_25X_385 AND X_32X_1613."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    ceva_conjugate,
    circumcenter_of,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_03504(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3504 = INTERSECTION OF LINES X_25X_385 AND X_32X_1613 on reference triangle ABC."""
    X_69 = eval_trilinear_point(model, A, B, C, '(cos(A))/a**(2)', ID="X_69", classes=["center"])
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center"])
    X_3504 = ceva_conjugate(model, A, B, C, X_69, X_3, ID="X_3504", classes=["selected", "target"])
    X_25 = eval_trilinear_point(model, A, B, C, 'sin(A)*tan(A)', ID="X_25", classes=["center", "incident"])
    X_385 = eval_trilinear_point(model, A, B, C, 'b*c*(a**(4) - b**(2)*c**(2))', ID="X_385", classes=["center", "incident"])
    central_line(model, X_25, X_385, 25, 385, incident=True)
    X_1423 = eval_trilinear_point(model, A, B, C, '((a*b + a*c - b*c)/(b + c - a))', ID="X_1423", classes=["center", "incident"])
    X_1716 = point_from_barycentrics(model, A, B, C, -0.1402975, 0.31440162, 0.82589588, ID="X_1716", classes=["center", "incident"])
    central_line(model, X_1423, X_1716, 1423, 1716, incident=True)
    X_32 = eval_trilinear_point(model, A, B, C, 'a**(3)', ID="X_32", classes=["center", "incident"])
    X_3229 = eval_trilinear_point(model, A, B, C, 'a*(a**(2)*b**(4) + a**(2)*c**(4) - b**(2)*c**(4) - c **(2)*b**(4))', ID="X_3229", classes=["center", "incident"])
    central_line(model, X_32, X_3229, 32, 3229, incident=True)
    return promote_point_to_top(model, X_3504)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3504 on the given reference triangle."""
    model = create_model('X_3504 = INTERSECTION OF LINES X_25X_385 AND X_32X_1613')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03504(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03504.json"))
    write_center_svg(
        model_acute,
        here / "x-03504.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
