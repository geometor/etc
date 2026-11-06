"""GEOMETOR construction model for X_3260 = ISOTOMIC CONJUGATE OF X_74."""

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
    orthocenter_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_03260(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3260 = ISOTOMIC CONJUGATE OF X_74 on reference triangle ABC."""
    X_74 = eval_trilinear_point(model, A, B, C, '1/(cos(A) - 2*cos(B)*cos(C))', ID="X_74", classes=["center"])
    X_3260 = isotomic_conjugate(model, A, B, C, X_74, ID="X_3260", classes=["selected", "target"])
    X_4 = orthocenter_of(model, A, B, C, ID="X_4", classes=["center", "incident"])
    X_69 = eval_trilinear_point(model, A, B, C, '(cos(A))/a**(2)', ID="X_69", classes=["center", "incident"])
    central_line(model, X_4, X_69, 4, 69, incident=True)
    X_94 = eval_trilinear_point(model, A, B, C, 'csc(3*A)', ID="X_94", classes=["center", "incident"])
    X_323 = eval_trilinear_point(model, A, B, C, 'sin(3*A)*(csc(A))**(2)', ID="X_323", classes=["center", "incident"])
    central_line(model, X_94, X_323, 94, 323, incident=True)
    X_99 = eval_trilinear_point(model, A, B, C, 'b*c/(b**(2) - c**(2))', ID="X_99", classes=["center", "incident"])
    X_477 = eval_trilinear_point(model, A, B, C, '1/(4*cos(A) + cos(A - 2*B) + cos(A - 2*C) - 3*cos(B - C))', ID="X_477", classes=["center", "incident"])
    central_line(model, X_99, X_477, 99, 477, incident=True)
    return promote_point_to_top(model, X_3260)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3260 on the given reference triangle."""
    model = create_model('X_3260 = ISOTOMIC CONJUGATE OF X_74')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03260(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03260.json"))
    write_center_svg(
        model_acute,
        here / "x-03260.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
