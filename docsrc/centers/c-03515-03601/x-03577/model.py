"""GEOMETOR construction model for X_3577 = ISOGONAL CONJUGATE OF X_3576."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    incenter_of,
    isogonal_conjugate,
    mittenpunkt_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_03577(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3577 = ISOGONAL CONJUGATE OF X_3576 on reference triangle ABC."""
    X_3576 = eval_trilinear_point(model, A, B, C, '(3*a - b - c)*(a - b + c)*(a + b - c) - 4*a*b*c', ID="X_3576", classes=["center"])
    X_3577 = isogonal_conjugate(model, A, B, C, X_3576, ID="X_3577", classes=["selected", "target"])
    X_21 = eval_trilinear_point(model, A, B, C, '1/(cos(B) + cos(C))', ID="X_21", classes=["center", "incident"])
    X_40 = eval_trilinear_point(model, A, B, C, 'cos(B) + cos(C) - cos(A) - 1', ID="X_40", classes=["center", "incident"])
    central_line(model, X_21, X_40, 21, 40, incident=True)
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center", "incident"])
    X_227 = eval_trilinear_point(model, A, B, C, '((b + c)*(cos(B) + cos(C) - cos(A) - 1)*tan(A/2))', ID="X_227", classes=["center", "incident"])
    central_line(model, X_1, X_227, 1, 227, incident=True)
    X_9 = mittenpunkt_of(model, A, B, C, ID="X_9", classes=["center", "incident"])
    X_374 = eval_trilinear_point(model, A, B, C, '(2*b + 2*c - 3*a + (c + a)*cos(C) + (b + a)*cos(B))', ID="X_374", classes=["center", "incident"])
    central_line(model, X_9, X_374, 9, 374, incident=True)
    return promote_point_to_top(model, X_3577)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3577 on the given reference triangle."""
    model = create_model('X_3577 = ISOGONAL CONJUGATE OF X_3576')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03577(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03577.json"))
    write_center_svg(
        model_acute,
        here / "x-03577.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
