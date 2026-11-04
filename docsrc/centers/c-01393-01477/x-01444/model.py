"""GEOMETOR construction model for X_1444 = X_332-BETH CONJUGATE OF X_332."""

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
    gergonne_point_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_01444(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1444 = X_332-BETH CONJUGATE OF X_332 on reference triangle ABC."""
    X_1444 = eval_trilinear_point(model, A, B, C, '(cot(A))/(b + c)', ID="X_1444", classes=["selected", "target"])
    X_7 = gergonne_point_of(model, A, B, C, ID="X_7", classes=["center", "incident"])
    X_21 = eval_trilinear_point(model, A, B, C, '1/(cos(B) + cos(C))', ID="X_21", classes=["center", "incident"])
    central_line(model, X_7, X_21, 7, 21, incident=True)
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center", "incident"])
    X_69 = eval_trilinear_point(model, A, B, C, '(cos(A))/a**(2)', ID="X_69", classes=["center", "incident"])
    central_line(model, X_3, X_69, 3, 69, incident=True)
    X_48 = eval_trilinear_point(model, A, B, C, 'tan(B) + tan(C)', ID="X_48", classes=["center", "incident"])
    X_63 = eval_trilinear_point(model, A, B, C, 'cot(A)', ID="X_63", classes=["center", "incident"])
    central_line(model, X_48, X_63, 48, 63, incident=True)
    return promote_point_to_top(model, X_1444)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1444 on the given reference triangle."""
    model = create_model('X_1444 = X_332-BETH CONJUGATE OF X_332')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01444(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01444.json"))
    write_center_svg(
        model_acute,
        here / "x-01444.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
