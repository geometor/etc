"""GEOMETOR construction model for X_1221 = ISOGONAL CONJUGATE OF X_1197."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    isogonal_conjugate,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_01221(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1221 = ISOGONAL CONJUGATE OF X_1197 on reference triangle ABC."""
    X_1197 = eval_trilinear_point(model, A, B, C, '(a**(2)*(a*b**(2) + a*c**(2) + b**(2)*c + b*c**(2)))', ID="X_1197", classes=["center"])
    X_1221 = isogonal_conjugate(model, A, B, C, X_1197, ID="X_1221", classes=["selected", "target"])
    X_43 = eval_trilinear_point(model, A, B, C, 'a*b + a*c - b*c', ID="X_43", classes=["center", "incident"])
    X_75 = eval_trilinear_point(model, A, B, C, '1/a**(2)', ID="X_75", classes=["center", "incident"])
    central_line(model, X_43, X_75, 43, 75, incident=True)
    X_76 = eval_trilinear_point(model, A, B, C, '1/a**(3)', ID="X_76", classes=["center", "incident"])
    X_192 = eval_trilinear_point(model, A, B, C, 'b*c*(c*a + a*b - b*c)', ID="X_192", classes=["center", "incident"])
    central_line(model, X_76, X_192, 76, 192, incident=True)
    X_213 = eval_trilinear_point(model, A, B, C, '(b + c)*a**(2)', ID="X_213", classes=["center", "incident"])
    X_274 = eval_trilinear_point(model, A, B, C, 'b**(2)*c**(2)/(b + c)', ID="X_274", classes=["center", "incident"])
    central_line(model, X_213, X_274, 213, 274, incident=True)
    return promote_point_to_top(model, X_1221)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1221 on the given reference triangle."""
    model = create_model('X_1221 = ISOGONAL CONJUGATE OF X_1197')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01221(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01221.json"))
    write_center_svg(
        model_acute,
        here / "x-01221.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
