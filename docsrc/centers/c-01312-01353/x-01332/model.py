"""GEOMETOR construction model for X_1332 = ORTHOCORRESPONDENT OF X_100."""

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
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_01332(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1332 = ORTHOCORRESPONDENT OF X_100 on reference triangle ABC."""
    X_1332 = eval_trilinear_point(model, A, B, C, '(b**(2) + c**(2) - a**(2))/(b - c)', ID="X_1332", classes=["selected", "target"])
    X_100 = eval_trilinear_point(model, A, B, C, '1/(b - c)', ID="X_100", classes=["center", "incident"])
    X_110 = eval_trilinear_point(model, A, B, C, 'csc(B - C)', ID="X_110", classes=["center", "incident"])
    central_line(model, X_100, X_110, 100, 110, incident=True)
    X_69 = eval_trilinear_point(model, A, B, C, '(cos(A))/a**(2)', ID="X_69", classes=["center", "incident"])
    X_219 = eval_trilinear_point(model, A, B, C, 'cos(A)*cot(A/2)', ID="X_219", classes=["center", "incident"])
    central_line(model, X_69, X_219, 69, 219, incident=True)
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center", "incident"])
    X_344 = eval_trilinear_point(model, A, B, C, '((csc(A/2))**(2))*((cos(B/2))**(4) + (cos(C/2))**(4) - (cos(A/2))**(4))', ID="X_344", classes=["center", "incident"])
    central_line(model, X_6, X_344, 6, 344, incident=True)
    return promote_point_to_top(model, X_1332)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1332 on the given reference triangle."""
    model = create_model('X_1332 = ORTHOCORRESPONDENT OF X_100')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01332(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01332.json"))
    write_center_svg(
        model_acute,
        here / "x-01332.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
