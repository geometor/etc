"""GEOMETOR construction model for X_1242 = ISOGONAL CONJUGATE OF X_1005."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_barycentric_point,
    eval_trilinear_point,
    isogonal_conjugate,
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_01242(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1242 = ISOGONAL CONJUGATE OF X_1005 on reference triangle ABC."""
    X_1005 = point_from_barycentrics(model, A, B, C, 0.38047896, 0.36259614, 0.2569249, ID="X_1005", classes=["center"])
    X_1242 = isogonal_conjugate(model, A, B, C, X_1005, ID="X_1242", classes=["selected", "target"])
    X_72 = eval_trilinear_point(model, A, B, C, '(b + c)*cot(A)', ID="X_72", classes=["center", "incident"])
    X_527 = eval_barycentric_point(model, A, B, C, '2*a**(2) - a*(b + c) - (b - c)**(2)', ID="X_527", classes=["center", "incident"])
    central_line(model, X_72, X_527, 72, 527, incident=True)
    X_71 = eval_trilinear_point(model, A, B, C, '(b + c)*cos(A)', ID="X_71", classes=["center", "incident"])
    X_1155 = eval_trilinear_point(model, A, B, C, '(cos(B) + cos(C) - 2*cos(A))', ID="X_1155", classes=["center", "incident"])
    central_line(model, X_71, X_1155, 71, 1155, incident=True)
    return promote_point_to_top(model, X_1242)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1242 on the given reference triangle."""
    model = create_model('X_1242 = ISOGONAL CONJUGATE OF X_1005')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01242(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01242.json"))
    write_center_svg(
        model_acute,
        here / "x-01242.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
