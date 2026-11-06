"""GEOMETOR construction model for X_3170 = X_6-CEVA CONJUGATE OF X_15."""

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
    promote_point_to_top,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_03170(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3170 = X_6-CEVA CONJUGATE OF X_15 on reference triangle ABC."""
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center"])
    X_15 = eval_trilinear_point(model, A, B, C, 'sin(A +  pi  /3)', ID="X_15", classes=["center"])
    X_3170 = ceva_conjugate(model, A, B, C, X_6, X_15, ID="X_3170", classes=["selected", "target"])
    X_16 = eval_trilinear_point(model, A, B, C, 'sin(A-  pi  /3)', ID="X_16", classes=["center", "incident"])
    X_184 = eval_trilinear_point(model, A, B, C, 'a**(2)*cos(A)', ID="X_184", classes=["center", "incident"])
    central_line(model, X_16, X_184, 16, 184, incident=True)
    X_323 = eval_trilinear_point(model, A, B, C, 'sin(3*A)*(csc(A))**(2)', ID="X_323", classes=["center", "incident"])
    central_line(model, X_15, X_323, 15, 323, incident=True)
    X_202 = eval_trilinear_point(model, A, B, C, '1 - cos(A +  pi  /3)', ID="X_202", classes=["center", "incident"])
    X_2308 = eval_trilinear_point(model, A, B, C, '1 - cos(2*A) + (1 + cos(A))*(cos(B) + cos(C))', ID="X_2308", classes=["center", "incident"])
    central_line(model, X_202, X_2308, 202, 2308, incident=True)
    return promote_point_to_top(model, X_3170)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3170 on the given reference triangle."""
    model = create_model('X_3170 = X_6-CEVA CONJUGATE OF X_15')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03170(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03170.json"))
    write_center_svg(
        model_acute,
        here / "x-03170.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
