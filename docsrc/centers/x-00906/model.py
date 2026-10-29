"""GEOMETOR construction model for X(906) = INTERSECTION OF LINES X(100)X(112) AND X(101)X(109)."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00906(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(906) = INTERSECTION OF LINES X(100)X(112) AND X(101)X(109) on reference triangle ABC."""
    X_906 = eval_trilinear_point(model, A, B, C, '(sin(2*A))/(b - c)', ID="X(906)", classes=["selected", "target"])
    X_101 = eval_trilinear_point(model, A, B, C, 'a/(b - c)', ID="X(101)", classes=["center", "incident"])
    X_109 = eval_trilinear_point(model, A, B, C, 'a/(cos(B) - cos(C))', ID="X(109)", classes=["center", "incident"])
    central_line(model, X_101, X_109, 101, 109, incident=True)
    X_100 = eval_trilinear_point(model, A, B, C, '1/(b - c)', ID="X(100)", classes=["center", "incident"])
    X_112 = eval_trilinear_point(model, A, B, C, 'a/(sin(2*B) - sin(2*C))', ID="X(112)", classes=["center", "incident"])
    central_line(model, X_100, X_112, 100, 112, incident=True)
    X_32 = eval_trilinear_point(model, A, B, C, 'a**(3)', ID="X(32)", classes=["center", "incident"])
    X_218 = eval_trilinear_point(model, A, B, C, '(cos(A/2))**(2)*((cos(B/2))**(4) + (cos(C/2))**(4) - (cos(A/2))**(4))', ID="X(218)", classes=["center", "incident"])
    central_line(model, X_32, X_218, 32, 218, incident=True)
    return promote_point_to_top(model, X_906)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(906) on the given reference triangle."""
    model = create_model('X(906) = INTERSECTION OF LINES X(100)X(112) AND X(101)X(109)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00906(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00906.json"))
    write_center_svg(
        model_acute,
        here / "x-00906.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
