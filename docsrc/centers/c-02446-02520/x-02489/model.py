"""GEOMETOR construction model for X_2489 = RADICAL CENTER OF {CIRCUMCIRCLE, NINE-POINT-CIRCLE, 2ND LEMOINE CIRCLE}."""

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
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_02489(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2489 = RADICAL CENTER OF {CIRCUMCIRCLE, NINE-POINT-CIRCLE, 2ND LEMOINE CIRCLE} on reference triangle ABC."""
    X_112 = eval_trilinear_point(model, A, B, C, 'a/(sin(2*B) - sin(2*C))', ID="X_112", classes=["center"])
    X_25 = eval_trilinear_point(model, A, B, C, 'sin(A)*tan(A)', ID="X_25", classes=["center"])
    X_2489 = ceva_conjugate(model, A, B, C, X_112, X_25, ID="X_2489", classes=["selected", "target"])
    X_250 = eval_trilinear_point(model, A, B, C, '(sec(A))*(csc(B - C))**(2)', ID="X_250", classes=["center", "incident"])
    central_line(model, X_112, X_250, 112, 250, incident=True)
    X_230 = eval_trilinear_point(model, A, B, C, 'b*c*(a**(2)*(2*a**(2) - b**(2) - c**(2)) + (b**(2) - c**(2))**(2))', ID="X_230", classes=["center", "incident"])
    X_231 = eval_trilinear_point(model, A, B, C, '(cos(B))*(4*(sin(C))**(2) - 1)*(cos(A)*sin(B) - sin(A)*cos(B)) - (cos(C))*(4*(sin(B))**(2) - 1)*(cos(C)*sin(A) - sin(C)*cos(A))', ID="X_231", classes=["center", "incident"])
    central_line(model, X_230, X_231, 230, 231, incident=True)
    X_19 = eval_trilinear_point(model, A, B, C, 'tan(A)', ID="X_19", classes=["center", "incident"])
    X_876 = point_from_barycentrics(model, A, B, C, 0.024662513, 1.0062305, -0.030893043, ID="X_876", classes=["center", "incident"])
    central_line(model, X_19, X_876, 19, 876, incident=True)
    return promote_point_to_top(model, X_2489)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2489 on the given reference triangle."""
    model = create_model('X_2489 = RADICAL CENTER OF {CIRCUMCIRCLE, NINE-POINT-CIRCLE, 2ND LEMOINE CIRCLE}')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02489(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02489.json"))
    write_center_svg(
        model_acute,
        here / "x-02489.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
