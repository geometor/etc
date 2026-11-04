"""GEOMETOR construction model for X_1626 = TCC-PERSPECTOR OF X_174."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    ceva_conjugate,
    circumcenter_of,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    point_from_barycentrics,
    promote_point_to_top,
    spieker_center_of,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_01626(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1626 = TCC-PERSPECTOR OF X_174 on reference triangle ABC."""
    X_85 = eval_trilinear_point(model, A, B, C, 'b**(2)*c**(2)/(b + c - a)', ID="X_85", classes=["center"])
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center"])
    X_1626 = ceva_conjugate(model, A, B, C, X_85, X_6, ID="X_1626", classes=["selected", "target"])
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center", "incident"])
    X_10 = spieker_center_of(model, A, B, C, ID="X_10", classes=["center", "incident"])
    central_line(model, X_3, X_10, 3, 10, incident=True)
    X_38 = eval_trilinear_point(model, A, B, C, 'b**(2) + c**(2)', ID="X_38", classes=["center", "incident"])
    X_55 = eval_trilinear_point(model, A, B, C, 'a*(b + c - a)', ID="X_55", classes=["center", "incident"])
    central_line(model, X_38, X_55, 38, 55, incident=True)
    X_22 = eval_trilinear_point(model, A, B, C, 'a*(b**(4) + c**(4) - a**(4))', ID="X_22", classes=["center", "incident"])
    X_1602 = point_from_barycentrics(model, A, B, C, 0.24316346, 0.2467371, 0.51009944, ID="X_1602", classes=["center", "incident"])
    central_line(model, X_22, X_1602, 22, 1602, incident=True)
    return promote_point_to_top(model, X_1626)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1626 on the given reference triangle."""
    model = create_model('X_1626 = TCC-PERSPECTOR OF X_174')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01626(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01626.json"))
    write_center_svg(
        model_acute,
        here / "x-01626.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
