"""GEOMETOR construction model for X_1175 = 1st SARAGOSSA POINT OF X_65."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    circumcenter_of,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    isogonal_conjugate,
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_01175(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1175 = 1st SARAGOSSA POINT OF X_65 on reference triangle ABC."""
    X_442 = point_from_barycentrics(model, A, B, C, 0.3215734, 0.32603406, 0.35239254, ID="X_442", classes=["center"])
    X_1175 = isogonal_conjugate(model, A, B, C, X_442, ID="X_1175", classes=["selected", "target"])
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center", "incident"])
    X_60 = eval_trilinear_point(model, A, B, C, '1/(1 + cos(B - C))', ID="X_60", classes=["center", "incident"])
    central_line(model, X_3, X_60, 3, 60, incident=True)
    X_21 = eval_trilinear_point(model, A, B, C, '1/(cos(B) + cos(C))', ID="X_21", classes=["center", "incident"])
    X_72 = eval_trilinear_point(model, A, B, C, '(b + c)*cot(A)', ID="X_72", classes=["center", "incident"])
    central_line(model, X_21, X_72, 21, 72, incident=True)
    X_28 = eval_trilinear_point(model, A, B, C, '(tan(A))/(b + c)', ID="X_28", classes=["center", "incident"])
    X_65 = eval_trilinear_point(model, A, B, C, 'cos(B) + cos(C)', ID="X_65", classes=["center", "incident"])
    central_line(model, X_28, X_65, 28, 65, incident=True)
    return promote_point_to_top(model, X_1175)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1175 on the given reference triangle."""
    model = create_model('X_1175 = 1st SARAGOSSA POINT OF X_65')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01175(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01175.json"))
    write_center_svg(
        model_acute,
        here / "x-01175.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
