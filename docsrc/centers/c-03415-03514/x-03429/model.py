"""GEOMETOR construction model for X_3429 = X_3-VERTEX CONJUGATE OF X_10."""

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
    promote_point_to_top,
    spieker_center_of,
)
from geometor.etc.render import write_center_svg


def construct_x_03429(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3429 = X_3-VERTEX CONJUGATE OF X_10 on reference triangle ABC."""
    X_3429 = eval_barycentric_point(model, A, B, C, '1/(a**(5) + a**(3)*b*c + a**(2)*(b + c)*(2*b**(2) - b*c + 2*c**(2)) - a*(b + c)**(2)*(b**(2) - b*c + c**(2)) - (b + c)*(2*b**(4) - b**(3)*c + 2*b**(2)*c**(2) - b*c**(3) + 2*c**(4)))', ID="X_3429", classes=["selected", "target"])
    X_10 = spieker_center_of(model, A, B, C, ID="X_10", classes=["center", "incident"])
    X_1503 = eval_trilinear_point(model, A, B, C, 'sin(A)*tan(omega)  - 2*cos(B)*cos(C)', ID="X_1503", classes=["center", "incident"])
    central_line(model, X_10, X_1503, 10, 1503, incident=True)
    return promote_point_to_top(model, X_3429)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3429 on the given reference triangle."""
    model = create_model('X_3429 = X_3-VERTEX CONJUGATE OF X_10')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03429(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03429.json"))
    write_center_svg(
        model_acute,
        here / "x-03429.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
