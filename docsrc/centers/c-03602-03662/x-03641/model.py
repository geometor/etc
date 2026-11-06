"""GEOMETOR construction model for X_3641 = 2nd KIRIKAMI POINT."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_barycentric_point,
    eval_trilinear_point,
    incenter_of,
    nagel_point_of,
    promote_point_to_top,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_03641(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3641 = 2nd KIRIKAMI POINT on reference triangle ABC."""
    X_3641 = eval_barycentric_point(model, A, B, C, 'a*(b**(2) + c**(2) - a*(b + c) - S)', ID="X_3641", classes=["selected", "target"])
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center", "incident"])
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center", "incident"])
    central_line(model, X_1, X_6, 1, 6, incident=True)
    X_8 = nagel_point_of(model, A, B, C, ID="X_8", classes=["center", "incident"])
    X_176 = eval_trilinear_point(model, A, B, C, '1 + sec(A/2)*cos(B/2)*cos(C/2)', ID="X_176", classes=["center", "incident"])
    central_line(model, X_8, X_176, 8, 176, incident=True)
    X_517 = eval_trilinear_point(model, A, B, C, '-1 + cos(B) + cos(C)', ID="X_517", classes=["center", "incident"])
    X_1161 = eval_trilinear_point(model, A, B, C, '(1 - 2*cot(A) - 2*cot(B) - 2*cot(C))*cos(A) + 2*sin(A)', ID="X_1161", classes=["center", "incident"])
    central_line(model, X_517, X_1161, 517, 1161, incident=True)
    return promote_point_to_top(model, X_3641)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3641 on the given reference triangle."""
    model = create_model('X_3641 = 2nd KIRIKAMI POINT')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03641(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03641.json"))
    write_center_svg(
        model_acute,
        here / "x-03641.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
