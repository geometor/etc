"""GEOMETOR construction model for X_2750 = SR(X_105, X_108)."""

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
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_02750(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2750 = SR(X_105, X_108) on reference triangle ABC."""
    X_105 = eval_trilinear_point(model, A, B, C, '1/(b**(2) + c**(2) - a*(b + c))', ID="X_105", classes=["center"])
    X_521 = eval_trilinear_point(model, A, B, C, '(sec(B) - sec(C))*(csc(A))', ID="X_521", classes=["center"])
    X_108 = eval_trilinear_point(model, A, B, C, 'a/(sec(B) - sec(C))', ID="X_108", classes=["center"])
    X_518 = eval_trilinear_point(model, A, B, C, '(a*b + a*c - b**(2) - c**(2))', ID="X_518", classes=["center"])
    central_line(model, X_105, X_521, 105, 521)
    central_line(model, X_108, X_518, 108, 518)
    X_2750 = intersect_lines(model, X_105, X_521, X_108, X_518, ID="X_2750", classes=["selected", "target"])
    X_69 = eval_trilinear_point(model, A, B, C, '(cos(A))/a**(2)', ID="X_69", classes=["center", "incident"])
    X_927 = point_from_barycentrics(model, A, B, C, -0.12244898, 0.81632653, 0.30612245, ID="X_927", classes=["center", "incident"])
    central_line(model, X_69, X_927, 69, 927, incident=True)
    return promote_point_to_top(model, X_2750)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2750 on the given reference triangle."""
    model = create_model('X_2750 = SR(X_105, X_108)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02750(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02750.json"))
    write_center_svg(
        model_acute,
        here / "x-02750.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
