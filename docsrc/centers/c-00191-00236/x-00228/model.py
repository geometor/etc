"""GEOMETOR construction model for X_228 = X_3-CEVA CONJUGATE OF X_71."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    circumcenter_of,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00228(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_228 = X_3-CEVA CONJUGATE OF X_71 on reference triangle ABC."""
    X_228 = eval_trilinear_point(model, A, B, C, '(sin(2*A))*(sin(B) + sin(C))', ID="X_228", classes=["selected", "target"])
    X_19 = eval_trilinear_point(model, A, B, C, 'tan(A)', ID="X_19", classes=["center", "incident"])
    X_25 = eval_trilinear_point(model, A, B, C, 'sin(A)*tan(A)', ID="X_25", classes=["center", "incident"])
    central_line(model, X_19, X_25, 19, 25, incident=True)
    X_31 = eval_trilinear_point(model, A, B, C, 'a**(2)', ID="X_31", classes=["center", "incident"])
    X_32 = eval_trilinear_point(model, A, B, C, 'a**(3)', ID="X_32", classes=["center", "incident"])
    central_line(model, X_31, X_32, 31, 32, incident=True)
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center", "incident"])
    X_63 = eval_trilinear_point(model, A, B, C, 'cot(A)', ID="X_63", classes=["center", "incident"])
    central_line(model, X_3, X_63, 3, 63, incident=True)
    return promote_point_to_top(model, X_228)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_228 on the given reference triangle."""
    model = create_model('X_228 = X_3-CEVA CONJUGATE OF X_71')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00228(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00228.json"))
    write_center_svg(
        model_acute,
        here / "x-00228.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
