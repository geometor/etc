"""GEOMETOR construction model for X_3399 = SEC(A - 2ω) POINT."""

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
    nine_point_center_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_03399(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3399 = SEC(A - 2ω) POINT on reference triangle ABC."""
    X_3398 = eval_trilinear_point(model, A, B, C, 'cos(A - 2*omega  )', ID="X_3398", classes=["center"])
    X_3399 = isogonal_conjugate(model, A, B, C, X_3398, ID="X_3399", classes=["selected", "target"])
    X_262 = eval_trilinear_point(model, A, B, C, 'sec(A -  omega  )', ID="X_262", classes=["center", "incident"])
    X_1506 = eval_trilinear_point(model, A, B, C, 'b*c*((b**(2) - c**(2))**(2) - 2*a**(2)*(b**(2) + c**(2)))', ID="X_1506", classes=["center", "incident"])
    central_line(model, X_262, X_1506, 262, 1506, incident=True)
    X_5 = nine_point_center_of(model, A, B, C, ID="X_5", classes=["center", "incident"])
    X_1916 = eval_trilinear_point(model, A, B, C, 'b*c/(a**(4) - b**(2)*c**(2))', ID="X_1916", classes=["center", "incident"])
    central_line(model, X_5, X_1916, 5, 1916, incident=True)
    X_597 = eval_trilinear_point(model, A, B, C, '(4*a**(2) + b**(2) + c**(2))/a', ID="X_597", classes=["center", "incident"])
    X_1576 = eval_trilinear_point(model, A, B, C, 'a**(3)/(b**(2) - c**(2))', ID="X_1576", classes=["center", "incident"])
    central_line(model, X_597, X_1576, 597, 1576, incident=True)
    return promote_point_to_top(model, X_3399)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3399 on the given reference triangle."""
    model = create_model('X_3399 = SEC(A - 2ω) POINT')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03399(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03399.json"))
    write_center_svg(
        model_acute,
        here / "x-03399.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
