"""GEOMETOR construction model for X_3377 = TAN(A - π/4) POINT."""

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


def construct_x_03377(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3377 = TAN(A - π/4) POINT on reference triangle ABC."""
    X_3377 = eval_trilinear_point(model, A, B, C, '(tan(A -  pi  /4))', ID="X_3377", classes=["selected", "target"])
    X_19 = eval_trilinear_point(model, A, B, C, 'tan(A)', ID="X_19", classes=["center", "incident"])
    X_91 = eval_trilinear_point(model, A, B, C, 'sec(2*A)', ID="X_91", classes=["center", "incident"])
    central_line(model, X_19, X_91, 19, 91, incident=True)
    X_46 = eval_trilinear_point(model, A, B, C, 'cos(B) + cos(C) - cos(A)', ID="X_46", classes=["center", "incident"])
    X_485 = eval_trilinear_point(model, A, B, C, 'sec(A -  pi  /4)', ID="X_485", classes=["center", "incident"])
    central_line(model, X_46, X_485, 46, 485, incident=True)
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center", "incident"])
    X_1805 = eval_trilinear_point(model, A, B, C, '(a*(1 - cot(A/2))/(b + c))', ID="X_1805", classes=["center", "incident"])
    central_line(model, X_1, X_1805, 1, 1805, incident=True)
    return promote_point_to_top(model, X_3377)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3377 on the given reference triangle."""
    model = create_model('X_3377 = TAN(A - π/4) POINT')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03377(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03377.json"))
    write_center_svg(
        model_acute,
        here / "x-03377.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
