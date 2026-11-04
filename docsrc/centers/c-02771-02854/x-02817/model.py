"""GEOMETOR construction model for X_2817 = ISOGONAL CONJUGATE OF X_2733."""

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
    isogonal_conjugate,
    point_from_barycentrics,
    promote_point_to_top,
    spieker_center_of,
)
from geometor.etc.render import write_center_svg


def construct_x_02817(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2817 = ISOGONAL CONJUGATE OF X_2733 on reference triangle ABC."""
    X_2733 = point_from_barycentrics(model, A, B, C, 0.94642546, 0.65687043, -0.60329589, ID="X_2733", classes=["center"])
    X_2817 = isogonal_conjugate(model, A, B, C, X_2733, ID="X_2817", classes=["selected", "target"])
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center", "incident"])
    X_102 = eval_trilinear_point(model, A, B, C, '1/(sin(B)*(sec(A) - sec(B)) + sin(C)*(sec(A) - sec(C)))', ID="X_102", classes=["center", "incident"])
    central_line(model, X_1, X_102, 1, 102, incident=True)
    X_10 = spieker_center_of(model, A, B, C, ID="X_10", classes=["center", "incident"])
    X_117 = point_from_barycentrics(model, A, B, C, 0.19223485, -0.017045455, 0.82481061, ID="X_117", classes=["center", "incident"])
    central_line(model, X_10, X_117, 10, 117, incident=True)
    X_40 = eval_trilinear_point(model, A, B, C, 'cos(B) + cos(C) - cos(A) - 1', ID="X_40", classes=["center", "incident"])
    X_109 = eval_trilinear_point(model, A, B, C, 'a/(cos(B) - cos(C))', ID="X_109", classes=["center", "incident"])
    central_line(model, X_40, X_109, 40, 109, incident=True)
    return promote_point_to_top(model, X_2817)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2817 on the given reference triangle."""
    model = create_model('X_2817 = ISOGONAL CONJUGATE OF X_2733')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02817(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02817.json"))
    write_center_svg(
        model_acute,
        here / "x-02817.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
