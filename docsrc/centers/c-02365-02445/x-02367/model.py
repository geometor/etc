"""GEOMETOR construction model for X_2367 = CIR(X_32)."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    intersect_lines,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_02367(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2367 = CIR(X_32) on reference triangle ABC."""
    X_76 = eval_trilinear_point(model, A, B, C, '1/a**(3)', ID="X_76", classes=["center"])
    X_110 = eval_trilinear_point(model, A, B, C, 'csc(B - C)', ID="X_110", classes=["center"])
    X_99 = eval_trilinear_point(model, A, B, C, 'b*c/(b**(2) - c**(2))', ID="X_99", classes=["center"])
    X_160 = eval_trilinear_point(model, A, B, C, '(a*((b**(2) + c**(2))*sin(2*A) + (c**(2) - a**(2))*sin(2*B) + (b**(2) - a**(2))*sin(2*C)))', ID="X_160", classes=["center"])
    central_line(model, X_76, X_110, 76, 110)
    central_line(model, X_99, X_160, 99, 160)
    X_2367 = intersect_lines(model, X_76, X_110, X_99, X_160, ID="X_2367", classes=["selected", "target"])
    X_112 = eval_trilinear_point(model, A, B, C, 'a/(sin(2*B) - sin(2*C))', ID="X_112", classes=["center", "incident"])
    X_264 = eval_trilinear_point(model, A, B, C, 'csc(A)*csc(2*A)', ID="X_264", classes=["center", "incident"])
    central_line(model, X_112, X_264, 112, 264, incident=True)
    return promote_point_to_top(model, X_2367)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2367 on the given reference triangle."""
    model = create_model('X_2367 = CIR(X_32)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02367(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02367.json"))
    write_center_svg(
        model_acute,
        here / "x-02367.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
