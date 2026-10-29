"""GEOMETOR construction model for X(255) = ISOGONAL CONJUGATE OF X(158)."""

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
    incenter_of,
    isogonal_conjugate,
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00255(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(255) = ISOGONAL CONJUGATE OF X(158) on reference triangle ABC."""
    X_158 = point_from_barycentrics(model, A, B, C, 0.04776757, 0.099240104, 0.85299233, ID="X(158)", classes=["center"])
    X_255 = isogonal_conjugate(model, A, B, C, X_158, ID="X(255)", classes=["selected", "target"])
    X_1 = incenter_of(model, A, B, C, ID="X(1)", classes=["center", "incident"])
    X_21 = eval_trilinear_point(model, A, B, C, '1/(cos(B) + cos(C))', ID="X(21)", classes=["center", "incident"])
    central_line(model, X_1, X_21, 1, 21, incident=True)
    X_3 = circumcenter_of(model, A, B, C, ID="X(3)", classes=["center", "incident"])
    X_73 = eval_trilinear_point(model, A, B, C, 'sec(B) + sec(C)', ID="X(73)", classes=["center", "incident"])
    central_line(model, X_3, X_73, 3, 73, incident=True)
    X_40 = eval_trilinear_point(model, A, B, C, 'cos(B) + cos(C) - cos(A) - 1', ID="X(40)", classes=["center", "incident"])
    X_109 = eval_trilinear_point(model, A, B, C, 'a/(cos(B) - cos(C))', ID="X(109)", classes=["center", "incident"])
    central_line(model, X_40, X_109, 40, 109, incident=True)
    return promote_point_to_top(model, X_255)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(255) on the given reference triangle."""
    model = create_model('X(255) = ISOGONAL CONJUGATE OF X(158)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00255(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00255.json"))
    write_center_svg(
        model_acute,
        here / "x-00255.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
