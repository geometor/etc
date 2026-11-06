"""GEOMETOR construction model for X_3760 = X_2275com[T(-bc, c²)]."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_barycentric_point,
    eval_trilinear_point,
    incenter_of,
    isotomic_conjugate,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_03760(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3760 = X_2275com[T(-bc, c²)] on reference triangle ABC."""
    X_749 = eval_trilinear_point(model, A, B, C, '1/(a**(2) - 2*b*c)', ID="X_749", classes=["center"])
    X_3760 = isotomic_conjugate(model, A, B, C, X_749, ID="X_3760", classes=["selected", "target"])
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center", "incident"])
    X_76 = eval_trilinear_point(model, A, B, C, '1/a**(3)', ID="X_76", classes=["center", "incident"])
    central_line(model, X_1, X_76, 1, 76, incident=True)
    X_35 = eval_trilinear_point(model, A, B, C, '1 + 2*cos(A)', ID="X_35", classes=["center", "incident"])
    X_183 = eval_trilinear_point(model, A, B, C, 'b**(2)*c**(2)*cos(A-  omega  )', ID="X_183", classes=["center", "incident"])
    central_line(model, X_35, X_183, 35, 183, incident=True)
    X_384 = eval_trilinear_point(model, A, B, C, 'b*c*(a**(4) + b**(2)*c**(2))', ID="X_384", classes=["center", "incident"])
    X_609 = eval_barycentric_point(model, A, B, C, 'a*( area + a**(2)*sin(A))', ID="X_609", classes=["center", "incident"])
    central_line(model, X_384, X_609, 384, 609, incident=True)
    return promote_point_to_top(model, X_3760)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3760 on the given reference triangle."""
    model = create_model('X_3760 = X_2275com[T(-bc, c²)]')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03760(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03760.json"))
    write_center_svg(
        model_acute,
        here / "x-03760.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
