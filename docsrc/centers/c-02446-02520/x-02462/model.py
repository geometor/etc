"""GEOMETOR construction model for X_2462 = INVERSE-IN-1st-LEMOINE-CIRCLE OF X_372."""

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
    reflection_in_point,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_02462(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2462 = INVERSE-IN-1st-LEMOINE-CIRCLE OF X_372 on reference triangle ABC."""
    X_2461 = eval_trilinear_point(model, A, B, C, '(cos(A - 3*omega  ) - cos(A -  omega  ) + 2*cos(A +  omega  ) - 2*cos(omega)*sin(A - 2*omega  ))', ID="X_2461", classes=["center"])
    X_2458 = eval_trilinear_point(model, A, B, C, '(sin(A) - sin(3*omega)*cos(A -  omega  ))', ID="X_2458", classes=["center"])
    X_2462 = reflection_in_point(model, X_2461, X_2458, ID="X_2462", classes=["selected", "target"], guide=False)
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center", "incident"])
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center", "incident"])
    central_line(model, X_3, X_6, 3, 6, incident=True)
    return promote_point_to_top(model, X_2462)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2462 on the given reference triangle."""
    model = create_model('X_2462 = INVERSE-IN-1st-LEMOINE-CIRCLE OF X_372')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02462(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02462.json"))
    write_center_svg(
        model_acute,
        here / "x-02462.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
