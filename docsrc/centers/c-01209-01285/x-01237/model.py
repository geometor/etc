"""GEOMETOR construction model for X_1237 = ISOTOMIC CONJUGATE OF X_1178."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    isotomic_conjugate,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_01237(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1237 = ISOTOMIC CONJUGATE OF X_1178 on reference triangle ABC."""
    X_1178 = eval_trilinear_point(model, A, B, C, '(a/((b + c)*(a**(2) + b*c)))', ID="X_1178", classes=["center"])
    X_1237 = isotomic_conjugate(model, A, B, C, X_1178, ID="X_1237", classes=["selected", "target"])
    X_12 = eval_trilinear_point(model, A, B, C, '1 + cos(B - C)', ID="X_12", classes=["center", "incident"])
    X_313 = eval_trilinear_point(model, A, B, C, '(b + c)*b**(3)*c**(3)', ID="X_313", classes=["center", "incident"])
    central_line(model, X_12, X_313, 12, 313, incident=True)
    X_76 = eval_trilinear_point(model, A, B, C, '1/a**(3)', ID="X_76", classes=["center", "incident"])
    X_334 = eval_trilinear_point(model, A, B, C, 'b**(2)*c**(2)/(a**(2) - b*c)', ID="X_334", classes=["center", "incident"])
    central_line(model, X_76, X_334, 76, 334, incident=True)
    X_561 = eval_trilinear_point(model, A, B, C, 'a **(- 4)', ID="X_561", classes=["center", "incident"])
    X_756 = eval_trilinear_point(model, A, B, C, '(b + c)**(2)', ID="X_756", classes=["center", "incident"])
    central_line(model, X_561, X_756, 561, 756, incident=True)
    return promote_point_to_top(model, X_1237)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1237 on the given reference triangle."""
    model = create_model('X_1237 = ISOTOMIC CONJUGATE OF X_1178')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01237(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01237.json"))
    write_center_svg(
        model_acute,
        here / "x-01237.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
