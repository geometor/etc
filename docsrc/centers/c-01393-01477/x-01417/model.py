"""GEOMETOR construction model for X_1417 = X_106-BETH CONJUGATE OF X_106."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    intersect_lines,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_01417(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1417 = X_106-BETH CONJUGATE OF X_106 on reference triangle ABC."""
    X_56 = eval_trilinear_point(model, A, B, C, 'a/(b + c - a)', ID="X_56", classes=["center"])
    X_106 = eval_trilinear_point(model, A, B, C, 'a/(2*a - b - c)', ID="X_106", classes=["center"])
    X_88 = eval_trilinear_point(model, A, B, C, '1/(b + c - 2*a)', ID="X_88", classes=["center"])
    X_961 = eval_trilinear_point(model, A, B, C, '(1/((b + c - a)*(b**(2) + c**(2) + a*b + a*c)))', ID="X_961", classes=["center"])
    central_line(model, X_56, X_106, 56, 106)
    central_line(model, X_88, X_961, 88, 961)
    X_1417 = intersect_lines(model, X_56, X_106, X_88, X_961, ID="X_1417", classes=["selected", "target"])
    X_65 = eval_trilinear_point(model, A, B, C, 'cos(B) + cos(C)', ID="X_65", classes=["center", "incident"])
    X_1320 = eval_trilinear_point(model, A, B, C, '((b + c - a)/ (b + c - 2*a))', ID="X_1320", classes=["center", "incident"])
    central_line(model, X_65, X_1320, 65, 1320, incident=True)
    return promote_point_to_top(model, X_1417)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1417 on the given reference triangle."""
    model = create_model('X_1417 = X_106-BETH CONJUGATE OF X_106')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01417(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01417.json"))
    write_center_svg(
        model_acute,
        here / "x-01417.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
