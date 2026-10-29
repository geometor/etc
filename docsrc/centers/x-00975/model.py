"""GEOMETOR construction model for X(975) = INTERSECTION OF LINES X(1)X(2) AND X(3)X(37)."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    centroid_of,
    circumcenter_of,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    incenter_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00975(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(975) = INTERSECTION OF LINES X(1)X(2) AND X(3)X(37) on reference triangle ABC."""
    X_975 = eval_trilinear_point(model, A, B, C, 'a**(3)+ a**(2)*(b + c) + a*(b**(2)+ c**(2)+ 4*b*c) + (b + c)**(3)', ID="X(975)", classes=["selected", "target"])
    X_1 = incenter_of(model, A, B, C, ID="X(1)", classes=["center", "incident"])
    X_2 = centroid_of(model, A, B, C, ID="X(2)", classes=["center", "incident"])
    central_line(model, X_1, X_2, 1, 2, incident=True)
    X_3 = circumcenter_of(model, A, B, C, ID="X(3)", classes=["center", "incident"])
    X_37 = eval_trilinear_point(model, A, B, C, 'b + c', ID="X(37)", classes=["center", "incident"])
    central_line(model, X_3, X_37, 3, 37, incident=True)
    X_28 = eval_trilinear_point(model, A, B, C, '(tan(A))/(b + c)', ID="X(28)", classes=["center", "incident"])
    X_33 = eval_trilinear_point(model, A, B, C, '1 + sec(A)', ID="X(33)", classes=["center", "incident"])
    central_line(model, X_28, X_33, 28, 33, incident=True)
    return promote_point_to_top(model, X_975)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(975) on the given reference triangle."""
    model = create_model('X(975) = INTERSECTION OF LINES X(1)X(2) AND X(3)X(37)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00975(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00975.json"))
    write_center_svg(
        model_acute,
        here / "x-00975.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
