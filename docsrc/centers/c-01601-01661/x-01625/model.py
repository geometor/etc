"""GEOMETOR construction model for X_1625 = TCC-PERSPECTOR OF X_163."""

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
    nine_point_center_of,
    promote_point_to_top,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_01625(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1625 = TCC-PERSPECTOR OF X_163 on reference triangle ABC."""
    X_75 = eval_trilinear_point(model, A, B, C, '1/a**(2)', ID="X_75", classes=["center"])
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center"])
    X_1625 = ceva_conjugate(model, A, B, C, X_75, X_6, ID="X_1625", classes=["selected", "target"])
    X_13 = eval_trilinear_point(model, A, B, C, 'csc(A +  pi  /3)', ID="X_13", classes=["center", "incident"])
    central_line(model, X_6, X_13, 6, 13, incident=True)
    X_5 = nine_point_center_of(model, A, B, C, ID="X_5", classes=["center", "incident"])
    X_217 = eval_trilinear_point(model, A, B, C, '((sin(A))**(3))*cos(A)*cos(B - C)', ID="X_217", classes=["center", "incident"])
    central_line(model, X_5, X_217, 5, 217, incident=True)
    X_110 = eval_trilinear_point(model, A, B, C, 'csc(B - C)', ID="X_110", classes=["center", "incident"])
    X_112 = eval_trilinear_point(model, A, B, C, 'a/(sin(2*B) - sin(2*C))', ID="X_112", classes=["center", "incident"])
    central_line(model, X_110, X_112, 110, 112, incident=True)
    return promote_point_to_top(model, X_1625)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1625 on the given reference triangle."""
    model = create_model('X_1625 = TCC-PERSPECTOR OF X_163')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01625(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01625.json"))
    write_center_svg(
        model_acute,
        here / "x-01625.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
