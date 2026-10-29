"""GEOMETOR construction model for X(568) = ORTHOHARMONIC OF X(50)."""

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
    orthocenter_of,
    promote_point_to_top,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_00568(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(568) = ORTHOHARMONIC OF X(50) on reference triangle ABC."""
    X_568 = eval_trilinear_point(model, A, B, C, 'a*(3*R**(2)*(b**(2) + c**(2) - a**(2)) + a**(2)*b**(2) + a**(2)*c**(2) - b**(4) - c**(4))', ID="X(568)", classes=["selected", "target"])
    X_3 = circumcenter_of(model, A, B, C, ID="X(3)", classes=["center", "incident"])
    X_6 = symmedian_point_of(model, A, B, C, ID="X(6)", classes=["center", "incident"])
    central_line(model, X_3, X_6, 3, 6, incident=True)
    X_24 = eval_trilinear_point(model, A, B, C, 'sec(A)*cos(2*A)', ID="X(24)", classes=["center", "incident"])
    X_49 = eval_trilinear_point(model, A, B, C, 'cos(3*A)', ID="X(49)", classes=["center", "incident"])
    central_line(model, X_24, X_49, 24, 49, incident=True)
    X_4 = orthocenter_of(model, A, B, C, ID="X(4)", classes=["center", "incident"])
    X_94 = eval_trilinear_point(model, A, B, C, 'csc(3*A)', ID="X(94)", classes=["center", "incident"])
    central_line(model, X_4, X_94, 4, 94, incident=True)
    return promote_point_to_top(model, X_568)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(568) on the given reference triangle."""
    model = create_model('X(568) = ORTHOHARMONIC OF X(50)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00568(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00568.json"))
    write_center_svg(
        model_acute,
        here / "x-00568.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
