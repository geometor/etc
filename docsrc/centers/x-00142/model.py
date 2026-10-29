"""GEOMETOR construction model for X(142) = COMPLEMENT OF X(9)."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    centroid_of,
    complement,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    gergonne_point_of,
    mittenpunkt_of,
    promote_point_to_top,
    spieker_center_of,
)
from geometor.etc.render import write_center_svg


def construct_x_00142(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(142) = COMPLEMENT OF X(9) on reference triangle ABC."""
    X_9 = mittenpunkt_of(model, A, B, C, ID="X(9)", classes=["center"])
    X_142 = complement(model, A, B, C, X_9, ID="X(142)", classes=["selected", "target"])
    X_2 = centroid_of(model, A, B, C, ID="X(2)", classes=["center", "incident"])
    X_7 = gergonne_point_of(model, A, B, C, ID="X(7)", classes=["center", "incident"])
    central_line(model, X_2, X_7, 2, 7, incident=True)
    X_10 = spieker_center_of(model, A, B, C, ID="X(10)", classes=["center", "incident"])
    X_141 = eval_trilinear_point(model, A, B, C, 'b*c*(b**(2) + c**(2))', ID="X(141)", classes=["center", "incident"])
    central_line(model, X_10, X_141, 10, 141, incident=True)
    X_116 = eval_trilinear_point(model, A, B, C, 'b*c*((b - c)**(2)*(b**(2) + b*c + c**(2) - a*b - a*c))', ID="X(116)", classes=["center", "incident"])
    X_119 = eval_trilinear_point(model, A, B, C, '(csc(A))*(-1 + cos(B) + cos(C))*(sin(2*B) + sin(2*C) + 2*(-1 + cos(A))*(sin(B) + sin(C)))', ID="X(119)", classes=["center", "incident"])
    central_line(model, X_116, X_119, 116, 119, incident=True)
    return promote_point_to_top(model, X_142)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(142) on the given reference triangle."""
    model = create_model('X(142) = COMPLEMENT OF X(9)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00142(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00142.json"))
    write_center_svg(
        model_acute,
        here / "x-00142.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
