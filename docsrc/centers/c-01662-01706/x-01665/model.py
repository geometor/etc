"""GEOMETOR construction model for X_1665 = INVERSE-IN-BROCARD-CIRCLE OF X_1663."""

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


def construct_x_01665(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1665 = INVERSE-IN-BROCARD-CIRCLE OF X_1663 on reference triangle ABC."""
    X_1664 = eval_trilinear_point(model, A, B, C, '(e*cos(A +  omega  ) + cos(A -  omega  ))', ID="X_1664", classes=["center"])
    X_182 = eval_trilinear_point(model, A, B, C, 'cos(A-  omega  )', ID="X_182", classes=["center"])
    X_1665 = reflection_in_point(model, X_1664, X_182, ID="X_1665", classes=["selected", "target"], guide=False)
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center", "incident"])
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center", "incident"])
    central_line(model, X_3, X_6, 3, 6, incident=True)
    return promote_point_to_top(model, X_1665)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1665 on the given reference triangle."""
    model = create_model('X_1665 = INVERSE-IN-BROCARD-CIRCLE OF X_1663')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01665(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01665.json"))
    write_center_svg(
        model_acute,
        here / "x-01665.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
