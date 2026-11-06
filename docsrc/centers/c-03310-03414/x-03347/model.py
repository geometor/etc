"""GEOMETOR construction model for X_3347 = ISOGONAL CONJUGATE OF X_3182."""

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
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_03347(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3347 = ISOGONAL CONJUGATE OF X_3182 on reference triangle ABC."""
    X_40 = eval_trilinear_point(model, A, B, C, 'cos(B) + cos(C) - cos(A) - 1', ID="X_40", classes=["center"])
    X_1712 = point_from_barycentrics(model, A, B, C, -0.33317932, -0.56013201, 1.8933113, ID="X_1712", classes=["center"])
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center"])
    X_2130 = point_from_barycentrics(model, A, B, C, 0.19373197, 0.27423005, 0.53203798, ID="X_2130", classes=["center"])
    central_line(model, X_40, X_1712, 40, 1712)
    central_line(model, X_1, X_2130, 1, 2130)
    X_3347 = intersect_lines(model, X_40, X_1712, X_1, X_2130, ID="X_3347", classes=["selected", "target"])
    X_1490 = eval_trilinear_point(model, A, B, C, '1 + sec(A) - sec(B) - sec(C)', ID="X_1490", classes=["center", "incident"])
    X_1498 = eval_trilinear_point(model, A, B, C, '(sin(A))*((tan(B))**(2) + (tan(C))**(2) - (tan(A))**(2))', ID="X_1498", classes=["center", "incident"])
    central_line(model, X_1490, X_1498, 1490, 1498, incident=True)
    return promote_point_to_top(model, X_3347)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3347 on the given reference triangle."""
    model = create_model('X_3347 = ISOGONAL CONJUGATE OF X_3182')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03347(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03347.json"))
    write_center_svg(
        model_acute,
        here / "x-03347.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
