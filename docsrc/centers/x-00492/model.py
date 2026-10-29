"""GEOMETOR construction model for X(492) = CEVAPOINT OF X(2) AND X(488)."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    centroid_of,
    circumcenter_of,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    isotomic_conjugate,
    orthocenter_of,
    promote_point_to_top,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_00492(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(492) = CEVAPOINT OF X(2) AND X(488) on reference triangle ABC."""
    X_485 = eval_trilinear_point(model, A, B, C, 'sec(A - pi /4)', ID="X(485)", classes=["center"])
    X_492 = isotomic_conjugate(model, A, B, C, X_485, ID="X(492)", classes=["selected", "target"])
    X_2 = centroid_of(model, A, B, C, ID="X(2)", classes=["center", "incident"])
    X_6 = symmedian_point_of(model, A, B, C, ID="X(6)", classes=["center", "incident"])
    central_line(model, X_2, X_6, 2, 6, incident=True)
    X_3 = circumcenter_of(model, A, B, C, ID="X(3)", classes=["center", "incident"])
    X_489 = eval_trilinear_point(model, A, B, C, '(cos(A))*(1 - csc(A)*sin(B)*sin(C)) - cos(B)*cos(C)', ID="X(489)", classes=["center", "incident"])
    central_line(model, X_3, X_489, 3, 489, incident=True)
    X_4 = orthocenter_of(model, A, B, C, ID="X(4)", classes=["center", "incident"])
    X_488 = eval_trilinear_point(model, A, B, C, '(cos(A))*(1 + csc(A)*sin(B)*sin(C))', ID="X(488)", classes=["center", "incident"])
    central_line(model, X_4, X_488, 4, 488, incident=True)
    return promote_point_to_top(model, X_492)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(492) on the given reference triangle."""
    model = create_model('X(492) = CEVAPOINT OF X(2) AND X(488)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00492(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00492.json"))
    write_center_svg(
        model_acute,
        here / "x-00492.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
