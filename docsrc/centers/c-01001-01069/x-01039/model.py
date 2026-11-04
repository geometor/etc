"""GEOMETOR construction model for X_1039 = ISOGONAL CONJUGATE OF X_1038."""

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


def construct_x_01039(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1039 = ISOGONAL CONJUGATE OF X_1038 on reference triangle ABC."""
    X_1038 = eval_trilinear_point(model, A, B, C, 'cos(A) + cos(A)*cos(B)*cos(C)', ID="X_1038", classes=["center"])
    X_1039 = isogonal_conjugate(model, A, B, C, X_1038, ID="X_1039", classes=["selected", "target"])
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center", "incident"])
    X_25 = eval_trilinear_point(model, A, B, C, 'sin(A)*tan(A)', ID="X_25", classes=["center", "incident"])
    central_line(model, X_1, X_25, 1, 25, incident=True)
    X_7 = gergonne_point_of(model, A, B, C, ID="X_7", classes=["center", "incident"])
    X_34 = eval_trilinear_point(model, A, B, C, '1 - sec(A)', ID="X_34", classes=["center", "incident"])
    central_line(model, X_7, X_34, 7, 34, incident=True)
    X_8 = nagel_point_of(model, A, B, C, ID="X_8", classes=["center", "incident"])
    X_33 = eval_trilinear_point(model, A, B, C, '1 + sec(A)', ID="X_33", classes=["center", "incident"])
    central_line(model, X_8, X_33, 8, 33, incident=True)
    return promote_point_to_top(model, X_1039)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1039 on the given reference triangle."""
    model = create_model('X_1039 = ISOGONAL CONJUGATE OF X_1038')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01039(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01039.json"))
    write_center_svg(
        model_acute,
        here / "x-01039.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
