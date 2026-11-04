"""GEOMETOR construction model for X_1401 = X_38-BETH CONJUGATE OF X_38."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    crosspoint,
    eval_trilinear_point,
    gergonne_point_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_01401(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1401 = X_38-BETH CONJUGATE OF X_38 on reference triangle ABC."""
    X_7 = gergonne_point_of(model, A, B, C, ID="X_7", classes=["center"])
    X_56 = eval_trilinear_point(model, A, B, C, 'a/(b + c - a)', ID="X_56", classes=["center"])
    X_1401 = crosspoint(model, A, B, C, X_7, X_56, ID="X_1401", classes=["selected", "target"])
    X_43 = eval_trilinear_point(model, A, B, C, 'a*b + a*c - b*c', ID="X_43", classes=["center", "incident"])
    X_57 = eval_trilinear_point(model, A, B, C, '1/(b + c - a)', ID="X_57", classes=["center", "incident"])
    central_line(model, X_43, X_57, 43, 57, incident=True)
    X_58 = eval_trilinear_point(model, A, B, C, 'a/(b + c)', ID="X_58", classes=["center", "incident"])
    central_line(model, X_56, X_58, 56, 58, incident=True)
    X_51 = eval_trilinear_point(model, A, B, C, 'a**(2)*cos(B - C)', ID="X_51", classes=["center", "incident"])
    X_244 = eval_trilinear_point(model, A, B, C, '(b - c)**(2)', ID="X_244", classes=["center", "incident"])
    central_line(model, X_51, X_244, 51, 244, incident=True)
    return promote_point_to_top(model, X_1401)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1401 on the given reference triangle."""
    model = create_model('X_1401 = X_38-BETH CONJUGATE OF X_38')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01401(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01401.json"))
    write_center_svg(
        model_acute,
        here / "x-01401.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
