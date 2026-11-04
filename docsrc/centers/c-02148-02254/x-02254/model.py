"""GEOMETOR construction model for X_2254 = X_2-ISOCONJUGATE OF X_919."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    cevapoint,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    feuerbach_point_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_02254(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2254 = X_2-ISOCONJUGATE OF X_919 on reference triangle ABC."""
    X_665 = eval_trilinear_point(model, A, B, C, 'a*((a - b)**(2)*(a + b - c) - (c - a)**(2)*(c + a - b))', ID="X_665", classes=["center"])
    X_926 = eval_trilinear_point(model, A, B, C, 'a*(a - b - c)*(b - c)*(a*b + a*c - b**(2) - c**(2))', ID="X_926", classes=["center"])
    X_2254 = cevapoint(model, A, B, C, X_665, X_926, ID="X_2254", classes=["selected", "target"])
    X_103 = eval_trilinear_point(model, A, B, C, 'a/((a - b)*cot(C) + (a - c)*cot(B))', ID="X_103", classes=["center", "incident"])
    X_105 = eval_trilinear_point(model, A, B, C, '1/(b**(2) + c**(2) - a*(b + c))', ID="X_105", classes=["center", "incident"])
    central_line(model, X_103, X_105, 103, 105, incident=True)
    X_100 = eval_trilinear_point(model, A, B, C, '1/(b - c)', ID="X_100", classes=["center", "incident"])
    X_109 = eval_trilinear_point(model, A, B, C, 'a/(cos(B) - cos(C))', ID="X_109", classes=["center", "incident"])
    central_line(model, X_100, X_109, 100, 109, incident=True)
    X_11 = feuerbach_point_of(model, A, B, C, ID="X_11", classes=["center", "incident"])
    X_244 = eval_trilinear_point(model, A, B, C, '(b - c)**(2)', ID="X_244", classes=["center", "incident"])
    central_line(model, X_11, X_244, 11, 244, incident=True)
    return promote_point_to_top(model, X_2254)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2254 on the given reference triangle."""
    model = create_model('X_2254 = X_2-ISOCONJUGATE OF X_919')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02254(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02254.json"))
    write_center_svg(
        model_acute,
        here / "x-02254.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
