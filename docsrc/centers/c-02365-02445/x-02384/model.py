"""GEOMETOR construction model for X_2384 = CIR(X_545)."""

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
    isogonal_conjugate,
    promote_point_to_top,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_02384(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2384 = CIR(X_545) on reference triangle ABC."""
    X_545 = eval_barycentric_point(model, A, B, C, '2*a**(2) - b**(2) - c**(2) - 2*a*b - 2*a*c + 4*b*c', ID="X_545", classes=["center"])
    X_2384 = isogonal_conjugate(model, A, B, C, X_545, ID="X_2384", classes=["selected", "target"])
    X_44 = eval_trilinear_point(model, A, B, C, 'b + c - 2*a', ID="X_44", classes=["center", "incident"])
    X_100 = eval_trilinear_point(model, A, B, C, '1/(b - c)', ID="X_100", classes=["center", "incident"])
    central_line(model, X_44, X_100, 44, 100, incident=True)
    X_106 = eval_trilinear_point(model, A, B, C, 'a/(2*a - b - c)', ID="X_106", classes=["center", "incident"])
    X_649 = eval_trilinear_point(model, A, B, C, 'a*(b - c)', ID="X_649", classes=["center", "incident"])
    central_line(model, X_106, X_649, 106, 649, incident=True)
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center", "incident"])
    X_901 = eval_trilinear_point(model, A, B, C, 'a/((b - c)*(b + c - 2*a))', ID="X_901", classes=["center", "incident"])
    central_line(model, X_6, X_901, 6, 901, incident=True)
    return promote_point_to_top(model, X_2384)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2384 on the given reference triangle."""
    model = create_model('X_2384 = CIR(X_545)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02384(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02384.json"))
    write_center_svg(
        model_acute,
        here / "x-02384.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
