"""GEOMETOR construction model for X_3027 = INCIRCLE-ANTIPODE OF X_3023."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    feuerbach_point_of,
    incenter_of,
    promote_point_to_top,
    reflection_in_point,
)
from geometor.etc.render import write_center_svg


def construct_x_03027(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3027 = INCIRCLE-ANTIPODE OF X_3023 on reference triangle ABC."""
    X_3023 = eval_trilinear_point(model, A, B, C, '(b*c*(b + c - a)*(b - c)**(2)*(a**(2) + b*c)**(2))', ID="X_3023", classes=["center"])
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center"])
    X_3027 = reflection_in_point(model, X_3023, X_1, ID="X_3027", classes=["selected", "target"], guide=False)
    X_11 = feuerbach_point_of(model, A, B, C, ID="X_11", classes=["center", "incident"])
    X_114 = eval_trilinear_point(model, A, B, C, 'b*c*(b*sec(B +  omega  ) + c*sec(C +  omega  ))', ID="X_114", classes=["center", "incident"])
    central_line(model, X_11, X_114, 11, 114, incident=True)
    X_12 = eval_trilinear_point(model, A, B, C, '1 + cos(B - C)', ID="X_12", classes=["center", "incident"])
    X_115 = eval_trilinear_point(model, A, B, C, 'b*c*(b**(2) - c**(2))**(2)', ID="X_115", classes=["center", "incident"])
    central_line(model, X_12, X_115, 12, 115, incident=True)
    X_56 = eval_trilinear_point(model, A, B, C, 'a/(b + c - a)', ID="X_56", classes=["center", "incident"])
    X_99 = eval_trilinear_point(model, A, B, C, 'b*c/(b**(2) - c**(2))', ID="X_99", classes=["center", "incident"])
    central_line(model, X_56, X_99, 56, 99, incident=True)
    return promote_point_to_top(model, X_3027)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3027 on the given reference triangle."""
    model = create_model('X_3027 = INCIRCLE-ANTIPODE OF X_3023')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03027(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03027.json"))
    write_center_svg(
        model_acute,
        here / "x-03027.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
