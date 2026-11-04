"""GEOMETOR construction model for X_2762 = SR(X_107, X_109)."""

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
    point_from_barycentrics,
    promote_point_to_top,
    reflection_in_point,
)
from geometor.etc.render import write_center_svg


def construct_x_02762(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2762 = SR(X_107, X_109) on reference triangle ABC."""
    X_2732 = point_from_barycentrics(model, A, B, C, 0.91816265, 0.7113824, -0.62954505, ID="X_2732", classes=["center"])
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center"])
    X_2762 = reflection_in_point(model, X_2732, X_3, ID="X_2762", classes=["selected", "target"], guide=False)
    X_107 = eval_trilinear_point(model, A, B, C, '1/(cos(A)*(sin(2*B) - sin(2*C)))', ID="X_107", classes=["center", "incident"])
    X_522 = eval_trilinear_point(model, A, B, C, '(cos(B) - cos(C))*(csc(A))', ID="X_522", classes=["center", "incident"])
    central_line(model, X_107, X_522, 107, 522, incident=True)
    X_109 = eval_trilinear_point(model, A, B, C, 'a/(cos(B) - cos(C))', ID="X_109", classes=["center", "incident"])
    X_520 = eval_trilinear_point(model, A, B, C, '(cos(A))*(sin(2*B) - sin(2*C))', ID="X_520", classes=["center", "incident"])
    central_line(model, X_109, X_520, 109, 520, incident=True)
    X_108 = eval_trilinear_point(model, A, B, C, 'a/(sec(B) - sec(C))', ID="X_108", classes=["center", "incident"])
    X_656 = eval_trilinear_point(model, A, B, C, 'tan(B) - tan(C)', ID="X_656", classes=["center", "incident"])
    central_line(model, X_108, X_656, 108, 656, incident=True)
    return promote_point_to_top(model, X_2762)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2762 on the given reference triangle."""
    model = create_model('X_2762 = SR(X_107, X_109)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02762(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02762.json"))
    write_center_svg(
        model_acute,
        here / "x-02762.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
