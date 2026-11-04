"""GEOMETOR construction model for X_1652 = 4th EVANS PERSPECTOR."""

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
    incenter_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_01652(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1652 = 4th EVANS PERSPECTOR on reference triangle ABC."""
    X_1652 = eval_trilinear_point(model, A, B, C, 'sqrt(3/4) - cos(A -  pi  /6) + cos(B -  pi  /6) + cos(C -  pi  /6)', ID="X_1652", classes=["selected", "target"])
    X_2 = centroid_of(model, A, B, C, ID="X_2", classes=["center", "incident"])
    X_7 = gergonne_point_of(model, A, B, C, ID="X_7", classes=["center", "incident"])
    central_line(model, X_2, X_7, 2, 7, incident=True)
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center", "incident"])
    X_15 = eval_trilinear_point(model, A, B, C, 'sin(A +  pi  /3)', ID="X_15", classes=["center", "incident"])
    central_line(model, X_1, X_15, 1, 15, incident=True)
    X_396 = eval_trilinear_point(model, A, B, C, 'cos(B - C) + 2*cos(A -  pi  /3)', ID="X_396", classes=["center", "incident"])
    X_554 = eval_trilinear_point(model, A, B, C, 'sec(A/2)*csc(A/2 +  pi  /3)', ID="X_554", classes=["center", "incident"])
    central_line(model, X_396, X_554, 396, 554, incident=True)
    return promote_point_to_top(model, X_1652)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1652 on the given reference triangle."""
    model = create_model('X_1652 = 4th EVANS PERSPECTOR')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01652(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01652.json"))
    write_center_svg(
        model_acute,
        here / "x-01652.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
