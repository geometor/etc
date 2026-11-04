"""GEOMETOR construction model for X_1692 = RADICAL TRACE OF CIRCUMCIRCLE AND 2nd LEMOINE CIRCLE."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    circumcenter_of,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    promote_point_to_top,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_01692(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1692 = RADICAL TRACE OF CIRCUMCIRCLE AND 2nd LEMOINE CIRCLE on reference triangle ABC."""
    X_1692 = eval_trilinear_point(model, A, B, C, '2*sin(A - 2*omega  ) + sin(A + 2*omega  ) - sin(A)', ID="X_1692", classes=["selected", "target"])
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center", "incident"])
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center", "incident"])
    central_line(model, X_3, X_6, 3, 6, incident=True)
    X_114 = eval_trilinear_point(model, A, B, C, 'b*c*(b*sec(B +  omega  ) + c*sec(C +  omega  ))', ID="X_114", classes=["center", "incident"])
    X_230 = eval_trilinear_point(model, A, B, C, 'b*c*(a**(2)*(2*a**(2) - b**(2) - c**(2)) + (b**(2) - c**(2))**(2))', ID="X_230", classes=["center", "incident"])
    central_line(model, X_114, X_230, 114, 230, incident=True)
    X_184 = eval_trilinear_point(model, A, B, C, 'a**(2)*cos(A)', ID="X_184", classes=["center", "incident"])
    X_1196 = eval_trilinear_point(model, A, B, C, '(a*(b**(4) + c**(4) + a**(2)*b**(2) + a**(2)*c**(2) - 2*b**(2)*c**(2)))', ID="X_1196", classes=["center", "incident"])
    central_line(model, X_184, X_1196, 184, 1196, incident=True)
    return promote_point_to_top(model, X_1692)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1692 on the given reference triangle."""
    model = create_model('X_1692 = RADICAL TRACE OF CIRCUMCIRCLE AND 2nd LEMOINE CIRCLE')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01692(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01692.json"))
    write_center_svg(
        model_acute,
        here / "x-01692.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
