"""GEOMETOR construction model for X_1802 = INVERSE MIMOSA TRANSFORM OF X_170."""

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
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_01802(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1802 = INVERSE MIMOSA TRANSFORM OF X_170 on reference triangle ABC."""
    X_1802 = eval_trilinear_point(model, A, B, C, '(1 + cos(A))**(2)*cot(A)', ID="X_1802", classes=["selected", "target"])
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center", "incident"])
    X_48 = eval_trilinear_point(model, A, B, C, 'tan(B) + tan(C)', ID="X_48", classes=["center", "incident"])
    central_line(model, X_3, X_48, 3, 48, incident=True)
    X_41 = eval_trilinear_point(model, A, B, C, 'a**(2)*(b + c - a)', ID="X_41", classes=["center", "incident"])
    X_55 = eval_trilinear_point(model, A, B, C, 'a*(b + c - a)', ID="X_55", classes=["center", "incident"])
    central_line(model, X_41, X_55, 41, 55, incident=True)
    X_40 = eval_trilinear_point(model, A, B, C, 'cos(B) + cos(C) - cos(A) - 1', ID="X_40", classes=["center", "incident"])
    X_101 = eval_trilinear_point(model, A, B, C, 'a/(b - c)', ID="X_101", classes=["center", "incident"])
    central_line(model, X_40, X_101, 40, 101, incident=True)
    return promote_point_to_top(model, X_1802)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1802 on the given reference triangle."""
    model = create_model('X_1802 = INVERSE MIMOSA TRANSFORM OF X_170')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01802(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01802.json"))
    write_center_svg(
        model_acute,
        here / "x-01802.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
