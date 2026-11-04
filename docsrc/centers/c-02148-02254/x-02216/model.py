"""GEOMETOR construction model for X_2216 = X_2-ISOCONJUGATE OF X_570."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    cevapoint,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_02216(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2216 = X_2-ISOCONJUGATE OF X_570 on reference triangle ABC."""
    X_31 = eval_trilinear_point(model, A, B, C, 'a**(2)', ID="X_31", classes=["center"])
    X_1953 = eval_trilinear_point(model, A, B, C, 'sin(2*B) + sin(2*C)', ID="X_1953", classes=["center"])
    X_2216 = cevapoint(model, A, B, C, X_31, X_1953, ID="X_2216", classes=["selected", "target"])
    X_91 = eval_trilinear_point(model, A, B, C, 'sec(2*A)', ID="X_91", classes=["center", "incident"])
    central_line(model, X_31, X_91, 31, 91, incident=True)
    X_47 = eval_trilinear_point(model, A, B, C, 'cos(2*A)', ID="X_47", classes=["center", "incident"])
    X_75 = eval_trilinear_point(model, A, B, C, '1/a**(2)', ID="X_75", classes=["center", "incident"])
    central_line(model, X_47, X_75, 47, 75, incident=True)
    X_225 = eval_trilinear_point(model, A, B, C, '(sec(A))*(cos(B) + cos(C))', ID="X_225", classes=["center", "incident"])
    X_1179 = point_from_barycentrics(model, A, B, C, 0.088343284, 0.17113976, 0.74051696, ID="X_1179", classes=["center", "incident"])
    central_line(model, X_225, X_1179, 225, 1179, incident=True)
    return promote_point_to_top(model, X_2216)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2216 on the given reference triangle."""
    model = create_model('X_2216 = X_2-ISOCONJUGATE OF X_570')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02216(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02216.json"))
    write_center_svg(
        model_acute,
        here / "x-02216.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
