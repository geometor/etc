"""GEOMETOR construction model for X_3471 = ISOGONAL CONJUGATE OF X_3470."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_barycentric_point,
    eval_trilinear_point,
    isogonal_conjugate,
    nine_point_center_of,
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_03471(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3471 = ISOGONAL CONJUGATE OF X_3470 on reference triangle ABC."""
    X_3470 = point_from_barycentrics(model, A, B, C, 0.41095246, -0.012346313, 0.60139385, ID="X_3470", classes=["center"])
    X_3471 = isogonal_conjugate(model, A, B, C, X_3470, ID="X_3471", classes=["selected", "target"])
    X_140 = eval_trilinear_point(model, A, B, C, '2*cos(A) + cos(B - C)', ID="X_140", classes=["center", "incident"])
    X_523 = eval_trilinear_point(model, A, B, C, 'sin(B -C)', ID="X_523", classes=["center", "incident"])
    central_line(model, X_140, X_523, 140, 523, incident=True)
    X_477 = eval_trilinear_point(model, A, B, C, '1/(4*cos(A) + cos(A - 2*B) + cos(A - 2*C) - 3*cos(B - C))', ID="X_477", classes=["center", "incident"])
    X_550 = eval_trilinear_point(model, A, B, C, '- cos(B - C) + 4*cos(A)', ID="X_550", classes=["center", "incident"])
    central_line(model, X_477, X_550, 477, 550, incident=True)
    X_5 = nine_point_center_of(model, A, B, C, ID="X_5", classes=["center", "incident"])
    X_1117 = eval_barycentric_point(model, A, B, C, '(a**(2)-a*b+b**(2)-c**(2))*(a**(2)+a*b+b**(2)-c**(2))*(a**(2)-b**(2)-a*c+c**(2))*(a**(2)-b**(2)+a*c+c**(2))*(a**(6)-a**(4)*b**(2)-a**(2)*b**(4)+b**(6)-3*a**(4)*c**(2)+a**(2)*b**(2)*c**(2)-3*b**(4)*c**(2)+3*a**(2)*c**(4)+3*b**(2)*c**(4)-c**(6))*(a**(6)-3*a**(4)*b**(2)+3*a**(2)*b**(4)-b**(6)-a**(4)*c**(2)+a**(2)*b**(2)*c**(2)+3*b**(4)*c**(2)-a**(2)*c**(4)-3*b**(2)*c**(4)+c**(6))*(a**(8)-4*a**(6)*b**(2)+6*a**(4)*b**(4)-4*a**(2)*b**(6)+b**(8)-4*a**(6)*c**(2)+a**(4)*b**(2)*c**(2)+a**(2)*b**(4)*c**(2)+2*b**(6)*c**(2)+6*a**(4)*c**(4)+a**(2)*b**(2)*c**(4)-6*b**(4)*c**(4)-4*a**(2)*c**(6)+2*b**(2)*c**(6)+c**(8))', ID="X_1117", classes=["center", "incident"])
    central_line(model, X_5, X_1117, 5, 1117, incident=True)
    return promote_point_to_top(model, X_3471)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3471 on the given reference triangle."""
    model = create_model('X_3471 = ISOGONAL CONJUGATE OF X_3470')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03471(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03471.json"))
    write_center_svg(
        model_acute,
        here / "x-03471.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
