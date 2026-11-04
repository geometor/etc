"""GEOMETOR construction model for X_1388 = POINT ANCHA."""

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
    feuerbach_point_of,
    incenter_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_01388(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1388 = POINT ANCHA on reference triangle ABC."""
    X_1388 = eval_trilinear_point(model, A, B, C, '((3*a - 2*b -2*c)/(a - b - c))', ID="X_1388", classes=["selected", "target"])
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center", "incident"])
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center", "incident"])
    central_line(model, X_1, X_3, 1, 3, incident=True)
    X_11 = feuerbach_point_of(model, A, B, C, ID="X_11", classes=["center", "incident"])
    X_944 = eval_trilinear_point(model, A, B, C, 'b*c*(3*a**(4) - 2*a**(3)*(b + c) + (b - c)**(2)*(2*a*b + 2*a*c - 2*b*c - b**(2) - c**(2) - 2*a**(2)))', ID="X_944", classes=["center", "incident"])
    central_line(model, X_11, X_944, 11, 944, incident=True)
    X_73 = eval_trilinear_point(model, A, B, C, 'sec(B) + sec(C)', ID="X_73", classes=["center", "incident"])
    X_1149 = eval_trilinear_point(model, A, B, C, '(a*(b**(2) + c**(2) + b*a + c*a - 4*b*c))', ID="X_1149", classes=["center", "incident"])
    central_line(model, X_73, X_1149, 73, 1149, incident=True)
    return promote_point_to_top(model, X_1388)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1388 on the given reference triangle."""
    model = create_model('X_1388 = POINT ANCHA')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01388(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01388.json"))
    write_center_svg(
        model_acute,
        here / "x-01388.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
