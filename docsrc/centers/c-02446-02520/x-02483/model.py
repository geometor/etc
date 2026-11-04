"""GEOMETOR construction model for X_2483 = RADICAL CENTER OF {CIRCUMCIRCLE, 1st LEMOINE CIRCLE, BEVAN CIRCLE}."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_barycentric_point,
    eval_trilinear_point,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_02483(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2483 = RADICAL CENTER OF {CIRCUMCIRCLE, 1st LEMOINE CIRCLE, BEVAN CIRCLE} on reference triangle ABC."""
    X_2483 = eval_trilinear_point(model, A, B, C, '(a*(b - c)*(a**(2) + b**(2) + c**(2) + b*c))', ID="X_2483", classes=["selected", "target"])
    X_44 = eval_trilinear_point(model, A, B, C, 'b + c - 2*a', ID="X_44", classes=["center", "incident"])
    X_513 = eval_trilinear_point(model, A, B, C, 'b - c', ID="X_513", classes=["center", "incident"])
    central_line(model, X_44, X_513, 44, 513, incident=True)
    X_918 = eval_barycentric_point(model, A, B, C, '((b - c)*(b**(2) + c**(2) -a*b - a*c))', ID="X_918", classes=["center", "incident"])
    X_1019 = eval_trilinear_point(model, A, B, C, '(b - c)/(b + c)', ID="X_1019", classes=["center", "incident"])
    central_line(model, X_918, X_1019, 918, 1019, incident=True)
    X_512 = eval_trilinear_point(model, A, B, C, 'a*(b**(2) - c**(2))', ID="X_512", classes=["center", "incident"])
    X_1691 = eval_trilinear_point(model, A, B, C, 'sin(A - 2*omega  )', ID="X_1691", classes=["center", "incident"])
    central_line(model, X_512, X_1691, 512, 1691, incident=True)
    return promote_point_to_top(model, X_2483)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2483 on the given reference triangle."""
    model = create_model('X_2483 = RADICAL CENTER OF {CIRCUMCIRCLE, 1st LEMOINE CIRCLE, BEVAN CIRCLE}')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02483(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02483.json"))
    write_center_svg(
        model_acute,
        here / "x-02483.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
