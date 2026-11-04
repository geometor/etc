"""GEOMETOR construction model for X_1708 = MIMOSA TRANSFORM OF X_7."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    centroid_of,
    ceva_conjugate,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    gergonne_point_of,
    incenter_of,
    orthocenter_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_01708(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1708 = MIMOSA TRANSFORM OF X_7 on reference triangle ABC."""
    X_273 = eval_trilinear_point(model, A, B, C, 'sec(A)*(sec(A/2))**(2)', ID="X_273", classes=["center"])
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center"])
    X_1708 = ceva_conjugate(model, A, B, C, X_273, X_1, ID="X_1708", classes=["selected", "target"])
    X_2 = centroid_of(model, A, B, C, ID="X_2", classes=["center", "incident"])
    X_7 = gergonne_point_of(model, A, B, C, ID="X_7", classes=["center", "incident"])
    central_line(model, X_2, X_7, 2, 7, incident=True)
    X_4 = orthocenter_of(model, A, B, C, ID="X_4", classes=["center", "incident"])
    X_46 = eval_trilinear_point(model, A, B, C, 'cos(B) + cos(C) - cos(A)', ID="X_46", classes=["center", "incident"])
    central_line(model, X_4, X_46, 4, 46, incident=True)
    X_56 = eval_trilinear_point(model, A, B, C, 'a/(b + c - a)', ID="X_56", classes=["center", "incident"])
    X_72 = eval_trilinear_point(model, A, B, C, '(b + c)*cot(A)', ID="X_72", classes=["center", "incident"])
    central_line(model, X_56, X_72, 56, 72, incident=True)
    return promote_point_to_top(model, X_1708)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1708 on the given reference triangle."""
    model = create_model('X_1708 = MIMOSA TRANSFORM OF X_7')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01708(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01708.json"))
    write_center_svg(
        model_acute,
        here / "x-01708.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
