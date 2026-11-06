"""GEOMETOR construction model for X_2030 = RADICAL TRACE OF MOSES CIRCLE AND CIRCUMCIRCLE."""

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
    midpoint,
    point_from_barycentrics,
    promote_point_to_top,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_02030(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2030 = RADICAL TRACE OF MOSES CIRCLE AND CIRCUMCIRCLE on reference triangle ABC."""
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center"])
    X_187 = eval_trilinear_point(model, A, B, C, 'a*(2*a**(2) - b**(2) - c**(2))', ID="X_187", classes=["center"])
    X_2030 = midpoint(model, X_6, X_187, ID="X_2030", classes=["selected", "target"], guide=False)
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center", "incident"])
    central_line(model, X_3, X_6, 3, 6, incident=True)
    X_230 = eval_trilinear_point(model, A, B, C, 'b*c*(a**(2)*(2*a**(2) - b**(2) - c**(2)) + (b**(2) - c**(2))**(2))', ID="X_230", classes=["center", "incident"])
    X_542 = eval_barycentric_point(model, A, B, C, '2*a**(6) - 2*a**(4)*(b**(2) + c**(2)) + a**(2)*(b**(4) + c**(4)) - (b**(2) - c**(2))**(2)*(b**(2) + c**(2))', ID="X_542", classes=["center", "incident"])
    central_line(model, X_230, X_542, 230, 542, incident=True)
    X_112 = eval_trilinear_point(model, A, B, C, 'a/(sin(2*B) - sin(2*C))', ID="X_112", classes=["center", "incident"])
    X_843 = point_from_barycentrics(model, A, B, C, 0.55581336, -0.33333326, 0.77751991, ID="X_843", classes=["center", "incident"])
    central_line(model, X_112, X_843, 112, 843, incident=True)
    return promote_point_to_top(model, X_2030)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2030 on the given reference triangle."""
    model = create_model('X_2030 = RADICAL TRACE OF MOSES CIRCLE AND CIRCUMCIRCLE')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02030(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02030.json"))
    write_center_svg(
        model_acute,
        here / "x-02030.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
