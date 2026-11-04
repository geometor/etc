"""GEOMETOR construction model for X_1276 = 2nd EVANS PERSPECTOR."""

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
    mittenpunkt_of,
    orthocenter_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_01276(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1276 = 2nd EVANS PERSPECTOR on reference triangle ABC."""
    X_1276 = eval_trilinear_point(model, A, B, C, 'sqrt(3/4) + cos(A - pi /6) - cos(B - pi /6) - cos(C - pi /6)', ID="X_1276", classes=["selected", "target"])
    X_4 = orthocenter_of(model, A, B, C, ID="X_4", classes=["center", "incident"])
    X_9 = mittenpunkt_of(model, A, B, C, ID="X_9", classes=["center", "incident"])
    central_line(model, X_4, X_9, 4, 9, incident=True)
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center", "incident"])
    X_15 = eval_trilinear_point(model, A, B, C, 'sin(A + pi /3)', ID="X_15", classes=["center", "incident"])
    central_line(model, X_1, X_15, 1, 15, incident=True)
    X_14 = eval_trilinear_point(model, A, B, C, 'csc(A - pi /3)', ID="X_14", classes=["center", "incident"])
    X_484 = eval_trilinear_point(model, A, B, C, '1 + 2*(cos(A) - cos(B) - cos(C))', ID="X_484", classes=["center", "incident"])
    central_line(model, X_14, X_484, 14, 484, incident=True)
    return promote_point_to_top(model, X_1276)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1276 on the given reference triangle."""
    model = create_model('X_1276 = 2nd EVANS PERSPECTOR')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01276(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01276.json"))
    write_center_svg(
        model_acute,
        here / "x-01276.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
