"""GEOMETOR construction model for X_3149 = X_285-CEVA CONJUGATE OF X_1."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    centroid_of,
    ceva_conjugate,
    circumcenter_of,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    incenter_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_03149(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3149 = X_285-CEVA CONJUGATE OF X_1 on reference triangle ABC."""
    X_285 = eval_trilinear_point(model, A, B, C, '(1/((cos(B) + cos(C))*(-1 - cos(A) + cos(B) + cos(C))))', ID="X_285", classes=["center"])
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center"])
    X_3149 = ceva_conjugate(model, A, B, C, X_285, X_1, ID="X_3149", classes=["selected", "target"])
    X_2 = centroid_of(model, A, B, C, ID="X_2", classes=["center"])
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center"])
    central_line(model, X_2, X_3, 2, 3)
    X_227 = eval_trilinear_point(model, A, B, C, '((b + c)*(cos(B) + cos(C) - cos(A) - 1)*tan(A/2))', ID="X_227", classes=["center", "incident"])
    central_line(model, X_1, X_227, 1, 227, incident=True)
    X_56 = eval_trilinear_point(model, A, B, C, 'a/(b + c - a)', ID="X_56", classes=["center", "incident"])
    X_515 = eval_trilinear_point(model, A, B, C, '(b + c)*sec(A) - b*sec(B) - c*sec(C)', ID="X_515", classes=["center", "incident"])
    central_line(model, X_56, X_515, 56, 515, incident=True)
    return promote_point_to_top(model, X_3149)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3149 on the given reference triangle."""
    model = create_model('X_3149 = X_285-CEVA CONJUGATE OF X_1')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03149(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03149.json"))
    write_center_svg(
        model_acute,
        here / "x-03149.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
