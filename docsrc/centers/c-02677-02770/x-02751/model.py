"""GEOMETOR construction model for X_2751 = SR(X_105, X_109)."""

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
    mittenpunkt_of,
    point_from_barycentrics,
    promote_point_to_top,
    reflection_in_point,
)
from geometor.etc.render import write_center_svg


def construct_x_02751(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2751 = SR(X_105, X_109) on reference triangle ABC."""
    X_2730 = point_from_barycentrics(model, A, B, C, -0.041035354, 0.95530303, 0.085732323, ID="X_2730", classes=["center"])
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center"])
    X_2751 = reflection_in_point(model, X_2730, X_3, ID="X_2751", classes=["selected", "target"], guide=False)
    X_105 = eval_trilinear_point(model, A, B, C, '1/(b**(2) + c**(2) - a*(b + c))', ID="X_105", classes=["center", "incident"])
    X_522 = eval_trilinear_point(model, A, B, C, '(cos(B) - cos(C))*(csc(A))', ID="X_522", classes=["center", "incident"])
    central_line(model, X_105, X_522, 105, 522, incident=True)
    X_109 = eval_trilinear_point(model, A, B, C, 'a/(cos(B) - cos(C))', ID="X_109", classes=["center", "incident"])
    X_518 = eval_trilinear_point(model, A, B, C, '(a*b + a*c - b**(2) - c**(2))', ID="X_518", classes=["center", "incident"])
    central_line(model, X_109, X_518, 109, 518, incident=True)
    X_9 = mittenpunkt_of(model, A, B, C, ID="X_9", classes=["center", "incident"])
    X_919 = point_from_barycentrics(model, A, B, C, -0.11560694, 0.83236994, 0.28323699, ID="X_919", classes=["center", "incident"])
    central_line(model, X_9, X_919, 9, 919, incident=True)
    return promote_point_to_top(model, X_2751)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2751 on the given reference triangle."""
    model = create_model('X_2751 = SR(X_105, X_109)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02751(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02751.json"))
    write_center_svg(
        model_acute,
        here / "x-02751.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
