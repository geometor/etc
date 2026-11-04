"""GEOMETOR construction model for X_1257 = ISOGONAL CONJUGATE OF X_1104."""

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
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_01257(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1257 = ISOGONAL CONJUGATE OF X_1104 on reference triangle ABC."""
    X_1104 = point_from_barycentrics(model, A, B, C, 0.17229255, 0.32067511, 0.50703235, ID="X_1104", classes=["center"])
    X_1257 = isogonal_conjugate(model, A, B, C, X_1104, ID="X_1257", classes=["selected", "target"])
    X_28 = eval_trilinear_point(model, A, B, C, '(tan(A))/(b + c)', ID="X_28", classes=["center", "incident"])
    X_72 = eval_trilinear_point(model, A, B, C, '(b + c)*cot(A)', ID="X_72", classes=["center", "incident"])
    central_line(model, X_28, X_72, 28, 72, incident=True)
    X_57 = eval_trilinear_point(model, A, B, C, '1/(b + c - a)', ID="X_57", classes=["center", "incident"])
    X_78 = eval_trilinear_point(model, A, B, C, '1/(1 - sec(A))', ID="X_78", classes=["center", "incident"])
    central_line(model, X_57, X_78, 57, 78, incident=True)
    X_8 = nagel_point_of(model, A, B, C, ID="X_8", classes=["center", "incident"])
    X_278 = eval_trilinear_point(model, A, B, C, 'sec(A)*tan(A/2)', ID="X_278", classes=["center", "incident"])
    central_line(model, X_8, X_278, 8, 278, incident=True)
    return promote_point_to_top(model, X_1257)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1257 on the given reference triangle."""
    model = create_model('X_1257 = ISOGONAL CONJUGATE OF X_1104')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01257(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01257.json"))
    write_center_svg(
        model_acute,
        here / "x-01257.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
