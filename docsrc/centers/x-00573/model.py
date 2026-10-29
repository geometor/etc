"""GEOMETOR construction model for X(573) = ORTHOHARMONIC OF X(58)."""

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
    mittenpunkt_of,
    orthocenter_of,
    promote_point_to_top,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_00573(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(573) = ORTHOHARMONIC OF X(58) on reference triangle ABC."""
    X_573 = eval_trilinear_point(model, A, B, C, '(c - a)*cos(B)*sin(A - B) - (a - b)*cos(C)*sin(C - A)', ID="X(573)", classes=["selected", "target"])
    X_3 = circumcenter_of(model, A, B, C, ID="X(3)", classes=["center", "incident"])
    X_6 = symmedian_point_of(model, A, B, C, ID="X(6)", classes=["center", "incident"])
    central_line(model, X_3, X_6, 3, 6, incident=True)
    X_4 = orthocenter_of(model, A, B, C, ID="X(4)", classes=["center", "incident"])
    X_9 = mittenpunkt_of(model, A, B, C, ID="X(9)", classes=["center", "incident"])
    central_line(model, X_4, X_9, 4, 9, incident=True)
    X_101 = eval_trilinear_point(model, A, B, C, 'a/(b - c)', ID="X(101)", classes=["center", "incident"])
    X_102 = eval_trilinear_point(model, A, B, C, '1/(sin(B)*(sec(A) - sec(B)) + sin(C)*(sec(A) - sec(C)))', ID="X(102)", classes=["center", "incident"])
    central_line(model, X_101, X_102, 101, 102, incident=True)
    return promote_point_to_top(model, X_573)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(573) on the given reference triangle."""
    model = create_model('X(573) = ORTHOHARMONIC OF X(58)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00573(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00573.json"))
    write_center_svg(
        model_acute,
        here / "x-00573.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
