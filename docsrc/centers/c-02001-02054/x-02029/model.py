"""GEOMETOR construction model for X_2029 = 2nd BROCARD-AXIS-MOSES-CIRCLE INTERSECTION."""

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
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_02029(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2029 = 2nd BROCARD-AXIS-MOSES-CIRCLE INTERSECTION on reference triangle ABC."""
    X_2029 = eval_trilinear_point(model, A, B, C, '(sin(A) + e*sin(A +  omega  ) - sin(A + 2*omega  ))', ID="X_2029", classes=["selected", "target"])
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center", "incident"])
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center", "incident"])
    central_line(model, X_3, X_6, 3, 6, incident=True)
    X_115 = eval_trilinear_point(model, A, B, C, 'b*c*(b**(2) - c**(2))**(2)', ID="X_115", classes=["center", "incident"])
    X_2040 = eval_trilinear_point(model, A, B, C, 'e*cos(A) + 2*e*cos(B)*cos(C) - cos(A +  omega  )', ID="X_2040", classes=["center", "incident"])
    central_line(model, X_115, X_2040, 115, 2040, incident=True)
    X_1506 = eval_trilinear_point(model, A, B, C, 'b*c*((b**(2) - c**(2))**(2) - 2*a**(2)*(b**(2) + c**(2)))', ID="X_1506", classes=["center", "incident"])
    X_2039 = eval_trilinear_point(model, A, B, C, 'e*cos(A) + 2*e*cos(B)*cos(C) + cos(A +  omega  )', ID="X_2039", classes=["center", "incident"])
    central_line(model, X_1506, X_2039, 1506, 2039, incident=True)
    return promote_point_to_top(model, X_2029)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2029 on the given reference triangle."""
    model = create_model('X_2029 = 2nd BROCARD-AXIS-MOSES-CIRCLE INTERSECTION')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02029(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02029.json"))
    write_center_svg(
        model_acute,
        here / "x-02029.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
