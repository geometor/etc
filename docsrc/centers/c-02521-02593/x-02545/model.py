"""GEOMETOR construction model for X_2545 = EXSIMILICENTER(GALLATLY CIRCLE, (X_4,2R))."""

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
    orthocenter_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_02545(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2545 = EXSIMILICENTER(GALLATLY CIRCLE, (X_4,2R)) on reference triangle ABC."""
    X_2545 = eval_trilinear_point(model, A, B, C, '(cos(B)*cos(C) - sin(A +  omega  ))', ID="X_2545", classes=["selected", "target"])
    X_4 = orthocenter_of(model, A, B, C, ID="X_4", classes=["center", "incident"])
    X_39 = eval_trilinear_point(model, A, B, C, 'a*(b**(2) + c**(2))', ID="X_39", classes=["center", "incident"])
    central_line(model, X_4, X_39, 4, 39, incident=True)
    X_2 = centroid_of(model, A, B, C, ID="X_2", classes=["center", "incident"])
    X_1690 = eval_trilinear_point(model, A, B, C, 'cos(A +  omega  /2 -  pi  /4)', ID="X_1690", classes=["center", "incident"])
    central_line(model, X_2, X_1690, 2, 1690, incident=True)
    X_20 = eval_trilinear_point(model, A, B, C, 'cos(A) - cos(B)*cos(C)', ID="X_20", classes=["center", "incident"])
    X_1689 = eval_trilinear_point(model, A, B, C, 'cos(A +  omega  /2 +  pi  /4)', ID="X_1689", classes=["center", "incident"])
    central_line(model, X_20, X_1689, 20, 1689, incident=True)
    return promote_point_to_top(model, X_2545)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2545 on the given reference triangle."""
    model = create_model('X_2545 = EXSIMILICENTER(GALLATLY CIRCLE, (X_4,2R))')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02545(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02545.json"))
    write_center_svg(
        model_acute,
        here / "x-02545.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
