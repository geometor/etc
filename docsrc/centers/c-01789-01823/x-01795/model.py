"""GEOMETOR construction model for X_1795 = INVERSE MIMOSA TRANSFORM OF X_36."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    incenter_of,
    isogonal_conjugate,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_01795(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1795 = INVERSE MIMOSA TRANSFORM OF X_36 on reference triangle ABC."""
    X_1785 = eval_trilinear_point(model, A, B, C, '(sec(A))*(cos(B) + cos(C) - 1)', ID="X_1785", classes=["center"])
    X_1795 = isogonal_conjugate(model, A, B, C, X_1785, ID="X_1795", classes=["selected", "target"])
    X_29 = eval_trilinear_point(model, A, B, C, '(sec(A))/(cos(B) + cos(C))', ID="X_29", classes=["center", "incident"])
    X_58 = eval_trilinear_point(model, A, B, C, 'a/(b + c)', ID="X_58", classes=["center", "incident"])
    central_line(model, X_29, X_58, 29, 58, incident=True)
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center", "incident"])
    X_104 = eval_trilinear_point(model, A, B, C, '1/(-1 + cos(B) + cos(C))', ID="X_104", classes=["center", "incident"])
    central_line(model, X_1, X_104, 1, 104, incident=True)
    X_36 = eval_trilinear_point(model, A, B, C, '1 - 2*cos(A)', ID="X_36", classes=["center", "incident"])
    X_102 = eval_trilinear_point(model, A, B, C, '1/(sin(B)*(sec(A) - sec(B)) + sin(C)*(sec(A) - sec(C)))', ID="X_102", classes=["center", "incident"])
    central_line(model, X_36, X_102, 36, 102, incident=True)
    return promote_point_to_top(model, X_1795)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1795 on the given reference triangle."""
    model = create_model('X_1795 = INVERSE MIMOSA TRANSFORM OF X_36')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01795(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01795.json"))
    write_center_svg(
        model_acute,
        here / "x-01795.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
