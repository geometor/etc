"""GEOMETOR construction model for X(847) = X(5)-CROSS CONJUGATE OF X(4)."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    centroid_of,
    cevapoint,
    construct_baseline_triangle,
    create_model,
    eval_barycentric_point,
    eval_trilinear_point,
    orthocenter_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00847(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(847) = X(5)-CROSS CONJUGATE OF X(4) on reference triangle ABC."""
    X_485 = eval_trilinear_point(model, A, B, C, 'sec(A - pi /4)', ID="X(485)", classes=["center"])
    X_486 = eval_trilinear_point(model, A, B, C, 'sec(A + pi /4)', ID="X(486)", classes=["center"])
    X_847 = cevapoint(model, A, B, C, X_485, X_486, ID="X(847)", classes=["selected", "target"])
    X_4 = orthocenter_of(model, A, B, C, ID="X(4)", classes=["center", "incident"])
    X_52 = eval_trilinear_point(model, A, B, C, 'cos(2*A)*cos(B - C)', ID="X(52)", classes=["center", "incident"])
    central_line(model, X_4, X_52, 4, 52, incident=True)
    X_24 = eval_trilinear_point(model, A, B, C, 'sec(A)*cos(2*A)', ID="X(24)", classes=["center", "incident"])
    X_96 = eval_trilinear_point(model, A, B, C, 'sec(2*A)*sec(B - C)', ID="X(96)", classes=["center", "incident"])
    central_line(model, X_24, X_96, 24, 96, incident=True)
    X_2 = centroid_of(model, A, B, C, ID="X(2)", classes=["center", "incident"])
    X_254 = eval_barycentric_point(model, A, B, C, '1/((a**(2) - b**(2) - c**(2))*(a**(6) - 3*a**(4)*(b**(2) + c**(2)) + a**(2)*(3*b**(4) - 2*b**(2)*c**(2) + 3*c**(4)) - (b**(2) - c**(2))**(2)*(b**(2) + c**(2))))', ID="X(254)", classes=["center", "incident"])
    central_line(model, X_2, X_254, 2, 254, incident=True)
    return promote_point_to_top(model, X_847)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(847) on the given reference triangle."""
    model = create_model('X(847) = X(5)-CROSS CONJUGATE OF X(4)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00847(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00847.json"))
    write_center_svg(
        model_acute,
        here / "x-00847.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
