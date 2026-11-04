"""GEOMETOR construction model for X_2229 = X_2-ISOCONJUGATE OF X_715."""

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
    intersect_lines,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_02229(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2229 = X_2-ISOCONJUGATE OF X_715 on reference triangle ABC."""
    X_2 = centroid_of(model, A, B, C, ID="X_2", classes=["center"])
    X_39 = eval_trilinear_point(model, A, B, C, 'a*(b**(2) + c**(2))', ID="X_39", classes=["center"])
    X_44 = eval_trilinear_point(model, A, B, C, 'b + c - 2*a', ID="X_44", classes=["center"])
    X_513 = eval_trilinear_point(model, A, B, C, 'b - c', ID="X_513", classes=["center"])
    central_line(model, X_2, X_39, 2, 39)
    central_line(model, X_44, X_513, 44, 513)
    X_2229 = intersect_lines(model, X_2, X_39, X_44, X_513, ID="X_2229", classes=["selected", "target"])
    X_42 = eval_trilinear_point(model, A, B, C, 'a*(b + c)', ID="X_42", classes=["center", "incident"])
    X_2295 = eval_trilinear_point(model, A, B, C, '(a**(2) + b*c)*(b + c)', ID="X_2295", classes=["center", "incident"])
    central_line(model, X_42, X_2295, 42, 2295, incident=True)
    return promote_point_to_top(model, X_2229)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2229 on the given reference triangle."""
    model = create_model('X_2229 = X_2-ISOCONJUGATE OF X_715')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02229(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02229.json"))
    write_center_svg(
        model_acute,
        here / "x-02229.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
