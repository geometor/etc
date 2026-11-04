"""GEOMETOR construction model for X_271 = ISOGONAL CONJUGATE OF X_208."""

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
    nagel_point_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00271(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_271 = ISOGONAL CONJUGATE OF X_208 on reference triangle ABC."""
    X_208 = eval_trilinear_point(model, A, B, C, '((1 - sec(A))*(cos(B) + cos(C) - cos(A) - 1))', ID="X_208", classes=["center"])
    X_271 = isogonal_conjugate(model, A, B, C, X_208, ID="X_271", classes=["selected", "target"])
    X_8 = nagel_point_of(model, A, B, C, ID="X_8", classes=["center", "incident"])
    X_20 = eval_trilinear_point(model, A, B, C, 'cos(A) - cos(B)*cos(C)', ID="X_20", classes=["center", "incident"])
    central_line(model, X_8, X_20, 8, 20, incident=True)
    X_200 = eval_trilinear_point(model, A, B, C, '(cot(A/2))**(2)', ID="X_200", classes=["center", "incident"])
    X_255 = eval_trilinear_point(model, A, B, C, '(cos(A))**(2)', ID="X_255", classes=["center", "incident"])
    central_line(model, X_200, X_255, 200, 255, incident=True)
    X_78 = eval_trilinear_point(model, A, B, C, '1/(1 - sec(A))', ID="X_78", classes=["center", "incident"])
    X_394 = eval_trilinear_point(model, A, B, C, 'cos(A)*cot(A)', ID="X_394", classes=["center", "incident"])
    central_line(model, X_78, X_394, 78, 394, incident=True)
    return promote_point_to_top(model, X_271)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_271 on the given reference triangle."""
    model = create_model('X_271 = ISOGONAL CONJUGATE OF X_208')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00271(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00271.json"))
    write_center_svg(
        model_acute,
        here / "x-00271.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
