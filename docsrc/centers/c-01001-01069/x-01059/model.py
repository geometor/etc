"""GEOMETOR construction model for X_1059 = ISOGONAL CONJUGATE OF X_1058."""

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
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_01059(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1059 = ISOGONAL CONJUGATE OF X_1058 on reference triangle ABC."""
    X_1058 = eval_trilinear_point(model, A, B, C, '(2 - cos(B)*cos(C))', ID="X_1058", classes=["center"])
    X_1059 = isogonal_conjugate(model, A, B, C, X_1058, ID="X_1059", classes=["selected", "target"])
    X_78 = eval_trilinear_point(model, A, B, C, '1/(1 - sec(A))', ID="X_78", classes=["center", "incident"])
    X_999 = eval_trilinear_point(model, A, B, C, '2 - cos(A)', ID="X_999", classes=["center", "incident"])
    central_line(model, X_78, X_999, 78, 999, incident=True)
    X_29 = eval_trilinear_point(model, A, B, C, '(sec(A))/(cos(B) + cos(C))', ID="X_29", classes=["center", "incident"])
    X_1056 = eval_trilinear_point(model, A, B, C, '(2 + cos(B)*cos(C))', ID="X_1056", classes=["center", "incident"])
    central_line(model, X_29, X_1056, 29, 1056, incident=True)
    X_73 = eval_trilinear_point(model, A, B, C, 'sec(B) + sec(C)', ID="X_73", classes=["center", "incident"])
    X_1057 = eval_trilinear_point(model, A, B, C, '(1/(2 + cos(B)*cos(C)))', ID="X_1057", classes=["center", "incident"])
    central_line(model, X_73, X_1057, 73, 1057, incident=True)
    return promote_point_to_top(model, X_1059)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1059 on the given reference triangle."""
    model = create_model('X_1059 = ISOGONAL CONJUGATE OF X_1058')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01059(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01059.json"))
    write_center_svg(
        model_acute,
        here / "x-01059.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
