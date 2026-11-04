"""GEOMETOR construction model for X_2291 = X_2-ISOCONJUGATE OF X_1155."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_barycentric_point,
    eval_trilinear_point,
    isogonal_conjugate,
    mittenpunkt_of,
    promote_point_to_top,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_02291(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2291 = X_2-ISOCONJUGATE OF X_1155 on reference triangle ABC."""
    X_527 = eval_barycentric_point(model, A, B, C, '2*a**(2) - a*(b + c) - (b - c)**(2)', ID="X_527", classes=["center"])
    X_2291 = isogonal_conjugate(model, A, B, C, X_527, ID="X_2291", classes=["selected", "target"])
    X_9 = mittenpunkt_of(model, A, B, C, ID="X_9", classes=["center", "incident"])
    X_100 = eval_trilinear_point(model, A, B, C, '1/(b - c)', ID="X_100", classes=["center", "incident"])
    central_line(model, X_9, X_100, 9, 100, incident=True)
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center", "incident"])
    X_109 = eval_trilinear_point(model, A, B, C, 'a/(cos(B) - cos(C))', ID="X_109", classes=["center", "incident"])
    central_line(model, X_6, X_109, 6, 109, incident=True)
    X_19 = eval_trilinear_point(model, A, B, C, 'tan(A)', ID="X_19", classes=["center", "incident"])
    X_108 = eval_trilinear_point(model, A, B, C, 'a/(sec(B) - sec(C))', ID="X_108", classes=["center", "incident"])
    central_line(model, X_19, X_108, 19, 108, incident=True)
    return promote_point_to_top(model, X_2291)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2291 on the given reference triangle."""
    model = create_model('X_2291 = X_2-ISOCONJUGATE OF X_1155')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02291(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02291.json"))
    write_center_svg(
        model_acute,
        here / "x-02291.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
