"""GEOMETOR construction model for X_1368 = COMPLEMENTARY CONJUGATE OF X_6."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    centroid_of,
    circumcenter_of,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_01368(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1368 = COMPLEMENTARY CONJUGATE OF X_6 on reference triangle ABC."""
    X_1368 = eval_trilinear_point(model, A, B, C, 'b*c*(b**(2)/(a**(2) - b**(2) + c**(2)) + c**(2)/(a**(2) + b**(2) - c**(2)))', ID="X_1368", classes=["selected", "target"])
    X_2 = centroid_of(model, A, B, C, ID="X_2", classes=["center"])
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center"])
    central_line(model, X_2, X_3, 2, 3)
    X_114 = eval_trilinear_point(model, A, B, C, 'b*c*(b*sec(B + omega ) + c*sec(C + omega ))', ID="X_114", classes=["center", "incident"])
    X_122 = eval_trilinear_point(model, A, B, C, '(b**(2) - c**(2))**(2)*(cos(A) - cos(B)*cos(C))*(cot(A))**(2)', ID="X_122", classes=["center", "incident"])
    central_line(model, X_114, X_122, 114, 122, incident=True)
    X_120 = eval_trilinear_point(model, A, B, C, 'b*c*(2*a*b*c - (b + c)*(a**(2) + (b - c)**(2)))*(b**(2) + c**(2) - a*b -a*c)', ID="X_120", classes=["center", "incident"])
    X_123 = eval_trilinear_point(model, A, B, C, '(csc(A))*(sec(B) - sec(C))*((sec(A))*((sin(B))**(2) - (sin(C))**(2)) + sin(C)*tan(C) - sin(B)*tan(B))', ID="X_123", classes=["center", "incident"])
    central_line(model, X_120, X_123, 120, 123, incident=True)
    return promote_point_to_top(model, X_1368)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1368 on the given reference triangle."""
    model = create_model('X_1368 = COMPLEMENTARY CONJUGATE OF X_6')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01368(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01368.json"))
    write_center_svg(
        model_acute,
        here / "x-01368.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
