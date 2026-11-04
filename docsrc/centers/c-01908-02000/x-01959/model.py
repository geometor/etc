"""GEOMETOR construction model for X_1959 = CROSSDIFFERENCE OF PU(23)."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    centroid_of,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    incenter_of,
    isogonal_conjugate,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_01959(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1959 = CROSSDIFFERENCE OF PU(23) on reference triangle ABC."""
    X_1910 = eval_trilinear_point(model, A, B, C, '(a/(a**(2)*cos(B)*cos(C) - b*c*(cos(A))**(2)))', ID="X_1910", classes=["center"])
    X_1959 = isogonal_conjugate(model, A, B, C, X_1910, ID="X_1959", classes=["selected", "target"])
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center", "incident"])
    X_21 = eval_trilinear_point(model, A, B, C, '1/(cos(B) + cos(C))', ID="X_21", classes=["center", "incident"])
    central_line(model, X_1, X_21, 1, 21, incident=True)
    X_2 = centroid_of(model, A, B, C, ID="X_2", classes=["center", "incident"])
    X_257 = eval_trilinear_point(model, A, B, C, '1/(a**(3) + a*b*c)', ID="X_257", classes=["center", "incident"])
    central_line(model, X_2, X_257, 2, 257, incident=True)
    X_19 = eval_trilinear_point(model, A, B, C, 'tan(A)', ID="X_19", classes=["center", "incident"])
    X_326 = eval_trilinear_point(model, A, B, C, '(cot(A))**(2)', ID="X_326", classes=["center", "incident"])
    central_line(model, X_19, X_326, 19, 326, incident=True)
    return promote_point_to_top(model, X_1959)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1959 on the given reference triangle."""
    model = create_model('X_1959 = CROSSDIFFERENCE OF PU(23)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01959(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01959.json"))
    write_center_svg(
        model_acute,
        here / "x-01959.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
