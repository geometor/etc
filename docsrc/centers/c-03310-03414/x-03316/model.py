"""GEOMETOR construction model for X_3316 = ISOGONAL CONJUGATE OF X_3311."""

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
    orthocenter_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_03316(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3316 = ISOGONAL CONJUGATE OF X_3311 on reference triangle ABC."""
    X_3311 = eval_trilinear_point(model, A, B, C, 'cos(A) + 2*sin(A)', ID="X_3311", classes=["center"])
    X_3316 = isogonal_conjugate(model, A, B, C, X_3311, ID="X_3316", classes=["selected", "target"])
    X_4 = orthocenter_of(model, A, B, C, ID="X_4", classes=["center", "incident"])
    X_590 = eval_trilinear_point(model, A, B, C, '(a**(2) + 4*area )/a', ID="X_590", classes=["center", "incident"])
    central_line(model, X_4, X_590, 4, 590, incident=True)
    X_485 = eval_trilinear_point(model, A, B, C, 'sec(A -  pi  /4)', ID="X_485", classes=["center", "incident"])
    X_631 = eval_trilinear_point(model, A, B, C, '2*cos(A) + cos(B)*cos(C)', ID="X_631", classes=["center", "incident"])
    central_line(model, X_485, X_631, 485, 631, incident=True)
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center", "incident"])
    X_1131 = eval_trilinear_point(model, A, B, C, '1/(sin(A) + 2*cos(A))', ID="X_1131", classes=["center", "incident"])
    central_line(model, X_3, X_1131, 3, 1131, incident=True)
    return promote_point_to_top(model, X_3316)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3316 on the given reference triangle."""
    model = create_model('X_3316 = ISOGONAL CONJUGATE OF X_3311')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03316(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03316.json"))
    write_center_svg(
        model_acute,
        here / "x-03316.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
