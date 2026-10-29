"""GEOMETOR construction model for X(885) = ISOTOMIC CONJUGATE OF X(883)."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    gergonne_point_of,
    incenter_of,
    isotomic_conjugate,
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00885(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(885) = ISOTOMIC CONJUGATE OF X(883) on reference triangle ABC."""
    X_883 = point_from_barycentrics(model, A, B, C, -1.5, 0.1, 2.4, ID="X(883)", classes=["center"])
    X_885 = isotomic_conjugate(model, A, B, C, X_883, ID="X(885)", classes=["selected", "target"])
    X_104 = eval_trilinear_point(model, A, B, C, '1/(-1 + cos(B) + cos(C))', ID="X(104)", classes=["center", "incident"])
    X_105 = eval_trilinear_point(model, A, B, C, '1/(b**(2) + c**(2) - a*(b + c))', ID="X(105)", classes=["center", "incident"])
    central_line(model, X_104, X_105, 104, 105, incident=True)
    X_1 = incenter_of(model, A, B, C, ID="X(1)", classes=["center", "incident"])
    X_514 = eval_trilinear_point(model, A, B, C, '(b - c)/a', ID="X(514)", classes=["center", "incident"])
    central_line(model, X_1, X_514, 1, 514, incident=True)
    X_7 = gergonne_point_of(model, A, B, C, ID="X(7)", classes=["center", "incident"])
    X_513 = eval_trilinear_point(model, A, B, C, 'b - c', ID="X(513)", classes=["center", "incident"])
    central_line(model, X_7, X_513, 7, 513, incident=True)
    return promote_point_to_top(model, X_885)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(885) on the given reference triangle."""
    model = create_model('X(885) = ISOTOMIC CONJUGATE OF X(883)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00885(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00885.json"))
    write_center_svg(
        model_acute,
        here / "x-00885.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
