"""GEOMETOR construction model for X(983) = ISOGONAL CONJUGATE OF X(982)."""

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
    isogonal_conjugate,
    nagel_point_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00983(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(983) = ISOGONAL CONJUGATE OF X(982) on reference triangle ABC."""
    X_982 = eval_trilinear_point(model, A, B, C, 'b**(2)- b*c + c**(2)', ID="X(982)", classes=["center"])
    X_983 = isogonal_conjugate(model, A, B, C, X_982, ID="X(983)", classes=["selected", "target"])
    X_7 = gergonne_point_of(model, A, B, C, ID="X(7)", classes=["center", "incident"])
    X_171 = eval_trilinear_point(model, A, B, C, 'a**(2) + b*c', ID="X(171)", classes=["center", "incident"])
    central_line(model, X_7, X_171, 7, 171, incident=True)
    X_1 = incenter_of(model, A, B, C, ID="X(1)", classes=["center", "incident"])
    X_182 = eval_trilinear_point(model, A, B, C, 'cos(A- omega )', ID="X(182)", classes=["center", "incident"])
    central_line(model, X_1, X_182, 1, 182, incident=True)
    X_8 = nagel_point_of(model, A, B, C, ID="X(8)", classes=["center", "incident"])
    X_238 = eval_trilinear_point(model, A, B, C, 'a**(2) - b*c', ID="X(238)", classes=["center", "incident"])
    central_line(model, X_8, X_238, 8, 238, incident=True)
    return promote_point_to_top(model, X_983)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(983) on the given reference triangle."""
    model = create_model('X(983) = ISOGONAL CONJUGATE OF X(982)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00983(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00983.json"))
    write_center_svg(
        model_acute,
        here / "x-00983.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
