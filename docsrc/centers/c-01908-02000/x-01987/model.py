"""GEOMETOR construction model for X_1987 = 1st LEMOINE ANTIPARALLELS POINT."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    isogonal_conjugate,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_01987(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1987 = 1st LEMOINE ANTIPARALLELS POINT on reference triangle ABC."""
    X_401 = eval_trilinear_point(model, A, B, C, '(sin(2*B)*sin(2*C) - (sin(2*A))**(2))*(csc(A))', ID="X_401", classes=["center"])
    X_1987 = isogonal_conjugate(model, A, B, C, X_401, ID="X_1987", classes=["selected", "target"])
    X_54 = eval_trilinear_point(model, A, B, C, 'sec(B - C)', ID="X_54", classes=["center", "incident"])
    X_112 = eval_trilinear_point(model, A, B, C, 'a/(sin(2*B) - sin(2*C))', ID="X_112", classes=["center", "incident"])
    central_line(model, X_54, X_112, 54, 112, incident=True)
    X_237 = eval_trilinear_point(model, A, B, C, 'a**(2)*cos(A +  omega  )', ID="X_237", classes=["center", "incident"])
    X_248 = eval_trilinear_point(model, A, B, C, 'sin(2*A)*sec(A +  omega  )', ID="X_248", classes=["center", "incident"])
    central_line(model, X_237, X_248, 237, 248, incident=True)
    X_290 = eval_trilinear_point(model, A, B, C, '(csc(A))**(2)*sec(A +  omega  )', ID="X_290", classes=["center", "incident"])
    X_297 = eval_trilinear_point(model, A, B, C, 'csc(2*A)*cos(A +  omega  )', ID="X_297", classes=["center", "incident"])
    central_line(model, X_290, X_297, 290, 297, incident=True)
    return promote_point_to_top(model, X_1987)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1987 on the given reference triangle."""
    model = create_model('X_1987 = 1st LEMOINE ANTIPARALLELS POINT')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01987(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01987.json"))
    write_center_svg(
        model_acute,
        here / "x-01987.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
