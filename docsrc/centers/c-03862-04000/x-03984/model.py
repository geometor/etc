"""GEOMETOR construction model for X_3984 = X_3304com[INVERSE(n(TANGENTIAL TRIANGLE))]."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    circumcenter_of,
    construct_baseline_triangle,
    create_model,
    eval_barycentric_point,
    eval_trilinear_point,
    incenter_of,
    intersect_lines,
    nagel_point_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_03984(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3984 = X_3304com[INVERSE(n(TANGENTIAL TRIANGLE))] on reference triangle ABC."""
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center"])
    X_63 = eval_trilinear_point(model, A, B, C, 'cot(A)', ID="X_63", classes=["center"])
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center"])
    X_748 = eval_trilinear_point(model, A, B, C, 'a**(2) - 2*b*c', ID="X_748", classes=["center"])
    central_line(model, X_3, X_63, 3, 63)
    central_line(model, X_1, X_748, 1, 748)
    X_3984 = intersect_lines(model, X_3, X_63, X_1, X_748, ID="X_3984", classes=["selected", "target"])
    X_8 = nagel_point_of(model, A, B, C, ID="X_8", classes=["center", "incident"])
    X_908 = eval_barycentric_point(model, A, B, C, 'cos(B) + cos(C) - 1', ID="X_908", classes=["center", "incident"])
    central_line(model, X_8, X_908, 8, 908, incident=True)
    return promote_point_to_top(model, X_3984)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3984 on the given reference triangle."""
    model = create_model('X_3984 = X_3304com[INVERSE(n(TANGENTIAL TRIANGLE))]')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03984(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03984.json"))
    write_center_svg(
        model_acute,
        here / "x-03984.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
