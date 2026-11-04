"""GEOMETOR construction model for X_1601 = TCC-PERSPECTOR OF X_5."""

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
    point_from_barycentrics,
    promote_point_to_top,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_01601(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1601 = TCC-PERSPECTOR OF X_5 on reference triangle ABC."""
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center"])
    X_128 = eval_trilinear_point(model, A, B, C, '((sec(A))*(cos(2*B) + cos(2*C))*(1 + 2*cos(2*A))*(cos(2*A) + 2*cos(2*B)*cos(2*C)))', ID="X_128", classes=["center"])
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center"])
    X_1166 = point_from_barycentrics(model, A, B, C, 0.20424736, 0.33803917, 0.45771347, ID="X_1166", classes=["center"])
    central_line(model, X_3, X_128, 3, 128)
    central_line(model, X_6, X_1166, 6, 1166)
    X_1601 = intersect_lines(model, X_3, X_128, X_6, X_1166, ID="X_1601", classes=["selected", "target"])
    return promote_point_to_top(model, X_1601)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1601 on the given reference triangle."""
    model = create_model('X_1601 = TCC-PERSPECTOR OF X_5')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01601(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01601.json"))
    write_center_svg(
        model_acute,
        here / "x-01601.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
