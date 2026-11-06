"""GEOMETOR construction model for X_3468 = X_5-CEVA CONJUGATE OF X_3336."""

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
    orthocenter_of,
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_03468(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3468 = X_5-CEVA CONJUGATE OF X_3336 on reference triangle ABC."""
    X_3468 = eval_trilinear_point(model, A, B, C, '2 - sec(A) + sec(B) + sec(C)', ID="X_3468", classes=["selected", "target"])
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center", "incident"])
    X_4 = orthocenter_of(model, A, B, C, ID="X_4", classes=["center", "incident"])
    central_line(model, X_1, X_4, 1, 4, incident=True)
    X_36 = eval_trilinear_point(model, A, B, C, '1 - 2*cos(A)', ID="X_36", classes=["center", "incident"])
    X_1410 = point_from_barycentrics(model, A, B, C, 0.21489592, 0.38593986, 0.39916422, ID="X_1410", classes=["center", "incident"])
    central_line(model, X_36, X_1410, 36, 1410, incident=True)
    X_62 = eval_trilinear_point(model, A, B, C, 'sin(A -  pi  /6)', ID="X_62", classes=["center", "incident"])
    X_1652 = eval_trilinear_point(model, A, B, C, '(sqrt(3/4) - sin(A +  pi  /3) + sin(B +  pi  /3) + sin(C +  pi  /3))', ID="X_1652", classes=["center", "incident"])
    central_line(model, X_62, X_1652, 62, 1652, incident=True)
    return promote_point_to_top(model, X_3468)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3468 on the given reference triangle."""
    model = create_model('X_3468 = X_5-CEVA CONJUGATE OF X_3336')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03468(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03468.json"))
    write_center_svg(
        model_acute,
        here / "x-03468.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
