"""GEOMETOR construction model for X_1486 = PERSPECTOR OF TANGENTIAL AND INTOUCH TRIANGLES."""

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
    gergonne_point_of,
    incenter_of,
    promote_point_to_top,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_01486(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1486 = PERSPECTOR OF TANGENTIAL AND INTOUCH TRIANGLES on reference triangle ABC."""
    X_7 = gergonne_point_of(model, A, B, C, ID="X_7", classes=["center"])
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center"])
    X_1486 = ceva_conjugate(model, A, B, C, X_7, X_6, ID="X_1486", classes=["selected", "target"])
    X_19 = eval_trilinear_point(model, A, B, C, 'tan(A)', ID="X_19", classes=["center", "incident"])
    X_25 = eval_trilinear_point(model, A, B, C, 'sin(A)*tan(A)', ID="X_25", classes=["center", "incident"])
    central_line(model, X_19, X_25, 19, 25, incident=True)
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center", "incident"])
    X_142 = eval_trilinear_point(model, A, B, C, 'b + c - ((b - c)**(2))/a', ID="X_142", classes=["center", "incident"])
    central_line(model, X_3, X_142, 3, 142, incident=True)
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center", "incident"])
    X_159 = eval_trilinear_point(model, A, B, C, '(a*((a**(2) + b**(2) + c**(2))*sin(2*A) + (c**(2) - b**(2) - a**(2))*sin(2*B) + (b**(2) - c**(2) - a**(2))*sin(2*C)))', ID="X_159", classes=["center", "incident"])
    central_line(model, X_1, X_159, 1, 159, incident=True)
    return promote_point_to_top(model, X_1486)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1486 on the given reference triangle."""
    model = create_model('X_1486 = PERSPECTOR OF TANGENTIAL AND INTOUCH TRIANGLES')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01486(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01486.json"))
    write_center_svg(
        model_acute,
        here / "x-01486.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
