"""GEOMETOR construction model for X_3383 = TAN(A - π/6) POINT."""

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


def construct_x_03383(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3383 = TAN(A - π/6) POINT on reference triangle ABC."""
    X_3383 = eval_trilinear_point(model, A, B, C, '(tan(A -  pi  /6))', ID="X_3383", classes=["selected", "target"])
    X_13 = eval_trilinear_point(model, A, B, C, 'csc(A +  pi  /3)', ID="X_13", classes=["center", "incident"])
    X_484 = eval_trilinear_point(model, A, B, C, '1 + 2*(cos(A) - cos(B) - cos(C))', ID="X_484", classes=["center", "incident"])
    central_line(model, X_13, X_484, 13, 484, incident=True)
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center", "incident"])
    X_1094 = eval_trilinear_point(model, A, B, C, '((sin(A +  pi  /3))**(2))', ID="X_1094", classes=["center", "incident"])
    central_line(model, X_1, X_1094, 1, 1094, incident=True)
    X_19 = eval_trilinear_point(model, A, B, C, 'tan(A)', ID="X_19", classes=["center", "incident"])
    X_2166 = eval_trilinear_point(model, A, B, C, '(sin(A)*csc(3*A))', ID="X_2166", classes=["center", "incident"])
    central_line(model, X_19, X_2166, 19, 2166, incident=True)
    return promote_point_to_top(model, X_3383)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3383 on the given reference triangle."""
    model = create_model('X_3383 = TAN(A - π/6) POINT')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03383(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03383.json"))
    write_center_svg(
        model_acute,
        here / "x-03383.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
