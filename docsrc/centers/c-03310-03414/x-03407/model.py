"""GEOMETOR construction model for X_3407 = CSC(A + 2ω) POINT."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    incenter_of,
    isogonal_conjugate,
    promote_point_to_top,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_03407(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3407 = CSC(A + 2ω) POINT on reference triangle ABC."""
    X_3094 = eval_trilinear_point(model, A, B, C, 'sin(A + 2*omega  )', ID="X_3094", classes=["center"])
    X_3407 = isogonal_conjugate(model, A, B, C, X_3094, ID="X_3407", classes=["selected", "target"])
    X_76 = eval_trilinear_point(model, A, B, C, '1/a**(3)', ID="X_76", classes=["center", "incident"])
    X_384 = eval_trilinear_point(model, A, B, C, 'b*c*(a**(4) + b**(2)*c**(2))', ID="X_384", classes=["center", "incident"])
    central_line(model, X_76, X_384, 76, 384, incident=True)
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center", "incident"])
    X_1501 = eval_trilinear_point(model, A, B, C, 'a**(5)', ID="X_1501", classes=["center", "incident"])
    central_line(model, X_1, X_1501, 1, 1501, incident=True)
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center", "incident"])
    X_1916 = eval_trilinear_point(model, A, B, C, 'b*c/(a**(4) - b**(2)*c**(2))', ID="X_1916", classes=["center", "incident"])
    central_line(model, X_6, X_1916, 6, 1916, incident=True)
    return promote_point_to_top(model, X_3407)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3407 on the given reference triangle."""
    model = create_model('X_3407 = CSC(A + 2ω) POINT')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03407(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03407.json"))
    write_center_svg(
        model_acute,
        here / "x-03407.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
