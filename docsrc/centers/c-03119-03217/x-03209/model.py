"""GEOMETOR construction model for X_3209 = X_56-CEVA CONJUGATE OF X_25."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    crosspoint,
    eval_trilinear_point,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_03209(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3209 = X_56-CEVA CONJUGATE OF X_25 on reference triangle ABC."""
    X_19 = eval_trilinear_point(model, A, B, C, 'tan(A)', ID="X_19", classes=["center"])
    X_2331 = eval_trilinear_point(model, A, B, C, '(1 + sec(A))*(1 - sec(A) + sec(B) + sec(C))', ID="X_2331", classes=["center"])
    X_3209 = crosspoint(model, A, B, C, X_19, X_2331, ID="X_3209", classes=["selected", "target"])
    X_56 = eval_trilinear_point(model, A, B, C, 'a/(b + c - a)', ID="X_56", classes=["center", "incident"])
    central_line(model, X_19, X_56, 19, 56, incident=True)
    X_108 = eval_trilinear_point(model, A, B, C, 'a/(sec(B) - sec(C))', ID="X_108", classes=["center", "incident"])
    X_281 = eval_trilinear_point(model, A, B, C, 'sec(A)*cot(A/2)', ID="X_281", classes=["center", "incident"])
    central_line(model, X_108, X_281, 108, 281, incident=True)
    X_198 = eval_trilinear_point(model, A, B, C, '(a*(cos(B) + cos(C) - cos(A) - 1))', ID="X_198", classes=["center", "incident"])
    X_208 = eval_trilinear_point(model, A, B, C, '((1 - sec(A))*(cos(B) + cos(C) - cos(A) - 1))', ID="X_208", classes=["center", "incident"])
    central_line(model, X_198, X_208, 198, 208, incident=True)
    return promote_point_to_top(model, X_3209)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3209 on the given reference triangle."""
    model = create_model('X_3209 = X_56-CEVA CONJUGATE OF X_25')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03209(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03209.json"))
    write_center_svg(
        model_acute,
        here / "x-03209.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
