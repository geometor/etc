"""GEOMETOR construction model for X(953) = ISOGONAL CONJUGATE OF X(952)."""

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
    promote_point_to_top,
    reflection_in_point,
)
from geometor.etc.render import write_center_svg


def construct_x_00953(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(953) = ISOGONAL CONJUGATE OF X(952) on reference triangle ABC."""
    X_901 = eval_trilinear_point(model, A, B, C, 'a/((b - c)*(b + c - 2*a))', ID="X(901)", classes=["center"])
    X_3 = circumcenter_of(model, A, B, C, ID="X(3)", classes=["center"])
    X_953 = reflection_in_point(model, X_901, X_3, ID="X(953)", classes=["selected", "target"], guide=False)
    X_36 = eval_trilinear_point(model, A, B, C, '1 - 2*cos(A)', ID="X(36)", classes=["center", "incident"])
    X_109 = eval_trilinear_point(model, A, B, C, 'a/(cos(B) - cos(C))', ID="X(109)", classes=["center", "incident"])
    central_line(model, X_36, X_109, 36, 109, incident=True)
    X_100 = eval_trilinear_point(model, A, B, C, '1/(b - c)', ID="X(100)", classes=["center", "incident"])
    X_517 = eval_trilinear_point(model, A, B, C, '-1 + cos(B) + cos(C)', ID="X(517)", classes=["center", "incident"])
    central_line(model, X_100, X_517, 100, 517, incident=True)
    X_104 = eval_trilinear_point(model, A, B, C, '1/(-1 + cos(B) + cos(C))', ID="X(104)", classes=["center", "incident"])
    X_513 = eval_trilinear_point(model, A, B, C, 'b - c', ID="X(513)", classes=["center", "incident"])
    central_line(model, X_104, X_513, 104, 513, incident=True)
    return promote_point_to_top(model, X_953)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(953) on the given reference triangle."""
    model = create_model('X(953) = ISOGONAL CONJUGATE OF X(952)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00953(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00953.json"))
    write_center_svg(
        model_acute,
        here / "x-00953.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
