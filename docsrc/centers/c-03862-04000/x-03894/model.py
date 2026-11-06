"""GEOMETOR construction model for X_3894 = X_549com[INVERSE(n(3rd EULER TRIANGLE))]."""

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
    incenter_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_03894(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3894 = X_549com[INVERSE(n(3rd EULER TRIANGLE))] on reference triangle ABC."""
    X_3894 = eval_barycentric_point(model, A, B, C, '(a*(2*b**(3) + 2*c**(3) - 2*a**(2)*b - 2*a**(2)*c - 3*a*b*c))', ID="X_3894", classes=["selected", "target"])
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center", "incident"])
    X_21 = eval_trilinear_point(model, A, B, C, '1/(cos(B) + cos(C))', ID="X_21", classes=["center", "incident"])
    central_line(model, X_1, X_21, 1, 21, incident=True)
    X_518 = eval_trilinear_point(model, A, B, C, '(a*b + a*c - b**(2) - c**(2))', ID="X_518", classes=["center", "incident"])
    X_599 = eval_trilinear_point(model, A, B, C, 'b*c*(a**(2) - 2*b**(2) - 2*c**(2))', ID="X_599", classes=["center", "incident"])
    central_line(model, X_518, X_599, 518, 599, incident=True)
    X_210 = eval_trilinear_point(model, A, B, C, '(b + c)*(b + c - a)', ID="X_210", classes=["center", "incident"])
    X_942 = eval_trilinear_point(model, A, B, C, '2*a*b*c + (b + c)*(a - b + c)*(a + b -c)', ID="X_942", classes=["center", "incident"])
    central_line(model, X_210, X_942, 210, 942, incident=True)
    return promote_point_to_top(model, X_3894)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3894 on the given reference triangle."""
    model = create_model('X_3894 = X_549com[INVERSE(n(3rd EULER TRIANGLE))]')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03894(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03894.json"))
    write_center_svg(
        model_acute,
        here / "x-03894.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
