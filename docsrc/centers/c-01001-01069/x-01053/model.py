"""GEOMETOR construction model for X_1053 = POINT ALHENA."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    incenter_of,
    intersect_lines,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_01053(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1053 = POINT ALHENA on reference triangle ABC."""
    X_238 = eval_trilinear_point(model, A, B, C, 'a**(2) - b*c', ID="X_238", classes=["center"])
    X_517 = eval_trilinear_point(model, A, B, C, '-1 + cos(B) + cos(C)', ID="X_517", classes=["center"])
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center"])
    X_1110 = eval_trilinear_point(model, A, B, C, '((a/(b - c))**(2))', ID="X_1110", classes=["center"])
    central_line(model, X_238, X_517, 238, 517)
    central_line(model, X_1, X_1110, 1, 1110)
    X_1053 = intersect_lines(model, X_238, X_517, X_1, X_1110, ID="X_1053", classes=["selected", "target"])
    X_905 = eval_trilinear_point(model, A, B, C, '(b - c)*cot(A)', ID="X_905", classes=["center", "incident"])
    X_1054 = eval_trilinear_point(model, A, B, C, 'b**(2) + c**(2) - a**(2) - 3*b*c + a*b + a*c', ID="X_1054", classes=["center", "incident"])
    central_line(model, X_905, X_1054, 905, 1054, incident=True)
    return promote_point_to_top(model, X_1053)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1053 on the given reference triangle."""
    model = create_model('X_1053 = POINT ALHENA')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01053(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01053.json"))
    write_center_svg(
        model_acute,
        here / "x-01053.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
