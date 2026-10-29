"""GEOMETOR construction model for X(267) = ISOGONAL CONJUGATE OF X(191)."""

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
    point_from_barycentrics,
    promote_point_to_top,
    reflection_in_point,
    spieker_center_of,
)
from geometor.etc.render import write_center_svg


def construct_x_00267(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(267) = ISOGONAL CONJUGATE OF X(191) on reference triangle ABC."""
    X_1 = incenter_of(model, A, B, C, ID="X(1)", classes=["center"])
    X_229 = point_from_barycentrics(model, A, B, C, 0.21061481, 0.29086323, 0.49852195, ID="X(229)", classes=["center"])
    X_267 = reflection_in_point(model, X_1, X_229, ID="X(267)", classes=["selected", "target"], guide=False)
    X_35 = eval_trilinear_point(model, A, B, C, '1 + 2*cos(A)', ID="X(35)", classes=["center", "incident"])
    X_37 = eval_trilinear_point(model, A, B, C, 'b + c', ID="X(37)", classes=["center", "incident"])
    central_line(model, X_35, X_37, 35, 37, incident=True)
    X_10 = spieker_center_of(model, A, B, C, ID="X(10)", classes=["center", "incident"])
    X_191 = eval_trilinear_point(model, A, B, C, '(b + c - a)*(b*c + c*a + a*b) + b**(3) + c**(3) - a**(3)', ID="X(191)", classes=["center", "incident"])
    central_line(model, X_10, X_191, 10, 191, incident=True)
    central_line(model, X_1, X_229, 1, 229, incident=True)
    return promote_point_to_top(model, X_267)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(267) on the given reference triangle."""
    model = create_model('X(267) = ISOGONAL CONJUGATE OF X(191)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00267(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00267.json"))
    write_center_svg(
        model_acute,
        here / "x-00267.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
