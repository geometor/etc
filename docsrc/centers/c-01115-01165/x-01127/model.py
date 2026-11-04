"""GEOMETOR construction model for X_1127 = 1st DE VILLIERS POINT."""

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
)
from geometor.etc.render import write_center_svg


def construct_x_01127(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1127 = 1st DE VILLIERS POINT on reference triangle ABC."""
    X_1127 = eval_trilinear_point(model, A, B, C, '(sin(A/4))/sin(3*A/4)', ID="X_1127", classes=["selected", "target"])
    X_174 = eval_trilinear_point(model, A, B, C, 'sec(A/2)', ID="X_174", classes=["center", "incident"])
    X_481 = eval_trilinear_point(model, A, B, C, '1 - 2*sec(A/2)*cos(B/2)*cos(C/2)', ID="X_481", classes=["center", "incident"])
    central_line(model, X_174, X_481, 174, 481, incident=True)
    return promote_point_to_top(model, X_1127)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1127 on the given reference triangle."""
    model = create_model('X_1127 = 1st DE VILLIERS POINT')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01127(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01127.json"))
    write_center_svg(
        model_acute,
        here / "x-01127.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
