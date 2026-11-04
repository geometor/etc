"""GEOMETOR construction model for X_2201 = X_2-ISOCONJUGATE OF X_295."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    intersect_lines,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_02201(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2201 = X_2-ISOCONJUGATE OF X_295 on reference triangle ABC."""
    X_19 = eval_trilinear_point(model, A, B, C, 'tan(A)', ID="X_19", classes=["center"])
    X_25 = eval_trilinear_point(model, A, B, C, 'sin(A)*tan(A)', ID="X_25", classes=["center"])
    X_27 = eval_trilinear_point(model, A, B, C, '(sec(A))/(b + c)', ID="X_27", classes=["center"])
    X_86 = eval_trilinear_point(model, A, B, C, 'b*c/(b + c)', ID="X_86", classes=["center"])
    central_line(model, X_19, X_25, 19, 25)
    central_line(model, X_27, X_86, 27, 86)
    X_2201 = intersect_lines(model, X_19, X_25, X_27, X_86, ID="X_2201", classes=["selected", "target"])
    X_48 = eval_trilinear_point(model, A, B, C, 'tan(B) + tan(C)', ID="X_48", classes=["center", "incident"])
    X_497 = eval_trilinear_point(model, A, B, C, '1 - cos(B)*cos(C)', ID="X_497", classes=["center", "incident"])
    central_line(model, X_48, X_497, 48, 497, incident=True)
    return promote_point_to_top(model, X_2201)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2201 on the given reference triangle."""
    model = create_model('X_2201 = X_2-ISOCONJUGATE OF X_295')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02201(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02201.json"))
    write_center_svg(
        model_acute,
        here / "x-02201.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
