"""GEOMETOR construction model for X_3477 = ISOGONAL CONJUGATE OF X_3475."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    circumcenter_of,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    isogonal_conjugate,
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_03477(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3477 = ISOGONAL CONJUGATE OF X_3475 on reference triangle ABC."""
    X_3475 = eval_trilinear_point(model, A, B, C, '2 + cos(A) + cos(B) + cos(C) + cos(B)*cos(C)', ID="X_3475", classes=["center"])
    X_3477 = isogonal_conjugate(model, A, B, C, X_3475, ID="X_3477", classes=["selected", "target"])
    X_77 = eval_trilinear_point(model, A, B, C, '1/(1 + sec(A))', ID="X_77", classes=["center", "incident"])
    X_354 = eval_trilinear_point(model, A, B, C, '(b - c)**(2) - a*b - a*c', ID="X_354", classes=["center", "incident"])
    central_line(model, X_77, X_354, 77, 354, incident=True)
    X_78 = eval_trilinear_point(model, A, B, C, '1/(1 - sec(A))', ID="X_78", classes=["center", "incident"])
    X_1001 = eval_trilinear_point(model, A, B, C, 'a**(2) - a*(b + c) - 2*b*c', ID="X_1001", classes=["center", "incident"])
    central_line(model, X_78, X_1001, 78, 1001, incident=True)
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center", "incident"])
    X_1471 = point_from_barycentrics(model, A, B, C, 0.1843921, 0.30264097, 0.51296693, ID="X_1471", classes=["center", "incident"])
    central_line(model, X_3, X_1471, 3, 1471, incident=True)
    return promote_point_to_top(model, X_3477)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3477 on the given reference triangle."""
    model = create_model('X_3477 = ISOGONAL CONJUGATE OF X_3475')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03477(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03477.json"))
    write_center_svg(
        model_acute,
        here / "x-03477.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
