"""GEOMETOR construction model for X(418) = X(3)-CEVA-CONJUGATE OF X(216)."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    centroid_of,
    circumcenter_of,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00418(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(418) = X(3)-CEVA-CONJUGATE OF X(216) on reference triangle ABC."""
    X_418 = eval_trilinear_point(model, A, B, C, '(cos(A))*(csc(2*B) + csc(2*C))', ID="X(418)", classes=["selected", "target"])
    X_2 = centroid_of(model, A, B, C, ID="X(2)", classes=["center"])
    X_3 = circumcenter_of(model, A, B, C, ID="X(3)", classes=["center"])
    central_line(model, X_2, X_3, 2, 3)
    X_97 = eval_trilinear_point(model, A, B, C, 'cot(A)*sec(B - C)', ID="X(97)", classes=["center", "incident"])
    X_110 = eval_trilinear_point(model, A, B, C, 'csc(B - C)', ID="X(110)", classes=["center", "incident"])
    central_line(model, X_97, X_110, 97, 110, incident=True)
    X_51 = eval_trilinear_point(model, A, B, C, 'a**(2)*cos(B - C)', ID="X(51)", classes=["center", "incident"])
    X_216 = eval_trilinear_point(model, A, B, C, 'sin(2*A)*cos(B - C)', ID="X(216)", classes=["center", "incident"])
    central_line(model, X_51, X_216, 51, 216, incident=True)
    return promote_point_to_top(model, X_418)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(418) on the given reference triangle."""
    model = create_model('X(418) = X(3)-CEVA-CONJUGATE OF X(216)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00418(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00418.json"))
    write_center_svg(
        model_acute,
        here / "x-00418.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
