"""GEOMETOR construction model for X_3638 = INNER SODDY-GERGONNE POINT."""

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
    gergonne_point_of,
    incenter_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_03638(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3638 = INNER SODDY-GERGONNE POINT on reference triangle ABC."""
    X_3638 = eval_barycentric_point(model, A, B, C, '(-2*(2*a**(2)-(b+c)*a-(b-c)**(2))*S+sqrt(3)*(-a+b+c) * (2*a**(3)-(b+c)*a**(2)-(b**(2)-c**(2)) * (b-c))) * (a-b+c) * (a+b-c)', ID="X_3638", classes=["selected", "target"])
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center", "incident"])
    X_7 = gergonne_point_of(model, A, B, C, ID="X_7", classes=["center", "incident"])
    central_line(model, X_1, X_7, 1, 7, incident=True)
    X_14 = eval_trilinear_point(model, A, B, C, 'csc(A -  pi  /3)', ID="X_14", classes=["center", "incident"])
    X_226 = eval_trilinear_point(model, A, B, C, '(csc(A))*(cos(B) + cos(C))', ID="X_226", classes=["center", "incident"])
    central_line(model, X_14, X_226, 14, 226, incident=True)
    X_57 = eval_trilinear_point(model, A, B, C, '1/(b + c - a)', ID="X_57", classes=["center", "incident"])
    X_1277 = eval_trilinear_point(model, A, B, C, '(sqrt(3/4) - sin(A -  pi  /3) + sin(B -  pi  /3) + sin(C -  pi  /3))', ID="X_1277", classes=["center", "incident"])
    central_line(model, X_57, X_1277, 57, 1277, incident=True)
    return promote_point_to_top(model, X_3638)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3638 on the given reference triangle."""
    model = create_model('X_3638 = INNER SODDY-GERGONNE POINT')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03638(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03638.json"))
    write_center_svg(
        model_acute,
        here / "x-03638.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
