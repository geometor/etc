"""GEOMETOR construction model for X(256) = 1st SHARYGIN POINT."""

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
    mittenpunkt_of,
    nagel_point_of,
    orthocenter_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00256(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(256) = 1st SHARYGIN POINT on reference triangle ABC."""
    X_171 = eval_trilinear_point(model, A, B, C, 'a**(2) + b*c', ID="X(171)", classes=["center"])
    X_256 = isogonal_conjugate(model, A, B, C, X_171, ID="X(256)", classes=["selected", "target"])
    X_9 = mittenpunkt_of(model, A, B, C, ID="X(9)", classes=["center", "incident"])
    X_43 = eval_trilinear_point(model, A, B, C, 'a*b + a*c - b*c', ID="X(43)", classes=["center", "incident"])
    central_line(model, X_9, X_43, 9, 43, incident=True)
    X_8 = nagel_point_of(model, A, B, C, ID="X(8)", classes=["center", "incident"])
    X_192 = eval_trilinear_point(model, A, B, C, 'b*c*(c*a + a*b - b*c)', ID="X(192)", classes=["center", "incident"])
    central_line(model, X_8, X_192, 8, 192, incident=True)
    X_4 = orthocenter_of(model, A, B, C, ID="X(4)", classes=["center", "incident"])
    X_240 = eval_trilinear_point(model, A, B, C, 'sec(A)*cos(A + omega )', ID="X(240)", classes=["center", "incident"])
    central_line(model, X_4, X_240, 4, 240, incident=True)
    return promote_point_to_top(model, X_256)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(256) on the given reference triangle."""
    model = create_model('X(256) = 1st SHARYGIN POINT')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00256(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00256.json"))
    write_center_svg(
        model_acute,
        here / "x-00256.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
