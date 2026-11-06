"""GEOMETOR construction model for X_3427 = X_3-VERTEX CONJUGATE OF X_7."""

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
    mittenpunkt_of,
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_03427(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3427 = X_3-VERTEX CONJUGATE OF X_7 on reference triangle ABC."""
    X_3427 = eval_barycentric_point(model, A, B, C, '(1/(a**(5) - a**(4)*(b + c) - 2*a**(3)*(b**(2) + c**(2)) + 2*a**(2)*(b + c)*(b - c)**(2) + a*(b**(4) + 6*b**(2)*c**(2) + c**(4)) - (b + c)*(b - c)**(4)))', ID="X_3427", classes=["selected", "target"])
    X_9 = mittenpunkt_of(model, A, B, C, ID="X_9", classes=["center", "incident"])
    X_515 = eval_trilinear_point(model, A, B, C, '(b + c)*sec(A) - b*sec(B) - c*sec(C)', ID="X_515", classes=["center", "incident"])
    central_line(model, X_9, X_515, 9, 515, incident=True)
    X_104 = eval_trilinear_point(model, A, B, C, '1/(-1 + cos(B) + cos(C))', ID="X_104", classes=["center", "incident"])
    X_1617 = point_from_barycentrics(model, A, B, C, 0.077591558, 0.25325885, 0.6691496, ID="X_1617", classes=["center", "incident"])
    central_line(model, X_104, X_1617, 104, 1617, incident=True)
    X_943 = eval_trilinear_point(model, A, B, C, '(1/(2*a*b*c + (b + c)*(a - b + c)*(a + b - c)))', ID="X_943", classes=["center", "incident"])
    X_944 = eval_trilinear_point(model, A, B, C, 'b*c*(3*a**(4) - 2*a**(3)*(b + c) + (b - c)**(2)*(2*a*b + 2*a*c - 2*b*c - b**(2) - c**(2) - 2*a**(2)))', ID="X_944", classes=["center", "incident"])
    central_line(model, X_943, X_944, 943, 944, incident=True)
    return promote_point_to_top(model, X_3427)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3427 on the given reference triangle."""
    model = create_model('X_3427 = X_3-VERTEX CONJUGATE OF X_7')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03427(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03427.json"))
    write_center_svg(
        model_acute,
        here / "x-03427.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
