"""GEOMETOR construction model for X_2108 = POINT KEPLER I."""

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
)
from geometor.etc.render import write_center_svg


def construct_x_02108(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2108 = POINT KEPLER I on reference triangle ABC."""
    X_2108 = eval_trilinear_point(model, A, B, C, '((b + c)*a**(3) - (b**(2) - b*c + c**(2))*a**(2) - (b + c)*(b**(2) + c**(2))*a + b*c*(b**(2) + b*c + c**(2)))', ID="X_2108", classes=["selected", "target"])
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center", "incident"])
    X_39 = eval_trilinear_point(model, A, B, C, 'a*(b**(2) + c**(2))', ID="X_39", classes=["center", "incident"])
    central_line(model, X_1, X_39, 1, 39, incident=True)
    X_31 = eval_trilinear_point(model, A, B, C, 'a**(2)', ID="X_31", classes=["center", "incident"])
    X_43 = eval_trilinear_point(model, A, B, C, 'a*b + a*c - b*c', ID="X_43", classes=["center", "incident"])
    central_line(model, X_31, X_43, 31, 43, incident=True)
    X_170 = point_from_barycentrics(model, A, B, C, 0.58949925, 0.50336323, -0.092862481, ID="X_170", classes=["center", "incident"])
    X_411 = eval_trilinear_point(model, A, B, C, '(cos(B)*cos(C) - (cos(A) + cos(B) + cos(C))*cos(A))', ID="X_411", classes=["center", "incident"])
    central_line(model, X_170, X_411, 170, 411, incident=True)
    return promote_point_to_top(model, X_2108)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2108 on the given reference triangle."""
    model = create_model('X_2108 = POINT KEPLER I')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02108(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02108.json"))
    write_center_svg(
        model_acute,
        here / "x-02108.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
