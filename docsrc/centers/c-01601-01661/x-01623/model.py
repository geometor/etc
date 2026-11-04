"""GEOMETOR construction model for X_1623 = TCC-PERSPECTOR OF X_88."""

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
    nagel_point_of,
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_01623(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1623 = TCC-PERSPECTOR OF X_88 on reference triangle ABC."""
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center"])
    X_8 = nagel_point_of(model, A, B, C, ID="X_8", classes=["center"])
    X_23 = eval_trilinear_point(model, A, B, C, 'a*(b**(4) + c**(4) - a**(4) - b**(2)*c**(2))', ID="X_23", classes=["center"])
    X_105 = eval_trilinear_point(model, A, B, C, '1/(b**(2) + c**(2) - a*(b + c))', ID="X_105", classes=["center"])
    central_line(model, X_3, X_8, 3, 8)
    central_line(model, X_23, X_105, 23, 105)
    X_1623 = intersect_lines(model, X_3, X_8, X_23, X_105, ID="X_1623", classes=["selected", "target"])
    X_36 = eval_trilinear_point(model, A, B, C, '1 - 2*cos(A)', ID="X_36", classes=["center", "incident"])
    X_1168 = point_from_barycentrics(model, A, B, C, -1.9444441e-07, 0.99999992, 2.7222218e-07, ID="X_1168", classes=["center", "incident"])
    central_line(model, X_36, X_1168, 36, 1168, incident=True)
    return promote_point_to_top(model, X_1623)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1623 on the given reference triangle."""
    model = create_model('X_1623 = TCC-PERSPECTOR OF X_88')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01623(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01623.json"))
    write_center_svg(
        model_acute,
        here / "x-01623.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
