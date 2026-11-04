"""GEOMETOR construction model for X_2925 = TANGENTIAL-ISOGONAL CONJUGATE OF X_15."""

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
    intersect_lines,
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_02925(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2925 = TANGENTIAL-ISOGONAL CONJUGATE OF X_15 on reference triangle ABC."""
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center"])
    X_13 = eval_trilinear_point(model, A, B, C, 'csc(A +  pi  /3)', ID="X_13", classes=["center"])
    X_22 = eval_trilinear_point(model, A, B, C, 'a*(b**(4) + c**(4) - a**(4))', ID="X_22", classes=["center"])
    X_1605 = point_from_barycentrics(model, A, B, C, 0.24200161, 0.21576869, 0.54222969, ID="X_1605", classes=["center"])
    central_line(model, X_3, X_13, 3, 13)
    central_line(model, X_22, X_1605, 22, 1605)
    X_2925 = intersect_lines(model, X_3, X_13, X_22, X_1605, ID="X_2925", classes=["selected", "target"])
    X_99 = eval_trilinear_point(model, A, B, C, 'b*c/(b**(2) - c**(2))', ID="X_99", classes=["center", "incident"])
    X_1606 = point_from_barycentrics(model, A, B, C, 0.46878519, 1.3979153, -0.86670046, ID="X_1606", classes=["center", "incident"])
    central_line(model, X_99, X_1606, 99, 1606, incident=True)
    return promote_point_to_top(model, X_2925)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2925 on the given reference triangle."""
    model = create_model('X_2925 = TANGENTIAL-ISOGONAL CONJUGATE OF X_15')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02925(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02925.json"))
    write_center_svg(
        model_acute,
        here / "x-02925.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
