"""GEOMETOR construction model for X_1391 = ISOGONAL CONJUGATE OF X_1387."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    isogonal_conjugate,
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_01391(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1391 = ISOGONAL CONJUGATE OF X_1387 on reference triangle ABC."""
    X_1387 = point_from_barycentrics(model, A, B, C, 0.25, 0.5, 0.25, ID="X_1387", classes=["center"])
    X_1391 = isogonal_conjugate(model, A, B, C, X_1387, ID="X_1391", classes=["selected", "target"])
    X_517 = eval_trilinear_point(model, A, B, C, '-1 + cos(B) + cos(C)', ID="X_517", classes=["center", "incident"])
    X_1443 = eval_trilinear_point(model, A, B, C, '((1 - 2*cos(A))/(1 + cos(A)))', ID="X_1443", classes=["center", "incident"])
    central_line(model, X_517, X_1443, 517, 1443, incident=True)
    return promote_point_to_top(model, X_1391)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1391 on the given reference triangle."""
    model = create_model('X_1391 = ISOGONAL CONJUGATE OF X_1387')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01391(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01391.json"))
    write_center_svg(
        model_acute,
        here / "x-01391.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
