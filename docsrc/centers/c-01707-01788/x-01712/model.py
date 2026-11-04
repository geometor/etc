"""GEOMETOR construction model for X_1712 = MIMOSA TRANSFORM OF (20)."""

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
    intersect_lines,
    orthocenter_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_01712(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1712 = MIMOSA TRANSFORM OF (20) on reference triangle ABC."""
    X_4 = orthocenter_of(model, A, B, C, ID="X_4", classes=["center"])
    X_57 = eval_trilinear_point(model, A, B, C, '1/(b + c - a)', ID="X_57", classes=["center"])
    X_19 = eval_trilinear_point(model, A, B, C, 'tan(A)', ID="X_19", classes=["center"])
    X_158 = eval_trilinear_point(model, A, B, C, '(sec(A))**(2)', ID="X_158", classes=["center"])
    central_line(model, X_4, X_57, 4, 57)
    central_line(model, X_19, X_158, 19, 158)
    X_1712 = intersect_lines(model, X_4, X_57, X_19, X_158, ID="X_1712", classes=["selected", "target"])
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center", "incident"])
    X_204 = eval_trilinear_point(model, A, B, C, '((tan(A))*(tan(B) + tan(C) - tan(A)))', ID="X_204", classes=["center", "incident"])
    central_line(model, X_1, X_204, 1, 204, incident=True)
    return promote_point_to_top(model, X_1712)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1712 on the given reference triangle."""
    model = create_model('X_1712 = MIMOSA TRANSFORM OF (20)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01712(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01712.json"))
    write_center_svg(
        model_acute,
        here / "x-01712.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
