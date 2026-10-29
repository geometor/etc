"""GEOMETOR construction model for X(805) = o-(- 2, 2) CIRCUMCIRCLE POINT."""

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
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00805(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(805) = o-(- 2, 2) CIRCUMCIRCLE POINT on reference triangle ABC."""
    X_804 = eval_trilinear_point(model, A, B, C, 'a **(-3)*(b**(2) - c**(2)) + a**(1)*(b **(-2) - c **(-2))', ID="X(804)", classes=["center"])
    X_805 = isogonal_conjugate(model, A, B, C, X_804, ID="X(805)", classes=["selected", "target"])
    X_98 = eval_trilinear_point(model, A, B, C, 'sec(A + omega )', ID="X(98)", classes=["center", "incident"])
    X_385 = eval_trilinear_point(model, A, B, C, 'b*c*(a**(4) - b**(2)*c**(2))', ID="X(385)", classes=["center", "incident"])
    central_line(model, X_98, X_385, 98, 385, incident=True)
    X_99 = eval_trilinear_point(model, A, B, C, 'b*c/(b**(2) - c**(2))', ID="X(99)", classes=["center", "incident"])
    X_512 = eval_trilinear_point(model, A, B, C, 'a*(b**(2) - c**(2))', ID="X(512)", classes=["center", "incident"])
    central_line(model, X_99, X_512, 99, 512, incident=True)
    X_110 = eval_trilinear_point(model, A, B, C, 'csc(B - C)', ID="X(110)", classes=["center", "incident"])
    X_669 = eval_trilinear_point(model, A, B, C, 'a**(3)*(b**(2) - c**(2))', ID="X(669)", classes=["center", "incident"])
    central_line(model, X_110, X_669, 110, 669, incident=True)
    return promote_point_to_top(model, X_805)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(805) on the given reference triangle."""
    model = create_model('X(805) = o-(- 2, 2) CIRCUMCIRCLE POINT')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00805(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00805.json"))
    write_center_svg(
        model_acute,
        here / "x-00805.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
