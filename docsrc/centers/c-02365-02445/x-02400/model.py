"""GEOMETOR construction model for X_2400 = GIBERT-SIMSON TRANSFORM OF X_103."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    gergonne_point_of,
    intersect_lines,
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_02400(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2400 = GIBERT-SIMSON TRANSFORM OF X_103 on reference triangle ABC."""
    X_7 = gergonne_point_of(model, A, B, C, ID="X_7", classes=["center"])
    X_522 = eval_trilinear_point(model, A, B, C, '(cos(B) - cos(C))*(csc(A))', ID="X_522", classes=["center"])
    X_103 = eval_trilinear_point(model, A, B, C, 'a/((a - b)*cot(C) + (a - c)*cot(B))', ID="X_103", classes=["center"])
    X_675 = eval_trilinear_point(model, A, B, C, '(b*c/(b**(3) + c**(3) - a*(b**(2) + c**(2))))', ID="X_675", classes=["center"])
    central_line(model, X_7, X_522, 7, 522)
    central_line(model, X_103, X_675, 103, 675)
    X_2400 = intersect_lines(model, X_7, X_522, X_103, X_675, ID="X_2400", classes=["selected", "target"])
    X_677 = eval_trilinear_point(model, A, B, C, '(a/((b - c)*(b**(3) + c**(3) - 2*a**(3) + (b + c)*(a**(2) - b*c))))', ID="X_677", classes=["center", "incident"])
    X_883 = point_from_barycentrics(model, A, B, C, -1.5, 0.1, 2.4, ID="X_883", classes=["center", "incident"])
    central_line(model, X_677, X_883, 677, 883, incident=True)
    return promote_point_to_top(model, X_2400)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2400 on the given reference triangle."""
    model = create_model('X_2400 = GIBERT-SIMSON TRANSFORM OF X_103')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02400(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02400.json"))
    write_center_svg(
        model_acute,
        here / "x-02400.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
