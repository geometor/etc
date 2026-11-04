"""GEOMETOR construction model for X_1035 = ISOGONAL CONJUGATE OF X_1034."""

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
    isogonal_conjugate,
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_01035(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1035 = ISOGONAL CONJUGATE OF X_1034 on reference triangle ABC."""
    X_1034 = point_from_barycentrics(model, A, B, C, 0.88413654, 0.82789709, -0.71203363, ID="X_1034", classes=["center"])
    X_1035 = isogonal_conjugate(model, A, B, C, X_1034, ID="X_1035", classes=["selected", "target"])
    X_25 = eval_trilinear_point(model, A, B, C, 'sin(A)*tan(A)', ID="X_25", classes=["center", "incident"])
    X_34 = eval_trilinear_point(model, A, B, C, '1 - sec(A)', ID="X_34", classes=["center", "incident"])
    central_line(model, X_25, X_34, 25, 34, incident=True)
    X_55 = eval_trilinear_point(model, A, B, C, 'a*(b + c - a)', ID="X_55", classes=["center", "incident"])
    X_64 = eval_trilinear_point(model, A, B, C, '1/(cos(A) - cos(B)*cos(C))', ID="X_64", classes=["center", "incident"])
    central_line(model, X_55, X_64, 55, 64, incident=True)
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center", "incident"])
    X_223 = eval_trilinear_point(model, A, B, C, '(tan(A/2))*(cos(B) + cos(C) - cos(A) - 1)', ID="X_223", classes=["center", "incident"])
    central_line(model, X_3, X_223, 3, 223, incident=True)
    return promote_point_to_top(model, X_1035)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1035 on the given reference triangle."""
    model = create_model('X_1035 = ISOGONAL CONJUGATE OF X_1034')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01035(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01035.json"))
    write_center_svg(
        model_acute,
        here / "x-01035.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
