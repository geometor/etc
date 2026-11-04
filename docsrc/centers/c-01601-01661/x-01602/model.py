"""GEOMETOR construction model for X_1602 = TCC-PERSPECTOR OF X_7."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    gergonne_point_of,
    intersect_lines,
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_01602(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1602 = TCC-PERSPECTOR OF X_7 on reference triangle ABC."""
    X_24 = eval_trilinear_point(model, A, B, C, 'sec(A)*cos(2*A)', ID="X_24", classes=["center"])
    X_242 = eval_trilinear_point(model, A, B, C, '((sec(A))*((sin(A))**(2) - sin(B)*sin(C)))', ID="X_242", classes=["center"])
    X_7 = gergonne_point_of(model, A, B, C, ID="X_7", classes=["center"])
    X_1486 = eval_trilinear_point(model, A, B, C, 'a*( - a**(2)*(b + c - a) + b**(2)*(c + a - b) + c**(2)*(a + b - c))', ID="X_1486", classes=["center"])
    central_line(model, X_24, X_242, 24, 242)
    central_line(model, X_7, X_1486, 7, 1486)
    X_1602 = intersect_lines(model, X_24, X_242, X_7, X_1486, ID="X_1602", classes=["selected", "target"])
    X_22 = eval_trilinear_point(model, A, B, C, 'a*(b**(4) + c**(4) - a**(4))', ID="X_22", classes=["center", "incident"])
    X_1626 = point_from_barycentrics(model, A, B, C, 0.33171058, 0.30813288, 0.36015655, ID="X_1626", classes=["center", "incident"])
    central_line(model, X_22, X_1626, 22, 1626, incident=True)
    return promote_point_to_top(model, X_1602)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1602 on the given reference triangle."""
    model = create_model('X_1602 = TCC-PERSPECTOR OF X_7')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01602(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01602.json"))
    write_center_svg(
        model_acute,
        here / "x-01602.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
