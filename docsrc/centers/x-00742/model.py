"""GEOMETOR construction model for X(742) = EVEN (- 1, 2) INFINITY POINT."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    promote_point_to_top,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_00742(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(742) = EVEN (- 1, 2) INFINITY POINT on reference triangle ABC."""
    X_742 = eval_trilinear_point(model, A, B, C, 'a**(-2)*(b**(2)+ c**(2)) - a**(1)*(b**(-1)+ c**(-1))', ID="X(742)", classes=["selected", "target"])
    X_6 = symmedian_point_of(model, A, B, C, ID="X(6)", classes=["center", "incident"])
    X_75 = eval_trilinear_point(model, A, B, C, '1/a**(2)', ID="X(75)", classes=["center", "incident"])
    central_line(model, X_6, X_75, 6, 75, incident=True)
    X_37 = eval_trilinear_point(model, A, B, C, 'b + c', ID="X(37)", classes=["center", "incident"])
    X_141 = eval_trilinear_point(model, A, B, C, 'b*c*(b**(2) + c**(2))', ID="X(141)", classes=["center", "incident"])
    central_line(model, X_37, X_141, 37, 141, incident=True)
    X_69 = eval_trilinear_point(model, A, B, C, '(cos(A))/a**(2)', ID="X(69)", classes=["center", "incident"])
    X_192 = eval_trilinear_point(model, A, B, C, 'b*c*(c*a + a*b - b*c)', ID="X(192)", classes=["center", "incident"])
    central_line(model, X_69, X_192, 69, 192, incident=True)
    return promote_point_to_top(model, X_742)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(742) on the given reference triangle."""
    model = create_model('X(742) = EVEN (- 1, 2) INFINITY POINT')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00742(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00742.json"))
    write_center_svg(
        model_acute,
        here / "x-00742.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
