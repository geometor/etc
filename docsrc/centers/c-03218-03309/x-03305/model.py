"""GEOMETOR construction model for X_3305 = INTERSECTION OF LINES X_1X_748 AND X_2X_7."""

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
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_03305(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3305 = INTERSECTION OF LINES X_1X_748 AND X_2X_7 on reference triangle ABC."""
    X_3305 = eval_trilinear_point(model, A, B, C, '(2 + cos(A))*csc(A)', ID="X_3305", classes=["selected", "target"])
    X_2 = centroid_of(model, A, B, C, ID="X_2", classes=["center", "incident"])
    X_7 = gergonne_point_of(model, A, B, C, ID="X_7", classes=["center", "incident"])
    central_line(model, X_2, X_7, 2, 7, incident=True)
    X_78 = eval_trilinear_point(model, A, B, C, '1/(1 - sec(A))', ID="X_78", classes=["center", "incident"])
    X_405 = eval_trilinear_point(model, A, B, C, 'b*c*(a + b + c) + a*b*c*cos(A)', ID="X_405", classes=["center", "incident"])
    central_line(model, X_78, X_405, 78, 405, incident=True)
    X_19 = eval_trilinear_point(model, A, B, C, 'tan(A)', ID="X_19", classes=["center", "incident"])
    X_469 = point_from_barycentrics(model, A, B, C, 0.14569854, 0.21687036, 0.6374311, ID="X_469", classes=["center", "incident"])
    central_line(model, X_19, X_469, 19, 469, incident=True)
    return promote_point_to_top(model, X_3305)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3305 on the given reference triangle."""
    model = create_model('X_3305 = INTERSECTION OF LINES X_1X_748 AND X_2X_7')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03305(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03305.json"))
    write_center_svg(
        model_acute,
        here / "x-03305.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
