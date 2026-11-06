"""GEOMETOR construction model for X_3562 = SS(sin A → cos A) OF X_1621."""

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
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_03562(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3562 = SS(sin A → cos A) OF X_1621 on reference triangle ABC."""
    X_3562 = eval_trilinear_point(model, A, B, C, '((cos(A))**(2) - cos(B)*cos(C) - cos(C)*cos(A) - cos(A)*cos(B))', ID="X_3562", classes=["selected", "target"])
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center", "incident"])
    X_21 = eval_trilinear_point(model, A, B, C, '1/(cos(B) + cos(C))', ID="X_21", classes=["center", "incident"])
    central_line(model, X_1, X_21, 1, 21, incident=True)
    X_40 = eval_trilinear_point(model, A, B, C, 'cos(B) + cos(C) - cos(A) - 1', ID="X_40", classes=["center", "incident"])
    X_77 = eval_trilinear_point(model, A, B, C, '1/(1 + sec(A))', ID="X_77", classes=["center", "incident"])
    central_line(model, X_40, X_77, 40, 77, incident=True)
    X_20 = eval_trilinear_point(model, A, B, C, 'cos(A) - cos(B)*cos(C)', ID="X_20", classes=["center", "incident"])
    X_222 = eval_trilinear_point(model, A, B, C, 'cos(A)*tan(A/2)', ID="X_222", classes=["center", "incident"])
    central_line(model, X_20, X_222, 20, 222, incident=True)
    return promote_point_to_top(model, X_3562)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3562 on the given reference triangle."""
    model = create_model('X_3562 = SS(sin A → cos A) OF X_1621')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03562(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03562.json"))
    write_center_svg(
        model_acute,
        here / "x-03562.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
