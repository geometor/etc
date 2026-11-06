"""GEOMETOR construction model for X_3439 = X_14-VERTEX CONJUGATE OF X_14."""

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
    isogonal_conjugate,
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_03439(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3439 = X_14-VERTEX CONJUGATE OF X_14 on reference triangle ABC."""
    X_622 = point_from_barycentrics(model, A, B, C, 5.69489, 2.0530231, -6.747913, ID="X_622", classes=["center"])
    X_3439 = isogonal_conjugate(model, A, B, C, X_622, ID="X_3439", classes=["selected", "target"])
    X_15 = eval_trilinear_point(model, A, B, C, 'sin(A +  pi  /3)', ID="X_15", classes=["center", "incident"])
    X_184 = eval_trilinear_point(model, A, B, C, 'a**(2)*cos(A)', ID="X_184", classes=["center", "incident"])
    central_line(model, X_15, X_184, 15, 184, incident=True)
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center", "incident"])
    X_298 = eval_trilinear_point(model, A, B, C, '(csc(A))**(2)*sin(A +  pi  /3)', ID="X_298", classes=["center", "incident"])
    central_line(model, X_3, X_298, 3, 298, incident=True)
    X_14 = eval_trilinear_point(model, A, B, C, 'csc(A -  pi  /3)', ID="X_14", classes=["center", "incident"])
    X_1606 = point_from_barycentrics(model, A, B, C, 0.46878519, 1.3979153, -0.86670046, ID="X_1606", classes=["center", "incident"])
    central_line(model, X_14, X_1606, 14, 1606, incident=True)
    return promote_point_to_top(model, X_3439)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3439 on the given reference triangle."""
    model = create_model('X_3439 = X_14-VERTEX CONJUGATE OF X_14')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03439(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03439.json"))
    write_center_svg(
        model_acute,
        here / "x-03439.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
