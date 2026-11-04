"""GEOMETOR construction model for X_1741 = MIMOSA TRANSFORM OF X_189."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    centroid_of,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    gergonne_point_of,
    intersect_lines,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_01741(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1741 = MIMOSA TRANSFORM OF X_189 on reference triangle ABC."""
    X_2 = centroid_of(model, A, B, C, ID="X_2", classes=["center"])
    X_7 = gergonne_point_of(model, A, B, C, ID="X_7", classes=["center"])
    X_46 = eval_trilinear_point(model, A, B, C, 'cos(B) + cos(C) - cos(A)', ID="X_46", classes=["center"])
    X_281 = eval_trilinear_point(model, A, B, C, 'sec(A)*cot(A/2)', ID="X_281", classes=["center"])
    central_line(model, X_2, X_7, 2, 7)
    central_line(model, X_46, X_281, 46, 281)
    X_1741 = intersect_lines(model, X_2, X_7, X_46, X_281, ID="X_1741", classes=["selected", "target"])
    X_19 = eval_trilinear_point(model, A, B, C, 'tan(A)', ID="X_19", classes=["center", "incident"])
    X_1158 = eval_trilinear_point(model, A, B, C, 'a**(6) - b**(6) - c**(6) + b**(2)*c**(2)*(b**(2) + c**(2)) + 3*a**(2)*(b**(4) + c**(4) - a**(2)*b**(2) - a**(2)*c**(2)) + 2*a*b*c*(a**(3) - b**(3) - c**(3) - a*b*c + (a**(2) + b*c)*(b + c) - a*b**(2) - a*c**(2))', ID="X_1158", classes=["center", "incident"])
    central_line(model, X_19, X_1158, 19, 1158, incident=True)
    return promote_point_to_top(model, X_1741)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1741 on the given reference triangle."""
    model = create_model('X_1741 = MIMOSA TRANSFORM OF X_189')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01741(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01741.json"))
    write_center_svg(
        model_acute,
        here / "x-01741.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
