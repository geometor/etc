"""GEOMETOR construction model for X_1633 = TCC-PERSPECTOR OF X_651."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    promote_point_to_top,
    reflection_in_point,
)
from geometor.etc.render import write_center_svg


def construct_x_01633(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1633 = TCC-PERSPECTOR OF X_651 on reference triangle ABC."""
    X_651 = eval_trilinear_point(model, A, B, C, '1/(cos(B) - cos(C))', ID="X_651", classes=["center"])
    X_692 = eval_trilinear_point(model, A, B, C, 'a**(2)/(b - c)', ID="X_692", classes=["center"])
    X_1633 = reflection_in_point(model, X_651, X_692, ID="X_1633", classes=["selected", "target"], guide=False)
    X_108 = eval_trilinear_point(model, A, B, C, 'a/(sec(B) - sec(C))', ID="X_108", classes=["center", "incident"])
    X_109 = eval_trilinear_point(model, A, B, C, 'a/(cos(B) - cos(C))', ID="X_109", classes=["center", "incident"])
    central_line(model, X_108, X_109, 108, 109, incident=True)
    X_100 = eval_trilinear_point(model, A, B, C, '1/(b - c)', ID="X_100", classes=["center", "incident"])
    X_190 = eval_trilinear_point(model, A, B, C, 'b*c/(b - c)', ID="X_190", classes=["center", "incident"])
    central_line(model, X_100, X_190, 100, 190, incident=True)
    X_105 = eval_trilinear_point(model, A, B, C, '1/(b**(2) + c**(2) - a*(b + c))', ID="X_105", classes=["center", "incident"])
    X_1086 = eval_trilinear_point(model, A, B, C, '(b*c*(b - c)**(2))', ID="X_1086", classes=["center", "incident"])
    central_line(model, X_105, X_1086, 105, 1086, incident=True)
    return promote_point_to_top(model, X_1633)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1633 on the given reference triangle."""
    model = create_model('X_1633 = TCC-PERSPECTOR OF X_651')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01633(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01633.json"))
    write_center_svg(
        model_acute,
        here / "x-01633.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
