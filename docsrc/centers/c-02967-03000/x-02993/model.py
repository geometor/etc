"""GEOMETOR construction model for X_2993 = CD(X_14)."""

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
    isotomic_conjugate,
    point_from_barycentrics,
    promote_point_to_top,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_02993(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2993 = CD(X_14) on reference triangle ABC."""
    X_622 = point_from_barycentrics(model, A, B, C, 5.69489, 2.0530231, -6.747913, ID="X_622", classes=["center"])
    X_2993 = isotomic_conjugate(model, A, B, C, X_622, ID="X_2993", classes=["selected", "target"])
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center", "incident"])
    X_298 = eval_trilinear_point(model, A, B, C, '(csc(A))**(2)*sin(A +  pi  /3)', ID="X_298", classes=["center", "incident"])
    central_line(model, X_3, X_298, 3, 298, incident=True)
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center", "incident"])
    X_470 = eval_trilinear_point(model, A, B, C, 'sin(A +  pi  /3)*csc(2*A)', ID="X_470", classes=["center", "incident"])
    central_line(model, X_6, X_470, 6, 470, incident=True)
    X_265 = eval_trilinear_point(model, A, B, C, 'sin(2*A)*csc(3*A)', ID="X_265", classes=["center", "incident"])
    X_301 = eval_trilinear_point(model, A, B, C, '(csc(A))**(2)*csc(A -  pi  /3)', ID="X_301", classes=["center", "incident"])
    central_line(model, X_265, X_301, 265, 301, incident=True)
    return promote_point_to_top(model, X_2993)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2993 on the given reference triangle."""
    model = create_model('X_2993 = CD(X_14)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02993(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02993.json"))
    write_center_svg(
        model_acute,
        here / "x-02993.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
