"""GEOMETOR construction model for X_3044 = INTERSECTION X_54X_114∩X_99X_184."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_03044(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3044 = INTERSECTION X_54X_114∩X_99X_184 on reference triangle ABC."""
    X_3044 = eval_trilinear_point(model, A, B, C, '(a*(a**(4) + b**(4) - a**(2)*b**(2) - a**(2)*c**(2))*(a**(4) + c**(4) - a**(2)*b**(2) - a**(2)*c**(2)))', ID="X_3044", classes=["selected", "target"])
    X_54 = eval_trilinear_point(model, A, B, C, 'sec(B - C)', ID="X_54", classes=["center", "incident"])
    X_114 = eval_trilinear_point(model, A, B, C, 'b*c*(b*sec(B +  omega  ) + c*sec(C +  omega  ))', ID="X_114", classes=["center", "incident"])
    central_line(model, X_54, X_114, 54, 114, incident=True)
    X_99 = eval_trilinear_point(model, A, B, C, 'b*c/(b**(2) - c**(2))', ID="X_99", classes=["center", "incident"])
    X_184 = eval_trilinear_point(model, A, B, C, 'a**(2)*cos(A)', ID="X_184", classes=["center", "incident"])
    central_line(model, X_99, X_184, 99, 184, incident=True)
    X_98 = eval_trilinear_point(model, A, B, C, 'sec(A +  omega  )', ID="X_98", classes=["center", "incident"])
    X_1147 = eval_trilinear_point(model, A, B, C, '(sin(4*A))/sin(A)', ID="X_1147", classes=["center", "incident"])
    central_line(model, X_98, X_1147, 98, 1147, incident=True)
    return promote_point_to_top(model, X_3044)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3044 on the given reference triangle."""
    model = create_model('X_3044 = INTERSECTION X_54X_114∩X_99X_184')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03044(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03044.json"))
    write_center_svg(
        model_acute,
        here / "x-03044.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
