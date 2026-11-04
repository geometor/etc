"""GEOMETOR construction model for X_1745 = MIMOSA TRANSFORM OF X_255."""

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
    orthocenter_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_01745(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1745 = MIMOSA TRANSFORM OF X_255 on reference triangle ABC."""
    X_1745 = eval_trilinear_point(model, A, B, C, '(sec(B) + sec(C) - sec(A))', ID="X_1745", classes=["selected", "target"])
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center", "incident"])
    X_4 = orthocenter_of(model, A, B, C, ID="X_4", classes=["center", "incident"])
    central_line(model, X_1, X_4, 1, 4, incident=True)
    X_43 = eval_trilinear_point(model, A, B, C, 'a*b + a*c - b*c', ID="X_43", classes=["center", "incident"])
    X_46 = eval_trilinear_point(model, A, B, C, 'cos(B) + cos(C) - cos(A)', ID="X_46", classes=["center", "incident"])
    central_line(model, X_43, X_46, 43, 46, incident=True)
    X_255 = eval_trilinear_point(model, A, B, C, '(cos(A))**(2)', ID="X_255", classes=["center", "incident"])
    X_411 = eval_trilinear_point(model, A, B, C, '(cos(B)*cos(C) - (cos(A) + cos(B) + cos(C))*cos(A))', ID="X_411", classes=["center", "incident"])
    central_line(model, X_255, X_411, 255, 411, incident=True)
    return promote_point_to_top(model, X_1745)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1745 on the given reference triangle."""
    model = create_model('X_1745 = MIMOSA TRANSFORM OF X_255')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01745(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01745.json"))
    write_center_svg(
        model_acute,
        here / "x-01745.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
