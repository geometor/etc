"""GEOMETOR construction model for X_1739 = MIMOSA TRANSFORM OF X_106."""

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
    incenter_of,
    promote_point_to_top,
    spieker_center_of,
)
from geometor.etc.render import write_center_svg


def construct_x_01739(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1739 = MIMOSA TRANSFORM OF X_106 on reference triangle ABC."""
    X_75 = eval_trilinear_point(model, A, B, C, '1/a**(2)', ID="X_75", classes=["center"])
    X_88 = eval_trilinear_point(model, A, B, C, '1/(b + c - 2*a)', ID="X_88", classes=["center"])
    X_1739 = crosspoint(model, A, B, C, X_75, X_88, ID="X_1739", classes=["selected", "target"])
    X_10 = spieker_center_of(model, A, B, C, ID="X_10", classes=["center", "incident"])
    X_38 = eval_trilinear_point(model, A, B, C, 'b**(2) + c**(2)', ID="X_38", classes=["center", "incident"])
    central_line(model, X_10, X_38, 10, 38, incident=True)
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center", "incident"])
    X_474 = eval_trilinear_point(model, A, B, C, 'cos(A) - (a + b + c)/a', ID="X_474", classes=["center", "incident"])
    central_line(model, X_1, X_474, 1, 474, incident=True)
    X_238 = eval_trilinear_point(model, A, B, C, 'a**(2) - b*c', ID="X_238", classes=["center", "incident"])
    X_484 = eval_trilinear_point(model, A, B, C, '1 + 2*(cos(A) - cos(B) - cos(C))', ID="X_484", classes=["center", "incident"])
    central_line(model, X_238, X_484, 238, 484, incident=True)
    return promote_point_to_top(model, X_1739)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1739 on the given reference triangle."""
    model = create_model('X_1739 = MIMOSA TRANSFORM OF X_106')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01739(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01739.json"))
    write_center_svg(
        model_acute,
        here / "x-01739.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
