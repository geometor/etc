"""GEOMETOR construction model for X_2432 = ISOGONAL CONJUGATE OF X_2406."""

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
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_02432(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2432 = ISOGONAL CONJUGATE OF X_2406 on reference triangle ABC."""
    X_2406 = point_from_barycentrics(model, A, B, C, -0.30434783, 0.17391304, 1.1304348, ID="X_2406", classes=["center"])
    X_2432 = isogonal_conjugate(model, A, B, C, X_2406, ID="X_2432", classes=["selected", "target"])
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center", "incident"])
    X_652 = eval_trilinear_point(model, A, B, C, 'sec(B) - sec(C)', ID="X_652", classes=["center", "incident"])
    central_line(model, X_6, X_652, 6, 652, incident=True)
    X_19 = eval_trilinear_point(model, A, B, C, 'tan(A)', ID="X_19", classes=["center", "incident"])
    X_650 = eval_trilinear_point(model, A, B, C, 'cos(B) - cos(C)', ID="X_650", classes=["center", "incident"])
    central_line(model, X_19, X_650, 19, 650, incident=True)
    X_57 = eval_trilinear_point(model, A, B, C, '1/(b + c - a)', ID="X_57", classes=["center", "incident"])
    X_905 = eval_trilinear_point(model, A, B, C, '(b - c)*cot(A)', ID="X_905", classes=["center", "incident"])
    central_line(model, X_57, X_905, 57, 905, incident=True)
    return promote_point_to_top(model, X_2432)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2432 on the given reference triangle."""
    model = create_model('X_2432 = ISOGONAL CONJUGATE OF X_2406')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02432(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02432.json"))
    write_center_svg(
        model_acute,
        here / "x-02432.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
