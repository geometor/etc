"""GEOMETOR construction model for X_1424 = X_194-BETH CONJUGATE OF X_194."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    ceva_conjugate,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_01424(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1424 = X_194-BETH CONJUGATE OF X_194 on reference triangle ABC."""
    X_604 = eval_trilinear_point(model, A, B, C, 'a*(1 - cos(A))', ID="X_604", classes=["center"])
    X_57 = eval_trilinear_point(model, A, B, C, '1/(b + c - a)', ID="X_57", classes=["center"])
    X_1424 = ceva_conjugate(model, A, B, C, X_604, X_57, ID="X_1424", classes=["selected", "target"])
    X_85 = eval_trilinear_point(model, A, B, C, 'b**(2)*c**(2)/(b + c - a)', ID="X_85", classes=["center", "incident"])
    central_line(model, X_57, X_85, 57, 85, incident=True)
    X_56 = eval_trilinear_point(model, A, B, C, 'a/(b + c - a)', ID="X_56", classes=["center", "incident"])
    X_87 = eval_trilinear_point(model, A, B, C, '1/(a*b + a*c - b*c)', ID="X_87", classes=["center", "incident"])
    central_line(model, X_56, X_87, 56, 87, incident=True)
    X_222 = eval_trilinear_point(model, A, B, C, 'cos(A)*tan(A/2)', ID="X_222", classes=["center", "incident"])
    X_1429 = point_from_barycentrics(model, A, B, C, -0.44973545, 0.042328042, 1.4074074, ID="X_1429", classes=["center", "incident"])
    central_line(model, X_222, X_1429, 222, 1429, incident=True)
    return promote_point_to_top(model, X_1424)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1424 on the given reference triangle."""
    model = create_model('X_1424 = X_194-BETH CONJUGATE OF X_194')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01424(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01424.json"))
    write_center_svg(
        model_acute,
        here / "x-01424.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
