"""GEOMETOR construction model for X_1452 = X_406-BETH CONJUGATE OF X_406."""

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
    intersect_lines,
    orthocenter_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_01452(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1452 = X_406-BETH CONJUGATE OF X_406 on reference triangle ABC."""
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center"])
    X_24 = eval_trilinear_point(model, A, B, C, 'sec(A)*cos(2*A)', ID="X_24", classes=["center"])
    X_4 = orthocenter_of(model, A, B, C, ID="X_4", classes=["center"])
    X_46 = eval_trilinear_point(model, A, B, C, 'cos(B) + cos(C) - cos(A)', ID="X_46", classes=["center"])
    central_line(model, X_1, X_24, 1, 24)
    central_line(model, X_4, X_46, 4, 46)
    X_1452 = intersect_lines(model, X_1, X_24, X_4, X_46, ID="X_1452", classes=["selected", "target"])
    X_28 = eval_trilinear_point(model, A, B, C, '(tan(A))/(b + c)', ID="X_28", classes=["center", "incident"])
    X_34 = eval_trilinear_point(model, A, B, C, '1 - sec(A)', ID="X_34", classes=["center", "incident"])
    central_line(model, X_28, X_34, 28, 34, incident=True)
    return promote_point_to_top(model, X_1452)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1452 on the given reference triangle."""
    model = create_model('X_1452 = X_406-BETH CONJUGATE OF X_406')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01452(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01452.json"))
    write_center_svg(
        model_acute,
        here / "x-01452.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
