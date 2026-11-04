"""GEOMETOR construction model for X_1264 = ISOTOMIC CONJUGATE OF X_1118."""

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
    nagel_point_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_01264(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1264 = ISOTOMIC CONJUGATE OF X_1118 on reference triangle ABC."""
    X_1118 = eval_trilinear_point(model, A, B, C, '((1 - cos(A))/(cos(A))**(2))', ID="X_1118", classes=["center"])
    X_1264 = isotomic_conjugate(model, A, B, C, X_1118, ID="X_1264", classes=["selected", "target"])
    X_69 = eval_trilinear_point(model, A, B, C, '(cos(A))/a**(2)', ID="X_69", classes=["center", "incident"])
    X_72 = eval_trilinear_point(model, A, B, C, '(b + c)*cot(A)', ID="X_72", classes=["center", "incident"])
    central_line(model, X_69, X_72, 69, 72, incident=True)
    X_8 = nagel_point_of(model, A, B, C, ID="X_8", classes=["center", "incident"])
    X_314 = eval_trilinear_point(model, A, B, C, '(b**(2)*c**(2)*(b + c - a)/(b + c))', ID="X_314", classes=["center", "incident"])
    central_line(model, X_8, X_314, 8, 314, incident=True)
    X_219 = eval_trilinear_point(model, A, B, C, 'cos(A)*cot(A/2)', ID="X_219", classes=["center", "incident"])
    X_332 = eval_trilinear_point(model, A, B, C, '(cot(A)*csc(A))/(cos(B) + cos(C))', ID="X_332", classes=["center", "incident"])
    central_line(model, X_219, X_332, 219, 332, incident=True)
    return promote_point_to_top(model, X_1264)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1264 on the given reference triangle."""
    model = create_model('X_1264 = ISOTOMIC CONJUGATE OF X_1118')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01264(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01264.json"))
    write_center_svg(
        model_acute,
        here / "x-01264.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
