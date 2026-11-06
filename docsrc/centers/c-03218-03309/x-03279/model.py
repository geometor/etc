"""GEOMETOR construction model for X_3279 = PERSPECTOR OF TRIANGLES M1M2M3 AND N1N2N3."""

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
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_03279(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3279 = PERSPECTOR OF TRIANGLES M1M2M3 AND N1N2N3 on reference triangle ABC."""
    X_3279 = eval_trilinear_point(model, A, B, C, '(cos(B/3)*cos(C/3) + sin(A/3)*sin(2*A/3))', ID="X_3279", classes=["selected", "target"])
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center", "incident"])
    X_356 = eval_trilinear_point(model, A, B, C, 'cos(A/3) + 2*cos(B/3)*cos(C/3)', ID="X_356", classes=["center", "incident"])
    central_line(model, X_3, X_356, 3, 356, incident=True)
    X_358 = eval_trilinear_point(model, A, B, C, 'cos(A/3)', ID="X_358", classes=["center", "incident"])
    X_3281 = eval_trilinear_point(model, A, B, C, '(2*cos(A/3) + cos(A) - 2*cos(B/3)*cos(C/3))', ID="X_3281", classes=["center", "incident"])
    central_line(model, X_358, X_3281, 358, 3281, incident=True)
    X_1135 = eval_trilinear_point(model, A, B, C, 'cos(A/3 + 2*pi  /3)', ID="X_1135", classes=["center", "incident"])
    X_3283 = eval_trilinear_point(model, A, B, C, '(cos(A) - 2*sin(B/3)*sin(C/3) + sin(A/3 -  pi  /6))', ID="X_3283", classes=["center", "incident"])
    central_line(model, X_1135, X_3283, 1135, 3283, incident=True)
    return promote_point_to_top(model, X_3279)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3279 on the given reference triangle."""
    model = create_model('X_3279 = PERSPECTOR OF TRIANGLES M1M2M3 AND N1N2N3')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03279(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03279.json"))
    write_center_svg(
        model_acute,
        here / "x-03279.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
