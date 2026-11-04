"""GEOMETOR construction model for X_2423 = ISOGONAL CONJUGATE OF X_2397."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    isogonal_conjugate,
    point_from_barycentrics,
    promote_point_to_top,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_02423(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2423 = ISOGONAL CONJUGATE OF X_2397 on reference triangle ABC."""
    X_2397 = point_from_barycentrics(model, A, B, C, -6, 1, 6, ID="X_2397", classes=["center"])
    X_2423 = isogonal_conjugate(model, A, B, C, X_2397, ID="X_2423", classes=["selected", "target"])
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center", "incident"])
    X_650 = eval_trilinear_point(model, A, B, C, 'cos(B) - cos(C)', ID="X_650", classes=["center", "incident"])
    central_line(model, X_6, X_650, 6, 650, incident=True)
    X_31 = eval_trilinear_point(model, A, B, C, 'a**(2)', ID="X_31", classes=["center", "incident"])
    X_663 = eval_trilinear_point(model, A, B, C, 'a*(b - c)*(b + c - a)', ID="X_663", classes=["center", "incident"])
    central_line(model, X_31, X_663, 31, 663, incident=True)
    X_104 = eval_trilinear_point(model, A, B, C, '1/(-1 + cos(B) + cos(C))', ID="X_104", classes=["center", "incident"])
    X_739 = eval_trilinear_point(model, A, B, C, '1/(a**(-2)*(b**(0) + c**(0)) - a **(-1)*(b **(-1) + c **(-1)))', ID="X_739", classes=["center", "incident"])
    central_line(model, X_104, X_739, 104, 739, incident=True)
    return promote_point_to_top(model, X_2423)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2423 on the given reference triangle."""
    model = create_model('X_2423 = ISOGONAL CONJUGATE OF X_2397')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02423(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02423.json"))
    write_center_svg(
        model_acute,
        here / "x-02423.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
