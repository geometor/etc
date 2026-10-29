"""GEOMETOR construction model for X(494) = 2nd VAN LAMOEN HOMOTHETIC CENTER."""

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


def construct_x_00494(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(494) = 2nd VAN LAMOEN HOMOTHETIC CENTER on reference triangle ABC."""
    X_494 = eval_trilinear_point(model, A, B, C, '1/(sin(A) - sin(B)*sin(C))', ID="X(494)", classes=["selected", "target"])
    X_25 = eval_trilinear_point(model, A, B, C, 'sin(A)*tan(A)', ID="X(25)", classes=["center", "incident"])
    X_372 = eval_trilinear_point(model, A, B, C, 'cos(A + pi /4)', ID="X(372)", classes=["center", "incident"])
    central_line(model, X_25, X_372, 25, 372, incident=True)
    X_39 = eval_trilinear_point(model, A, B, C, 'a*(b**(2) + c**(2))', ID="X(39)", classes=["center", "incident"])
    X_493 = eval_trilinear_point(model, A, B, C, '1/(sin(A) + sin(B)*sin(C))', ID="X(493)", classes=["center", "incident"])
    central_line(model, X_39, X_493, 39, 493, incident=True)
    return promote_point_to_top(model, X_494)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(494) on the given reference triangle."""
    model = create_model('X(494) = 2nd VAN LAMOEN HOMOTHETIC CENTER')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00494(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00494.json"))
    write_center_svg(
        model_acute,
        here / "x-00494.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
