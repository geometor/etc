"""GEOMETOR construction model for X_3622 = H(X_8; M,-1/2)."""

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
    incenter_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_03622(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3622 = H(X_8; M,-1/2) on reference triangle ABC."""
    X_3622 = eval_trilinear_point(model, A, B, C, '2*r + R*sin(B)*sin(C)', ID="X_3622", classes=["selected", "target"])
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center", "incident"])
    X_2 = centroid_of(model, A, B, C, ID="X_2", classes=["center", "incident"])
    central_line(model, X_1, X_2, 1, 2, incident=True)
    X_149 = eval_trilinear_point(model, A, B, C, '(b*c*(b**(3) + c**(3) - a**(3) + (a**(2) - b*c)*(b + c) + a*(b*c - b**(2) - c**(2))))', ID="X_149", classes=["center", "incident"])
    X_377 = eval_trilinear_point(model, A, B, C, '(b*c*(b**(4) + c**(4) - a**(4) - 2*b**(2)*c**(2) - 2*a*b*c*(a + b + c)))', ID="X_377", classes=["center", "incident"])
    central_line(model, X_149, X_377, 149, 377, incident=True)
    X_21 = eval_trilinear_point(model, A, B, C, '1/(cos(B) + cos(C))', ID="X_21", classes=["center", "incident"])
    X_999 = eval_trilinear_point(model, A, B, C, '2 - cos(A)', ID="X_999", classes=["center", "incident"])
    central_line(model, X_21, X_999, 21, 999, incident=True)
    return promote_point_to_top(model, X_3622)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3622 on the given reference triangle."""
    model = create_model('X_3622 = H(X_8; M,-1/2)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03622(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03622.json"))
    write_center_svg(
        model_acute,
        here / "x-03622.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
