"""GEOMETOR construction model for X_3644 = REFLECTION OF X_75 IN X_192."""

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
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_03644(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3644 = REFLECTION OF X_75 IN X_192 on reference triangle ABC."""
    X_3644 = eval_trilinear_point(model, A, B, C, '(b*c*(3/a - 2/b - 2/c))', ID="X_3644", classes=["selected", "target"])
    X_2 = centroid_of(model, A, B, C, ID="X_2", classes=["center", "incident"])
    X_37 = eval_trilinear_point(model, A, B, C, 'b + c', ID="X_37", classes=["center", "incident"])
    central_line(model, X_2, X_37, 2, 37, incident=True)
    X_190 = eval_trilinear_point(model, A, B, C, 'b*c/(b - c)', ID="X_190", classes=["center", "incident"])
    X_1743 = eval_trilinear_point(model, A, B, C, '3*a - b - c', ID="X_1743", classes=["center", "incident"])
    central_line(model, X_190, X_1743, 190, 1743, incident=True)
    X_726 = eval_trilinear_point(model, A, B, C, '(a **(-3)*(b **(-1) + c **(-1)) - a **(-2)*(b **(-2) + c **(-2)))', ID="X_726", classes=["center", "incident"])
    X_3244 = eval_trilinear_point(model, A, B, C, 'b*c*(4*a - b - c)', ID="X_3244", classes=["center", "incident"])
    central_line(model, X_726, X_3244, 726, 3244, incident=True)
    return promote_point_to_top(model, X_3644)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3644 on the given reference triangle."""
    model = create_model('X_3644 = REFLECTION OF X_75 IN X_192')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03644(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03644.json"))
    write_center_svg(
        model_acute,
        here / "x-03644.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
