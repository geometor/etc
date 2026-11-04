"""GEOMETOR construction model for X_1616 = TCC-PERSPECTOR OF X_56."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    crosspoint,
    eval_trilinear_point,
    incenter_of,
    promote_point_to_top,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_01616(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1616 = TCC-PERSPECTOR OF X_56 on reference triangle ABC."""
    X_934 = eval_trilinear_point(model, A, B, C, '1/((b - c)*(b + c - a)**(2))', ID="X_934", classes=["center"])
    X_1016 = eval_trilinear_point(model, A, B, C, '1/(sin(A)*(sin(A/2))**(2)*(1 - cos(B - C)))', ID="X_1016", classes=["center"])
    X_1616 = crosspoint(model, A, B, C, X_934, X_1016, ID="X_1616", classes=["selected", "target"])
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center", "incident"])
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center", "incident"])
    central_line(model, X_1, X_6, 1, 6, incident=True)
    X_55 = eval_trilinear_point(model, A, B, C, 'a*(b + c - a)', ID="X_55", classes=["center", "incident"])
    X_1201 = eval_trilinear_point(model, A, B, C, '(a*(b**(2) + c**(2) - 2*b*c + a*b + a*c))', ID="X_1201", classes=["center", "incident"])
    central_line(model, X_55, X_1201, 55, 1201, incident=True)
    X_42 = eval_trilinear_point(model, A, B, C, 'a*(b + c)', ID="X_42", classes=["center", "incident"])
    X_1293 = eval_trilinear_point(model, A, B, C, '(a/((b - c)*(3*a - b - c)))', ID="X_1293", classes=["center", "incident"])
    central_line(model, X_42, X_1293, 42, 1293, incident=True)
    return promote_point_to_top(model, X_1616)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1616 on the given reference triangle."""
    model = create_model('X_1616 = TCC-PERSPECTOR OF X_56')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01616(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01616.json"))
    write_center_svg(
        model_acute,
        here / "x-01616.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
