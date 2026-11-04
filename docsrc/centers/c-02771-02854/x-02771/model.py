"""GEOMETOR construction model for X_2771 = ISOGONAL CONJUGATE OF X_2687."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    feuerbach_point_of,
    isogonal_conjugate,
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_02771(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2771 = ISOGONAL CONJUGATE OF X_2687 on reference triangle ABC."""
    X_2687 = point_from_barycentrics(model, A, B, C, 0.96482975, -0.079301075, 0.11447133, ID="X_2687", classes=["center"])
    X_2771 = isogonal_conjugate(model, A, B, C, X_2687, ID="X_2771", classes=["selected", "target"])
    X_11 = feuerbach_point_of(model, A, B, C, ID="X_11", classes=["center", "incident"])
    X_113 = eval_trilinear_point(model, A, B, C, 'sin(B)*sin(C)*((sin(C))/(cos(C) - 2*cos(A)*cos(B)) + (sin(B))/(cos(B) - 2*cos(A)*cos(C)))', ID="X_113", classes=["center", "incident"])
    central_line(model, X_11, X_113, 11, 113, incident=True)
    X_21 = eval_trilinear_point(model, A, B, C, '1/(cos(B) + cos(C))', ID="X_21", classes=["center", "incident"])
    X_104 = eval_trilinear_point(model, A, B, C, '1/(-1 + cos(B) + cos(C))', ID="X_104", classes=["center", "incident"])
    central_line(model, X_21, X_104, 21, 104, incident=True)
    X_65 = eval_trilinear_point(model, A, B, C, 'cos(B) + cos(C)', ID="X_65", classes=["center", "incident"])
    X_79 = eval_trilinear_point(model, A, B, C, '1/(1 + 2*cos(A))', ID="X_79", classes=["center", "incident"])
    central_line(model, X_65, X_79, 65, 79, incident=True)
    return promote_point_to_top(model, X_2771)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2771 on the given reference triangle."""
    model = create_model('X_2771 = ISOGONAL CONJUGATE OF X_2687')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02771(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02771.json"))
    write_center_svg(
        model_acute,
        here / "x-02771.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
