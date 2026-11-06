"""GEOMETOR construction model for X_3345 = ISOGONAL CONJUGATE OF X_1490."""

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
    incenter_of,
    point_from_barycentrics,
    promote_point_to_top,
    reflection_in_point,
)
from geometor.etc.render import write_center_svg


def construct_x_03345(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3345 = ISOGONAL CONJUGATE OF X_1490 on reference triangle ABC."""
    X_3182 = point_from_barycentrics(model, A, B, C, -3.2427213, -5.3672014, 9.6099228, ID="X_3182", classes=["center"])
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center"])
    X_3345 = reflection_in_point(model, X_3182, X_3, ID="X_3345", classes=["selected", "target"], guide=False)
    X_20 = eval_trilinear_point(model, A, B, C, 'cos(A) - cos(B)*cos(C)', ID="X_20", classes=["center", "incident"])
    X_78 = eval_trilinear_point(model, A, B, C, '1/(1 - sec(A))', ID="X_78", classes=["center", "incident"])
    central_line(model, X_20, X_78, 20, 78, incident=True)
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center", "incident"])
    X_196 = eval_trilinear_point(model, A, B, C, '((cos(B) + cos(C) - cos(A) - 1)*sec(A)*tan(A/2))', ID="X_196", classes=["center", "incident"])
    central_line(model, X_1, X_196, 1, 196, incident=True)
    X_223 = eval_trilinear_point(model, A, B, C, '(tan(A/2))*(cos(B) + cos(C) - cos(A) - 1)', ID="X_223", classes=["center", "incident"])
    central_line(model, X_3, X_223, 3, 223, incident=True)
    return promote_point_to_top(model, X_3345)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3345 on the given reference triangle."""
    model = create_model('X_3345 = ISOGONAL CONJUGATE OF X_1490')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03345(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03345.json"))
    write_center_svg(
        model_acute,
        here / "x-03345.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
