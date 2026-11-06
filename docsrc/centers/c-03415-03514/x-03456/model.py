"""GEOMETOR construction model for X_3456 = X_17-VERTEX CONJUGATE OF X_18."""

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
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_03456(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3456 = X_17-VERTEX CONJUGATE OF X_18 on reference triangle ABC."""
    X_3456 = eval_barycentric_point(model, A, B, C, 'a**(2)/(a**(4) - b**(4) - c**(4) - b**(2)*c**(2))', ID="X_3456", classes=["selected", "target"])
    X_23 = eval_trilinear_point(model, A, B, C, 'a*(b**(4) + c**(4) - a**(4) - b**(2)*c**(2))', ID="X_23", classes=["center", "incident"])
    X_1799 = eval_trilinear_point(model, A, B, C, 'cot(A)*csc(A +  omega  )', ID="X_1799", classes=["center", "incident"])
    central_line(model, X_23, X_1799, 23, 1799, incident=True)
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center", "incident"])
    X_2916 = point_from_barycentrics(model, A, B, C, 0.54379762, 0.48047556, -0.024273171, ID="X_2916", classes=["center", "incident"])
    central_line(model, X_3, X_2916, 3, 2916, incident=True)
    return promote_point_to_top(model, X_3456)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3456 on the given reference triangle."""
    model = create_model('X_3456 = X_17-VERTEX CONJUGATE OF X_18')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03456(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03456.json"))
    write_center_svg(
        model_acute,
        here / "x-03456.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
