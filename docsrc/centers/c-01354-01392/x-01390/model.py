"""GEOMETOR construction model for X_1390 = ISOGONAL CONJUGATE OF X_1386."""

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


def construct_x_01390(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1390 = ISOGONAL CONJUGATE OF X_1386 on reference triangle ABC."""
    X_1386 = eval_trilinear_point(model, A, B, C, '(a*(a + b + c) + (a**(2) + b**(2) + c**(2)))', ID="X_1386", classes=["center"])
    X_1390 = isogonal_conjugate(model, A, B, C, X_1386, ID="X_1390", classes=["selected", "target"])
    X_38 = eval_trilinear_point(model, A, B, C, 'b**(2) + c**(2)', ID="X_38", classes=["center", "incident"])
    X_57 = eval_trilinear_point(model, A, B, C, '1/(b + c - a)', ID="X_57", classes=["center", "incident"])
    central_line(model, X_38, X_57, 38, 57, incident=True)
    X_37 = eval_trilinear_point(model, A, B, C, 'b + c', ID="X_37", classes=["center", "incident"])
    X_105 = eval_trilinear_point(model, A, B, C, '1/(b**(2) + c**(2) - a*(b + c))', ID="X_105", classes=["center", "incident"])
    central_line(model, X_37, X_105, 37, 105, incident=True)
    X_81 = eval_trilinear_point(model, A, B, C, '1/(b + c)', ID="X_81", classes=["center", "incident"])
    X_518 = eval_trilinear_point(model, A, B, C, '(a*b + a*c - b**(2) - c**(2))', ID="X_518", classes=["center", "incident"])
    central_line(model, X_81, X_518, 81, 518, incident=True)
    return promote_point_to_top(model, X_1390)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1390 on the given reference triangle."""
    model = create_model('X_1390 = ISOGONAL CONJUGATE OF X_1386')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01390(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01390.json"))
    write_center_svg(
        model_acute,
        here / "x-01390.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
