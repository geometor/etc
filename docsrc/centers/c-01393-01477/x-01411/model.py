"""GEOMETOR construction model for X_1411 = X_80-BETH CONJUGATE OF X_80."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    cevapoint,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    incenter_of,
    nine_point_center_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_01411(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1411 = X_80-BETH CONJUGATE OF X_80 on reference triangle ABC."""
    X_65 = eval_trilinear_point(model, A, B, C, 'cos(B) + cos(C)', ID="X_65", classes=["center"])
    X_1319 = eval_trilinear_point(model, A, B, C, '(b + c - 2*a)/ (b + c - a)', ID="X_1319", classes=["center"])
    X_1411 = cevapoint(model, A, B, C, X_65, X_1319, ID="X_1411", classes=["selected", "target"])
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center", "incident"])
    X_5 = nine_point_center_of(model, A, B, C, ID="X_5", classes=["center", "incident"])
    central_line(model, X_1, X_5, 1, 5, incident=True)
    X_58 = eval_trilinear_point(model, A, B, C, 'a/(b + c)', ID="X_58", classes=["center", "incident"])
    central_line(model, X_58, X_65, 58, 65, incident=True)
    X_56 = eval_trilinear_point(model, A, B, C, 'a/(b + c - a)', ID="X_56", classes=["center", "incident"])
    X_244 = eval_trilinear_point(model, A, B, C, '(b - c)**(2)', ID="X_244", classes=["center", "incident"])
    central_line(model, X_56, X_244, 56, 244, incident=True)
    return promote_point_to_top(model, X_1411)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1411 on the given reference triangle."""
    model = create_model('X_1411 = X_80-BETH CONJUGATE OF X_80')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01411(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01411.json"))
    write_center_svg(
        model_acute,
        here / "x-01411.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
