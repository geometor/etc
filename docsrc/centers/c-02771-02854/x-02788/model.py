"""GEOMETOR construction model for X_2788 = ISOGONAL CONJUGATE OF X_2704."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    isogonal_conjugate,
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_02788(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2788 = ISOGONAL CONJUGATE OF X_2704 on reference triangle ABC."""
    X_2704 = point_from_barycentrics(model, A, B, C, 0.25390548, 1.1213867, -0.37529215, ID="X_2704", classes=["center"])
    X_2788 = isogonal_conjugate(model, A, B, C, X_2704, ID="X_2788", classes=["selected", "target"])
    X_98 = eval_trilinear_point(model, A, B, C, 'sec(A +  omega  )', ID="X_98", classes=["center", "incident"])
    X_105 = eval_trilinear_point(model, A, B, C, '1/(b**(2) + c**(2) - a*(b + c))', ID="X_105", classes=["center", "incident"])
    central_line(model, X_98, X_105, 98, 105, incident=True)
    X_114 = eval_trilinear_point(model, A, B, C, 'b*c*(b*sec(B +  omega  ) + c*sec(C +  omega  ))', ID="X_114", classes=["center", "incident"])
    X_120 = eval_trilinear_point(model, A, B, C, 'b*c*(2*a*b*c - (b + c)*(a**(2) + (b - c)**(2)))*(b**(2) + c**(2) - a*b -a*c)', ID="X_120", classes=["center", "incident"])
    central_line(model, X_114, X_120, 114, 120, incident=True)
    X_30 = eval_trilinear_point(model, A, B, C, 'cos(A) - 2*cos(B)*cos(C)', ID="X_30", classes=["center", "incident"])
    X_511 = eval_trilinear_point(model, A, B, C, 'cos(A +  omega  )', ID="X_511", classes=["center", "incident"])
    central_line(model, X_30, X_511, 30, 511, incident=True)
    return promote_point_to_top(model, X_2788)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2788 on the given reference triangle."""
    model = create_model('X_2788 = ISOGONAL CONJUGATE OF X_2704')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02788(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02788.json"))
    write_center_svg(
        model_acute,
        here / "x-02788.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
