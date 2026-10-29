"""GEOMETOR construction model for X(827) = o-(0, 4) CIRCUMCIRCLE POINT."""

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
    promote_point_to_top,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_00827(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(827) = o-(0, 4) CIRCUMCIRCLE POINT on reference triangle ABC."""
    X_826 = eval_trilinear_point(model, A, B, C, 'a **(-1)*(b**(4) - c**(4)) + a**(3)*(b**(0) - c**(0))', ID="X(826)", classes=["center"])
    X_827 = isogonal_conjugate(model, A, B, C, X_826, ID="X(827)", classes=["selected", "target"])
    X_5 = nine_point_center_of(model, A, B, C, ID="X(5)", classes=["center", "incident"])
    X_83 = eval_trilinear_point(model, A, B, C, 'b*c/(b**(2) + c**(2))', ID="X(83)", classes=["center", "incident"])
    central_line(model, X_5, X_83, 5, 83, incident=True)
    X_111 = eval_trilinear_point(model, A, B, C, 'a/(2*a**(2) - b**(2) - c**(2))', ID="X(111)", classes=["center", "incident"])
    X_251 = eval_trilinear_point(model, A, B, C, 'a**(2)*csc(A + omega )', ID="X(251)", classes=["center", "incident"])
    central_line(model, X_111, X_251, 111, 251, incident=True)
    X_6 = symmedian_point_of(model, A, B, C, ID="X(6)", classes=["center", "incident"])
    X_755 = eval_trilinear_point(model, A, B, C, '1/(a**(-1)*(b**(4)+ c**(4)) - a**(3)*(b**(0)+ c**(0)))', ID="X(755)", classes=["center", "incident"])
    central_line(model, X_6, X_755, 6, 755, incident=True)
    return promote_point_to_top(model, X_827)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(827) on the given reference triangle."""
    model = create_model('X(827) = o-(0, 4) CIRCUMCIRCLE POINT')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00827(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00827.json"))
    write_center_svg(
        model_acute,
        here / "x-00827.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
