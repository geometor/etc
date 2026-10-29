"""GEOMETOR construction model for X(990) = INTERSECTION OF LINES X(1)X(7) AND X(3)X(37)."""

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
    incenter_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00990(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(990) = INTERSECTION OF LINES X(1)X(7) AND X(3)X(37) on reference triangle ABC."""
    X_990 = eval_trilinear_point(model, A, B, C, 'a**(5)- a**(4)*(b + c) - 2*a**(3)*b*c - a*(b - c)**(2)*(b**(2)+ c**(2)) + (b - c)**(2)*(b + c)**(3)', ID="X(990)", classes=["selected", "target"])
    X_1 = incenter_of(model, A, B, C, ID="X(1)", classes=["center", "incident"])
    X_7 = gergonne_point_of(model, A, B, C, ID="X(7)", classes=["center", "incident"])
    central_line(model, X_1, X_7, 1, 7, incident=True)
    X_3 = circumcenter_of(model, A, B, C, ID="X(3)", classes=["center", "incident"])
    X_37 = eval_trilinear_point(model, A, B, C, 'b + c', ID="X(37)", classes=["center", "incident"])
    central_line(model, X_3, X_37, 3, 37, incident=True)
    X_33 = eval_trilinear_point(model, A, B, C, '1 + sec(A)', ID="X(33)", classes=["center", "incident"])
    X_57 = eval_trilinear_point(model, A, B, C, '1/(b + c - a)', ID="X(57)", classes=["center", "incident"])
    central_line(model, X_33, X_57, 33, 57, incident=True)
    return promote_point_to_top(model, X_990)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(990) on the given reference triangle."""
    model = create_model('X(990) = INTERSECTION OF LINES X(1)X(7) AND X(3)X(37)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00990(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00990.json"))
    write_center_svg(
        model_acute,
        here / "x-00990.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
