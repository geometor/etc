"""GEOMETOR construction model for X_3051 = INTERSECTION X_2X_6∩X_32X_184."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    centroid_of,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    isogonal_conjugate,
    promote_point_to_top,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_03051(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3051 = INTERSECTION X_2X_6∩X_32X_184 on reference triangle ABC."""
    X_308 = eval_trilinear_point(model, A, B, C, 'b**(3)*c**(3)/(b**(2) + c**(2))', ID="X_308", classes=["center"])
    X_3051 = isogonal_conjugate(model, A, B, C, X_308, ID="X_3051", classes=["selected", "target"])
    X_2 = centroid_of(model, A, B, C, ID="X_2", classes=["center", "incident"])
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center", "incident"])
    central_line(model, X_2, X_6, 2, 6, incident=True)
    X_32 = eval_trilinear_point(model, A, B, C, 'a**(3)', ID="X_32", classes=["center", "incident"])
    X_184 = eval_trilinear_point(model, A, B, C, 'a**(2)*cos(A)', ID="X_184", classes=["center", "incident"])
    central_line(model, X_32, X_184, 32, 184, incident=True)
    X_25 = eval_trilinear_point(model, A, B, C, 'sin(A)*tan(A)', ID="X_25", classes=["center", "incident"])
    X_263 = eval_trilinear_point(model, A, B, C, 'a**(2)*sec(A -  omega  )', ID="X_263", classes=["center", "incident"])
    central_line(model, X_25, X_263, 25, 263, incident=True)
    return promote_point_to_top(model, X_3051)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3051 on the given reference triangle."""
    model = create_model('X_3051 = INTERSECTION X_2X_6∩X_32X_184')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03051(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03051.json"))
    write_center_svg(
        model_acute,
        here / "x-03051.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
