"""GEOMETOR construction model for X(380) = INTERSECTION OF LINES X(1)X(19) AND X(9)X(55)."""

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
    mittenpunkt_of,
    promote_point_to_top,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_00380(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(380) = INTERSECTION OF LINES X(1)X(19) AND X(9)X(55) on reference triangle ABC."""
    X_380 = eval_trilinear_point(model, A, B, C, '(b + c - a)*(3*a**(3)+ (b + c)*(3*a**(2)+ (b - c)**(2)+ a*(b + c)))', ID="X(380)", classes=["selected", "target"])
    X_1 = incenter_of(model, A, B, C, ID="X(1)", classes=["center", "incident"])
    X_19 = eval_trilinear_point(model, A, B, C, 'tan(A)', ID="X(19)", classes=["center", "incident"])
    central_line(model, X_1, X_19, 1, 19, incident=True)
    X_6 = symmedian_point_of(model, A, B, C, ID="X(6)", classes=["center", "incident"])
    X_40 = eval_trilinear_point(model, A, B, C, 'cos(B) + cos(C) - cos(A) - 1', ID="X(40)", classes=["center", "incident"])
    central_line(model, X_6, X_40, 6, 40, incident=True)
    X_9 = mittenpunkt_of(model, A, B, C, ID="X(9)", classes=["center", "incident"])
    X_55 = eval_trilinear_point(model, A, B, C, 'a*(b + c - a)', ID="X(55)", classes=["center", "incident"])
    central_line(model, X_9, X_55, 9, 55, incident=True)
    return promote_point_to_top(model, X_380)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(380) on the given reference triangle."""
    model = create_model('X(380) = INTERSECTION OF LINES X(1)X(19) AND X(9)X(55)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00380(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00380.json"))
    write_center_svg(
        model_acute,
        here / "x-00380.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
