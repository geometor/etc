"""GEOMETOR construction model for X(727) = EVEN (- 2, -1) CIRCUMCIRCLE POINT."""

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
    isogonal_conjugate,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00727(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(727) = EVEN (- 2, -1) CIRCUMCIRCLE POINT on reference triangle ABC."""
    X_726 = eval_barycentric_point(model, A, B, C, 'a*(b**(2) + c**(2)) - b*c*(b + c)', ID="X(726)", classes=["center"])
    X_727 = isogonal_conjugate(model, A, B, C, X_726, ID="X(727)", classes=["selected", "target"])
    X_31 = eval_trilinear_point(model, A, B, C, 'a**(2)', ID="X(31)", classes=["center", "incident"])
    X_43 = eval_trilinear_point(model, A, B, C, 'a*b + a*c - b*c', ID="X(43)", classes=["center", "incident"])
    central_line(model, X_31, X_43, 31, 43, incident=True)
    X_32 = eval_trilinear_point(model, A, B, C, 'a**(3)', ID="X(32)", classes=["center", "incident"])
    X_101 = eval_trilinear_point(model, A, B, C, 'a/(b - c)', ID="X(101)", classes=["center", "incident"])
    central_line(model, X_32, X_101, 32, 101, incident=True)
    X_58 = eval_trilinear_point(model, A, B, C, 'a/(b + c)', ID="X(58)", classes=["center", "incident"])
    X_99 = eval_trilinear_point(model, A, B, C, 'b*c/(b**(2) - c**(2))', ID="X(99)", classes=["center", "incident"])
    central_line(model, X_58, X_99, 58, 99, incident=True)
    return promote_point_to_top(model, X_727)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(727) on the given reference triangle."""
    model = create_model('X(727) = EVEN (- 2, -1) CIRCUMCIRCLE POINT')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00727(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00727.json"))
    write_center_svg(
        model_acute,
        here / "x-00727.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
