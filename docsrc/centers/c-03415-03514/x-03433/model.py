"""GEOMETOR construction model for X_3433 = X_7-VERTEX CONJUGATE OF X_7."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    circumcenter_of,
    construct_baseline_triangle,
    create_model,
    eval_barycentric_point,
    eval_trilinear_point,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_03433(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3433 = X_7-VERTEX CONJUGATE OF X_7 on reference triangle ABC."""
    X_3433 = eval_barycentric_point(model, A, B, C, 'a**(2)/(a**(3) - a**(2)*b - a**(2)*c + a*b**(2) + a*c**(2) - (b + c)*(b - c)**(2))', ID="X_3433", classes=["selected", "target"])
    X_104 = eval_trilinear_point(model, A, B, C, '1/(-1 + cos(B) + cos(C))', ID="X_104", classes=["center", "incident"])
    X_378 = eval_trilinear_point(model, A, B, C, 'sec(A) + 2*cos(A)', ID="X_378", classes=["center", "incident"])
    central_line(model, X_104, X_378, 104, 378, incident=True)
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center", "incident"])
    X_518 = eval_trilinear_point(model, A, B, C, '(a*b + a*c - b**(2) - c**(2))', ID="X_518", classes=["center", "incident"])
    central_line(model, X_3, X_518, 3, 518, incident=True)
    X_48 = eval_trilinear_point(model, A, B, C, 'tan(B) + tan(C)', ID="X_48", classes=["center", "incident"])
    X_672 = eval_trilinear_point(model, A, B, C, 'a*(b**(2) + c**(2) - a*(b + c))', ID="X_672", classes=["center", "incident"])
    central_line(model, X_48, X_672, 48, 672, incident=True)
    return promote_point_to_top(model, X_3433)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3433 on the given reference triangle."""
    model = create_model('X_3433 = X_7-VERTEX CONJUGATE OF X_7')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03433(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03433.json"))
    write_center_svg(
        model_acute,
        here / "x-03433.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
