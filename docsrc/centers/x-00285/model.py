"""GEOMETOR construction model for X(285) = X(58)-CROSS CONJUGATE OF X(21)."""

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


def construct_x_00285(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(285) = X(58)-CROSS CONJUGATE OF X(21) on reference triangle ABC."""
    X_227 = eval_trilinear_point(model, A, B, C, '(b + c)*(cos(B) + cos(C) - cos(A) - 1)*tan(A/2)', ID="X(227)", classes=["center"])
    X_285 = isogonal_conjugate(model, A, B, C, X_227, ID="X(285)", classes=["selected", "target"])
    X_21 = eval_trilinear_point(model, A, B, C, '1/(cos(B) + cos(C))', ID="X(21)", classes=["center", "incident"])
    X_84 = eval_trilinear_point(model, A, B, C, '1/(cos(B) + cos(C) - cos(A) - 1)', ID="X(84)", classes=["center", "incident"])
    central_line(model, X_21, X_84, 21, 84, incident=True)
    X_29 = eval_trilinear_point(model, A, B, C, '(sec(A))/(cos(B) + cos(C))', ID="X(29)", classes=["center", "incident"])
    X_81 = eval_trilinear_point(model, A, B, C, '1/(b + c)', ID="X(81)", classes=["center", "incident"])
    central_line(model, X_29, X_81, 29, 81, incident=True)
    X_271 = eval_trilinear_point(model, A, B, C, '(cot(A)*cot(A/2))/(-1 - cos(A) + cos(B) + cos(C))', ID="X(271)", classes=["center", "incident"])
    X_282 = eval_trilinear_point(model, A, B, C, '(cot(A/2))/(-1 - cos(A) + cos(B) + cos(C))', ID="X(282)", classes=["center", "incident"])
    central_line(model, X_271, X_282, 271, 282, incident=True)
    return promote_point_to_top(model, X_285)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(285) on the given reference triangle."""
    model = create_model('X(285) = X(58)-CROSS CONJUGATE OF X(21)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00285(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00285.json"))
    write_center_svg(
        model_acute,
        here / "x-00285.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
