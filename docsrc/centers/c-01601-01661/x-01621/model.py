"""GEOMETOR construction model for X_1621 = TCC-PERSPECTOR OF X_81."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    centroid_of,
    construct_baseline_triangle,
    create_model,
    crosspoint,
    eval_trilinear_point,
    feuerbach_point_of,
    incenter_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_01621(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1621 = TCC-PERSPECTOR OF X_81 on reference triangle ABC."""
    X_99 = eval_trilinear_point(model, A, B, C, 'b*c/(b**(2) - c**(2))', ID="X_99", classes=["center"])
    X_765 = eval_trilinear_point(model, A, B, C, '(b - c) **(-2)', ID="X_765", classes=["center"])
    X_1621 = crosspoint(model, A, B, C, X_99, X_765, ID="X_1621", classes=["selected", "target"])
    X_2 = centroid_of(model, A, B, C, ID="X_2", classes=["center", "incident"])
    X_11 = feuerbach_point_of(model, A, B, C, ID="X_11", classes=["center", "incident"])
    central_line(model, X_2, X_11, 2, 11, incident=True)
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center", "incident"])
    X_21 = eval_trilinear_point(model, A, B, C, '1/(cos(B) + cos(C))', ID="X_21", classes=["center", "incident"])
    central_line(model, X_1, X_21, 1, 21, incident=True)
    X_37 = eval_trilinear_point(model, A, B, C, 'b + c', ID="X_37", classes=["center", "incident"])
    X_82 = eval_trilinear_point(model, A, B, C, '1/(b**(2) + c**(2))', ID="X_82", classes=["center", "incident"])
    central_line(model, X_37, X_82, 37, 82, incident=True)
    return promote_point_to_top(model, X_1621)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1621 on the given reference triangle."""
    model = create_model('X_1621 = TCC-PERSPECTOR OF X_81')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01621(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01621.json"))
    write_center_svg(
        model_acute,
        here / "x-01621.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
