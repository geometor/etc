"""GEOMETOR construction model for X_2302 = X_2-ISOCONJUGATE OF X_1243."""

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
    intersect_lines,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_02302(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2302 = X_2-ISOCONJUGATE OF X_1243 on reference triangle ABC."""
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center"])
    X_19 = eval_trilinear_point(model, A, B, C, 'tan(A)', ID="X_19", classes=["center"])
    X_54 = eval_trilinear_point(model, A, B, C, 'sec(B - C)', ID="X_54", classes=["center"])
    X_71 = eval_trilinear_point(model, A, B, C, '(b + c)*cos(A)', ID="X_71", classes=["center"])
    central_line(model, X_1, X_19, 1, 19)
    central_line(model, X_54, X_71, 54, 71)
    X_2302 = intersect_lines(model, X_1, X_19, X_54, X_71, ID="X_2302", classes=["selected", "target"])
    X_55 = eval_trilinear_point(model, A, B, C, 'a*(b + c - a)', ID="X_55", classes=["center", "incident"])
    X_184 = eval_trilinear_point(model, A, B, C, 'a**(2)*cos(A)', ID="X_184", classes=["center", "incident"])
    central_line(model, X_55, X_184, 55, 184, incident=True)
    return promote_point_to_top(model, X_2302)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2302 on the given reference triangle."""
    model = create_model('X_2302 = X_2-ISOCONJUGATE OF X_1243')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02302(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02302.json"))
    write_center_svg(
        model_acute,
        here / "x-02302.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
