"""GEOMETOR construction model for X_2411 = GIBERT-SIMSON TRANSFORM OF X_477."""

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
    intersect_lines,
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_02411(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2411 = GIBERT-SIMSON TRANSFORM OF X_477 on reference triangle ABC."""
    X_477 = eval_trilinear_point(model, A, B, C, '1/(4*cos(A) + cos(A - 2*B) + cos(A - 2*C) - 3*cos(B - C))', ID="X_477", classes=["center"])
    X_842 = eval_barycentric_point(model, A, B, C, 'a**(2)/(2*a**(6) - 2*a**(4)*(b**(2) + c**(2)) + a**(2)*(b**(4) + c**(4)) - (b**(2) - c**(2))**(2)*(b**(2) + c**(2)))', ID="X_842", classes=["center"])
    X_249 = eval_trilinear_point(model, A, B, C, '(csc(A))*(csc(B - C))**(2)', ID="X_249", classes=["center"])
    X_2407 = eval_trilinear_point(model, A, B, C, '(csc(C - A)*cos(C) - csc(A - B)*cos(B))*(csc(B - C)/a)**(2)', ID="X_2407", classes=["center"])
    central_line(model, X_477, X_842, 477, 842)
    central_line(model, X_249, X_2407, 249, 2407)
    X_2411 = intersect_lines(model, X_477, X_842, X_249, X_2407, ID="X_2411", classes=["selected", "target"])
    X_323 = eval_trilinear_point(model, A, B, C, 'sin(3*A)*(csc(A))**(2)', ID="X_323", classes=["center", "incident"])
    X_2436 = point_from_barycentrics(model, A, B, C, 0.95620211, -0.024683707, 0.0684816, ID="X_2436", classes=["center", "incident"])
    central_line(model, X_323, X_2436, 323, 2436, incident=True)
    return promote_point_to_top(model, X_2411)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2411 on the given reference triangle."""
    model = create_model('X_2411 = GIBERT-SIMSON TRANSFORM OF X_477')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02411(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02411.json"))
    write_center_svg(
        model_acute,
        here / "x-02411.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
