"""GEOMETOR construction model for X(170) = X(9)-ALEPH CONJUGATE OF X(9)."""

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
    gergonne_point_of,
    incenter_of,
    intersect_lines,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00170(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(170) = X(9)-ALEPH CONJUGATE OF X(9) on reference triangle ABC."""
    X_1 = incenter_of(model, A, B, C, ID="X(1)", classes=["center"])
    X_7 = gergonne_point_of(model, A, B, C, ID="X(7)", classes=["center"])
    X_43 = eval_trilinear_point(model, A, B, C, 'a*b + a*c - b*c', ID="X(43)", classes=["center"])
    X_218 = eval_barycentric_point(model, A, B, C, 'a**(2)*(a**(2) + b**(2) + c**(2) - 2*a*b - 2*a*c)', ID="X(218)", classes=["center"])
    central_line(model, X_1, X_7, 1, 7)
    central_line(model, X_43, X_218, 43, 218)
    X_170 = intersect_lines(model, X_1, X_7, X_43, X_218, ID="X(170)", classes=["selected", "target"])
    return promote_point_to_top(model, X_170)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(170) on the given reference triangle."""
    model = create_model('X(170) = X(9)-ALEPH CONJUGATE OF X(9)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00170(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00170.json"))
    write_center_svg(
        model_acute,
        here / "x-00170.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
