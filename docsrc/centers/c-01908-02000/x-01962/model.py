"""GEOMETOR construction model for X_1962 = BICENTRIC SUM OF PU(32)."""

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
    reflection_in_point,
)
from geometor.etc.render import write_center_svg


def construct_x_01962(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1962 = BICENTRIC SUM OF PU(32) on reference triangle ABC."""
    X_1635 = eval_trilinear_point(model, A, B, C, '(b - c)*(b + c - 2*a)', ID="X_1635", classes=["center"])
    X_351 = eval_trilinear_point(model, A, B, C, '(a*(b**(2) - c**(2))*(b**(2) + c**(2) - 2*a**(2)))', ID="X_351", classes=["center"])
    X_1962 = reflection_in_point(model, X_1635, X_351, ID="X_1962", classes=["selected", "target"], guide=False)
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center", "incident"])
    X_21 = eval_trilinear_point(model, A, B, C, '1/(cos(B) + cos(C))', ID="X_21", classes=["center", "incident"])
    central_line(model, X_1, X_21, 1, 21, incident=True)
    X_37 = eval_trilinear_point(model, A, B, C, 'b + c', ID="X_37", classes=["center", "incident"])
    X_42 = eval_trilinear_point(model, A, B, C, 'a*(b + c)', ID="X_42", classes=["center", "incident"])
    central_line(model, X_37, X_42, 37, 42, incident=True)
    X_55 = eval_trilinear_point(model, A, B, C, 'a*(b + c - a)', ID="X_55", classes=["center", "incident"])
    X_199 = eval_trilinear_point(model, A, B, C, '(a*(b**(4) + c**(4) - a**(4) + (b**(2) + c**(2) - a**(2))*(b*c + c*a + a*b)))', ID="X_199", classes=["center", "incident"])
    central_line(model, X_55, X_199, 55, 199, incident=True)
    return promote_point_to_top(model, X_1962)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1962 on the given reference triangle."""
    model = create_model('X_1962 = BICENTRIC SUM OF PU(32)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01962(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01962.json"))
    write_center_svg(
        model_acute,
        here / "x-01962.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
