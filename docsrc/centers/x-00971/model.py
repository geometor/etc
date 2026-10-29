"""GEOMETOR construction model for X(971) = INTERSECTION OF LINES X(3)X(9) AND X(4)X(7)."""

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
    gergonne_point_of,
    mittenpunkt_of,
    orthocenter_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00971(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(971) = INTERSECTION OF LINES X(3)X(9) AND X(4)X(7) on reference triangle ABC."""
    X_971 = eval_trilinear_point(model, A, B, C, 'a**(4)*(b + c) - 2*a**(3)*(b**(2) + c**(2) - b*c) + 2*a*(b - c)**(2)*(b**(2) + c**(2) + b*c) - (b - c)**(2)*(b + c)**(3)', ID="X(971)", classes=["selected", "target"])
    X_4 = orthocenter_of(model, A, B, C, ID="X(4)", classes=["center", "incident"])
    X_7 = gergonne_point_of(model, A, B, C, ID="X(7)", classes=["center", "incident"])
    central_line(model, X_4, X_7, 4, 7, incident=True)
    X_3 = circumcenter_of(model, A, B, C, ID="X(3)", classes=["center", "incident"])
    X_9 = mittenpunkt_of(model, A, B, C, ID="X(9)", classes=["center", "incident"])
    central_line(model, X_3, X_9, 3, 9, incident=True)
    X_20 = eval_trilinear_point(model, A, B, C, 'cos(A) - cos(B)*cos(C)', ID="X(20)", classes=["center", "incident"])
    X_72 = eval_trilinear_point(model, A, B, C, '(b + c)*cot(A)', ID="X(72)", classes=["center", "incident"])
    central_line(model, X_20, X_72, 20, 72, incident=True)
    return promote_point_to_top(model, X_971)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(971) on the given reference triangle."""
    model = create_model('X(971) = INTERSECTION OF LINES X(3)X(9) AND X(4)X(7)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00971(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00971.json"))
    write_center_svg(
        model_acute,
        here / "x-00971.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
