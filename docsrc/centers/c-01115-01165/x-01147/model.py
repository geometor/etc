"""GEOMETOR construction model for X_1147 = ISOGONAL CONJUGATE OF X_847."""

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
    midpoint,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_01147(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1147 = ISOGONAL CONJUGATE OF X_847 on reference triangle ABC."""
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center"])
    X_155 = eval_trilinear_point(model, A, B, C, '(cos(A))*((cos(B))**(2) + (cos(C))**(2) - (cos(A))**(2))', ID="X_155", classes=["center"])
    X_1147 = midpoint(model, X_3, X_155, ID="X_1147", classes=["selected", "target"], guide=False)
    X_49 = eval_trilinear_point(model, A, B, C, 'cos(3*A)', ID="X_49", classes=["center", "incident"])
    central_line(model, X_3, X_49, 3, 49, incident=True)
    X_2 = centroid_of(model, A, B, C, ID="X_2", classes=["center", "incident"])
    X_54 = eval_trilinear_point(model, A, B, C, 'sec(B - C)', ID="X_54", classes=["center", "incident"])
    central_line(model, X_2, X_54, 2, 54, incident=True)
    X_24 = eval_trilinear_point(model, A, B, C, 'sec(A)*cos(2*A)', ID="X_24", classes=["center", "incident"])
    X_52 = eval_trilinear_point(model, A, B, C, 'cos(2*A)*cos(B - C)', ID="X_52", classes=["center", "incident"])
    central_line(model, X_24, X_52, 24, 52, incident=True)
    return promote_point_to_top(model, X_1147)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1147 on the given reference triangle."""
    model = create_model('X_1147 = ISOGONAL CONJUGATE OF X_847')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01147(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01147.json"))
    write_center_svg(
        model_acute,
        here / "x-01147.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
