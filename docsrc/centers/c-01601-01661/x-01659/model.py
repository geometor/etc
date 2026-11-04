"""GEOMETOR construction model for X_1659 = YIU-PAASCHE POINT."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    centroid_of,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    incenter_of,
    orthocenter_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_01659(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1659 = YIU-PAASCHE POINT on reference triangle ABC."""
    X_1659 = eval_trilinear_point(model, A, B, C, '(1/(1 + sin(A) + cos(A)))', ID="X_1659", classes=["selected", "target"])
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center", "incident"])
    X_4 = orthocenter_of(model, A, B, C, ID="X_4", classes=["center", "incident"])
    central_line(model, X_1, X_4, 1, 4, incident=True)
    X_2 = centroid_of(model, A, B, C, ID="X_2", classes=["center", "incident"])
    X_176 = eval_trilinear_point(model, A, B, C, '1 + sec(A/2)*cos(B/2)*cos(C/2)', ID="X_176", classes=["center", "incident"])
    central_line(model, X_2, X_176, 2, 176, incident=True)
    X_57 = eval_trilinear_point(model, A, B, C, '1/(b + c - a)', ID="X_57", classes=["center", "incident"])
    X_482 = eval_trilinear_point(model, A, B, C, '1 + 2*sec(A/2)*cos(B/2)*cos(C/2)', ID="X_482", classes=["center", "incident"])
    central_line(model, X_57, X_482, 57, 482, incident=True)
    return promote_point_to_top(model, X_1659)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1659 on the given reference triangle."""
    model = create_model('X_1659 = YIU-PAASCHE POINT')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01659(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01659.json"))
    write_center_svg(
        model_acute,
        here / "x-01659.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
