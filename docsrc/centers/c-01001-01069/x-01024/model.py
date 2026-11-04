"""GEOMETOR construction model for X_1024 = INTERSECTION OF LINES X_6X_513 ANDX(9)X_522."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    mittenpunkt_of,
    promote_point_to_top,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_01024(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1024 = INTERSECTION OF LINES X_6X_513 ANDX(9)X_522 on reference triangle ABC."""
    X_1024 = eval_trilinear_point(model, A, B, C, '((b - c)*(b + c - a)/(b**(2) + c**(2) - a*(b + c)))', ID="X_1024", classes=["selected", "target"])
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center", "incident"])
    X_513 = eval_trilinear_point(model, A, B, C, 'b - c', ID="X_513", classes=["center", "incident"])
    central_line(model, X_6, X_513, 6, 513, incident=True)
    X_9 = mittenpunkt_of(model, A, B, C, ID="X_9", classes=["center", "incident"])
    X_522 = eval_trilinear_point(model, A, B, C, '(cos(B) - cos(C))*(csc(A))', ID="X_522", classes=["center", "incident"])
    central_line(model, X_9, X_522, 9, 522, incident=True)
    X_55 = eval_trilinear_point(model, A, B, C, 'a*(b + c - a)', ID="X_55", classes=["center", "incident"])
    X_650 = eval_trilinear_point(model, A, B, C, 'cos(B) - cos(C)', ID="X_650", classes=["center", "incident"])
    central_line(model, X_55, X_650, 55, 650, incident=True)
    return promote_point_to_top(model, X_1024)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1024 on the given reference triangle."""
    model = create_model('X_1024 = INTERSECTION OF LINES X_6X_513 ANDX(9)X_522')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01024(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01024.json"))
    write_center_svg(
        model_acute,
        here / "x-01024.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
