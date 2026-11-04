"""GEOMETOR construction model for X_2946 = EXCENTRAL-ISOGONAL CONJUGATE OF X_16."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    intersect_lines,
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_02946(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2946 = EXCENTRAL-ISOGONAL CONJUGATE OF X_16 on reference triangle ABC."""
    X_15 = eval_trilinear_point(model, A, B, C, 'sin(A +  pi  /3)', ID="X_15", classes=["center"])
    X_846 = eval_trilinear_point(model, A, B, C, '(- a**(2) + b**(2) + c**(2) + b*c + c*a + a*b)', ID="X_846", classes=["center"])
    X_62 = eval_trilinear_point(model, A, B, C, 'sin(A -  pi  /6)', ID="X_62", classes=["center"])
    X_1046 = point_from_barycentrics(model, A, B, C, 0.13236391, 0.3064877, 0.5611484, ID="X_1046", classes=["center"])
    central_line(model, X_15, X_846, 15, 846)
    central_line(model, X_62, X_1046, 62, 1046)
    X_2946 = intersect_lines(model, X_15, X_846, X_62, X_1046, ID="X_2946", classes=["selected", "target"])
    X_573 = eval_trilinear_point(model, A, B, C, 'cos(A + U)', ID="X_573", classes=["center", "incident"])
    X_1761 = point_from_barycentrics(model, A, B, C, 0.54015296, 0.3957935, 0.064053537, ID="X_1761", classes=["center", "incident"])
    central_line(model, X_573, X_1761, 573, 1761, incident=True)
    return promote_point_to_top(model, X_2946)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2946 on the given reference triangle."""
    model = create_model('X_2946 = EXCENTRAL-ISOGONAL CONJUGATE OF X_16')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02946(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02946.json"))
    write_center_svg(
        model_acute,
        here / "x-02946.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
