"""GEOMETOR construction model for X(694) = ISOGONAL CONJUGATE OF X(385)."""

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


def construct_x_00694(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(694) = ISOGONAL CONJUGATE OF X(385) on reference triangle ABC."""
    X_385 = eval_trilinear_point(model, A, B, C, 'b*c*(a**(4) - b**(2)*c**(2))', ID="X(385)", classes=["center"])
    X_694 = isogonal_conjugate(model, A, B, C, X_385, ID="X(694)", classes=["selected", "target"])
    X_37 = eval_trilinear_point(model, A, B, C, 'b + c', ID="X(37)", classes=["center", "incident"])
    X_256 = eval_trilinear_point(model, A, B, C, '1/(a**(2) + b*c)', ID="X(256)", classes=["center", "incident"])
    central_line(model, X_37, X_256, 37, 256, incident=True)
    X_110 = eval_trilinear_point(model, A, B, C, 'csc(B - C)', ID="X(110)", classes=["center", "incident"])
    X_251 = eval_trilinear_point(model, A, B, C, 'a**(2)*csc(A + omega )', ID="X(251)", classes=["center", "incident"])
    central_line(model, X_110, X_251, 110, 251, incident=True)
    X_141 = eval_trilinear_point(model, A, B, C, 'b*c*(b**(2) + c**(2))', ID="X(141)", classes=["center", "incident"])
    X_308 = eval_trilinear_point(model, A, B, C, 'b**(3)*c**(3)/(b**(2) + c**(2))', ID="X(308)", classes=["center", "incident"])
    central_line(model, X_141, X_308, 141, 308, incident=True)
    return promote_point_to_top(model, X_694)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(694) on the given reference triangle."""
    model = create_model('X(694) = ISOGONAL CONJUGATE OF X(385)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00694(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00694.json"))
    write_center_svg(
        model_acute,
        here / "x-00694.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
