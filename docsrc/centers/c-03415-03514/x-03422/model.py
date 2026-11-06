"""GEOMETOR construction model for X_3422 = X_1-VERTEX CONJUGATE OF X_19."""

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
    isogonal_conjugate,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_03422(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3422 = X_1-VERTEX CONJUGATE OF X_19 on reference triangle ABC."""
    X_1478 = eval_trilinear_point(model, A, B, C, '1 + 2*cos(B)*cos(C)', ID="X_1478", classes=["center"])
    X_3422 = isogonal_conjugate(model, A, B, C, X_1478, ID="X_3422", classes=["selected", "target"])
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center", "incident"])
    X_24 = eval_trilinear_point(model, A, B, C, 'sec(A)*cos(2*A)', ID="X_24", classes=["center", "incident"])
    central_line(model, X_1, X_24, 1, 24, incident=True)
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center", "incident"])
    X_47 = eval_trilinear_point(model, A, B, C, 'cos(2*A)', ID="X_47", classes=["center", "incident"])
    central_line(model, X_3, X_47, 3, 47, incident=True)
    X_35 = eval_trilinear_point(model, A, B, C, '1 + 2*cos(A)', ID="X_35", classes=["center", "incident"])
    X_78 = eval_trilinear_point(model, A, B, C, '1/(1 - sec(A))', ID="X_78", classes=["center", "incident"])
    central_line(model, X_35, X_78, 35, 78, incident=True)
    return promote_point_to_top(model, X_3422)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3422 on the given reference triangle."""
    model = create_model('X_3422 = X_1-VERTEX CONJUGATE OF X_19')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03422(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03422.json"))
    write_center_svg(
        model_acute,
        here / "x-03422.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
