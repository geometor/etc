"""GEOMETOR construction model for X_1661 = 2nd GRINBERG MIDPOINTS PERSPECTOR."""

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
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_01661(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1661 = 2nd GRINBERG MIDPOINTS PERSPECTOR on reference triangle ABC."""
    X_20 = eval_trilinear_point(model, A, B, C, 'cos(A) - cos(B)*cos(C)', ID="X_20", classes=["center"])
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center"])
    X_1661 = ceva_conjugate(model, A, B, C, X_20, X_6, ID="X_1661", classes=["selected", "target"])
    X_25 = eval_trilinear_point(model, A, B, C, 'sin(A)*tan(A)', ID="X_25", classes=["center", "incident"])
    X_393 = eval_trilinear_point(model, A, B, C, 'b*c*(tan(A))**(2)', ID="X_393", classes=["center", "incident"])
    central_line(model, X_25, X_393, 25, 393, incident=True)
    X_154 = eval_trilinear_point(model, A, B, C, '(cos(A) - cos(B)*cos(C))*a**(2)', ID="X_154", classes=["center", "incident"])
    X_577 = eval_trilinear_point(model, A, B, C, 'sin(A)*(cos(A))**(2)', ID="X_577", classes=["center", "incident"])
    central_line(model, X_154, X_577, 154, 577, incident=True)
    X_1619 = point_from_barycentrics(model, A, B, C, 1.6442071, 2.1299263, -2.7741334, ID="X_1619", classes=["center", "incident"])
    X_1624 = point_from_barycentrics(model, A, B, C, 0.18909568, -0.24246678, 1.0533711, ID="X_1624", classes=["center", "incident"])
    central_line(model, X_1619, X_1624, 1619, 1624, incident=True)
    return promote_point_to_top(model, X_1661)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1661 on the given reference triangle."""
    model = create_model('X_1661 = 2nd GRINBERG MIDPOINTS PERSPECTOR')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01661(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01661.json"))
    write_center_svg(
        model_acute,
        here / "x-01661.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
