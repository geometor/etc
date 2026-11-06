"""GEOMETOR construction model for X_2992 = CD(X_13)."""

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
    intersect_lines,
    promote_point_to_top,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_02992(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2992 = CD(X_13) on reference triangle ABC."""
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center"])
    X_299 = eval_trilinear_point(model, A, B, C, '(csc(A))**(2)*sin(A -  pi  /3)', ID="X_299", classes=["center"])
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center"])
    X_471 = eval_trilinear_point(model, A, B, C, 'sin(A -  pi  /3)*csc(2*A)', ID="X_471", classes=["center"])
    central_line(model, X_3, X_299, 3, 299)
    central_line(model, X_6, X_471, 6, 471)
    X_2992 = intersect_lines(model, X_3, X_299, X_6, X_471, ID="X_2992", classes=["selected", "target"])
    X_265 = eval_trilinear_point(model, A, B, C, 'sin(2*A)*csc(3*A)', ID="X_265", classes=["center", "incident"])
    X_300 = eval_trilinear_point(model, A, B, C, '(csc(A))**(2)*csc(A +  pi  /3)', ID="X_300", classes=["center", "incident"])
    central_line(model, X_265, X_300, 265, 300, incident=True)
    return promote_point_to_top(model, X_2992)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2992 on the given reference triangle."""
    model = create_model('X_2992 = CD(X_13)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02992(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02992.json"))
    write_center_svg(
        model_acute,
        here / "x-02992.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
