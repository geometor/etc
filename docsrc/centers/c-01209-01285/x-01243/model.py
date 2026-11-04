"""GEOMETOR construction model for X_1243 = ISOGONAL CONJUGATE OF X_1006."""

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
    nine_point_center_of,
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_01243(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1243 = ISOGONAL CONJUGATE OF X_1006 on reference triangle ABC."""
    X_1006 = point_from_barycentrics(model, A, B, C, 0.38295089, 0.36413043, 0.25291868, ID="X_1006", classes=["center"])
    X_1243 = isogonal_conjugate(model, A, B, C, X_1006, ID="X_1243", classes=["selected", "target"])
    X_5 = nine_point_center_of(model, A, B, C, ID="X_5", classes=["center", "incident"])
    X_72 = eval_trilinear_point(model, A, B, C, '(b + c)*cot(A)', ID="X_72", classes=["center", "incident"])
    central_line(model, X_5, X_72, 5, 72, incident=True)
    X_28 = eval_trilinear_point(model, A, B, C, '(tan(A))/(b + c)', ID="X_28", classes=["center", "incident"])
    X_54 = eval_trilinear_point(model, A, B, C, 'sec(B - C)', ID="X_54", classes=["center", "incident"])
    central_line(model, X_28, X_54, 28, 54, incident=True)
    X_71 = eval_trilinear_point(model, A, B, C, '(b + c)*cos(A)', ID="X_71", classes=["center", "incident"])
    X_517 = eval_trilinear_point(model, A, B, C, '-1 + cos(B) + cos(C)', ID="X_517", classes=["center", "incident"])
    central_line(model, X_71, X_517, 71, 517, incident=True)
    return promote_point_to_top(model, X_1243)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1243 on the given reference triangle."""
    model = create_model('X_1243 = ISOGONAL CONJUGATE OF X_1006')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01243(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01243.json"))
    write_center_svg(
        model_acute,
        here / "x-01243.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
