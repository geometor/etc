"""GEOMETOR construction model for X_2296 = X_2-ISOCONJUGATE OF X_1185."""

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


def construct_x_02296(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2296 = X_2-ISOCONJUGATE OF X_1185 on reference triangle ABC."""
    X_31 = eval_trilinear_point(model, A, B, C, 'a**(2)', ID="X_31", classes=["center"])
    X_86 = eval_trilinear_point(model, A, B, C, 'b*c/(b + c)', ID="X_86", classes=["center"])
    X_42 = eval_trilinear_point(model, A, B, C, 'a*(b + c)', ID="X_42", classes=["center"])
    X_75 = eval_trilinear_point(model, A, B, C, '1/a**(2)', ID="X_75", classes=["center"])
    central_line(model, X_31, X_86, 31, 86)
    central_line(model, X_42, X_75, 42, 75)
    X_2296 = intersect_lines(model, X_31, X_86, X_42, X_75, ID="X_2296", classes=["selected", "target"])
    X_2 = centroid_of(model, A, B, C, ID="X_2", classes=["center", "incident"])
    X_213 = eval_trilinear_point(model, A, B, C, '(b + c)*a**(2)', ID="X_213", classes=["center", "incident"])
    central_line(model, X_2, X_213, 2, 213, incident=True)
    return promote_point_to_top(model, X_2296)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2296 on the given reference triangle."""
    model = create_model('X_2296 = X_2-ISOCONJUGATE OF X_1185')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02296(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02296.json"))
    write_center_svg(
        model_acute,
        here / "x-02296.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
