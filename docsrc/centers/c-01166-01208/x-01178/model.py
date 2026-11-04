"""GEOMETOR construction model for X_1178 = 1st SARAGOSSA POINT OF X_82."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    promote_point_to_top,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_01178(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1178 = 1st SARAGOSSA POINT OF X_82 on reference triangle ABC."""
    X_1178 = eval_trilinear_point(model, A, B, C, '(a/((b + c)*(a**(2) + b*c)))', ID="X_1178", classes=["selected", "target"])
    X_21 = eval_trilinear_point(model, A, B, C, '1/(cos(B) + cos(C))', ID="X_21", classes=["center", "incident"])
    X_238 = eval_trilinear_point(model, A, B, C, 'a**(2) - b*c', ID="X_238", classes=["center", "incident"])
    central_line(model, X_21, X_238, 21, 238, incident=True)
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center", "incident"])
    X_694 = eval_trilinear_point(model, A, B, C, 'a/(a**(4) - b**(2)*c**(2))', ID="X_694", classes=["center", "incident"])
    central_line(model, X_6, X_694, 6, 694, incident=True)
    X_82 = eval_trilinear_point(model, A, B, C, '1/(b**(2) + c**(2))', ID="X_82", classes=["center", "incident"])
    X_662 = eval_trilinear_point(model, A, B, C, '1/(cot(B) - cot(C))', ID="X_662", classes=["center", "incident"])
    central_line(model, X_82, X_662, 82, 662, incident=True)
    return promote_point_to_top(model, X_1178)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1178 on the given reference triangle."""
    model = create_model('X_1178 = 1st SARAGOSSA POINT OF X_82')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01178(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01178.json"))
    write_center_svg(
        model_acute,
        here / "x-01178.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
