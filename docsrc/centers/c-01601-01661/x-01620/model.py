"""GEOMETOR construction model for X_1620 = TCC-PERSPECTOR OF X_64."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    circumcenter_of,
    construct_baseline_triangle,
    create_model,
    eval_barycentric_point,
    eval_trilinear_point,
    intersect_lines,
    promote_point_to_top,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_01620(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1620 = TCC-PERSPECTOR OF X_64 on reference triangle ABC."""
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center"])
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center"])
    X_154 = eval_trilinear_point(model, A, B, C, '(cos(A) - cos(B)*cos(C))*a**(2)', ID="X_154", classes=["center"])
    X_1204 = eval_barycentric_point(model, A, B, C, 'a**(2)*(a**(2) - b**(2) - c**(2))*(a**(6) - 3*a**(2)*(b**(2) - c**(2))**(2) + 2*(b**(2) - c**(2))**(2)*(b**(2) + c**(2)))', ID="X_1204", classes=["center"])
    central_line(model, X_3, X_6, 3, 6)
    central_line(model, X_154, X_1204, 154, 1204)
    X_1620 = intersect_lines(model, X_3, X_6, X_154, X_1204, ID="X_1620", classes=["selected", "target"])
    X_186 = eval_trilinear_point(model, A, B, C, '4*cos(A) - sec(A)', ID="X_186", classes=["center", "incident"])
    X_1498 = eval_trilinear_point(model, A, B, C, '(sin(A))*((tan(B))**(2) + (tan(C))**(2) - (tan(A))**(2))', ID="X_1498", classes=["center", "incident"])
    central_line(model, X_186, X_1498, 186, 1498, incident=True)
    return promote_point_to_top(model, X_1620)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1620 on the given reference triangle."""
    model = create_model('X_1620 = TCC-PERSPECTOR OF X_64')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01620(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01620.json"))
    write_center_svg(
        model_acute,
        here / "x-01620.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
