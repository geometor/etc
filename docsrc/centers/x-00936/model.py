"""GEOMETOR construction model for X(936) = INTERSECTION OF LINES X(1)X(2) AND X(3)X(9)."""

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
    mittenpunkt_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00936(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(936) = INTERSECTION OF LINES X(1)X(2) AND X(3)X(9) on reference triangle ABC."""
    X_936 = eval_trilinear_point(model, A, B, C, 'a**(3) - a**(2)*(b + c) - a*(b - c)**(2) + (b + c)**(3)', ID="X(936)", classes=["selected", "target"])
    X_1 = incenter_of(model, A, B, C, ID="X(1)", classes=["center", "incident"])
    X_2 = centroid_of(model, A, B, C, ID="X(2)", classes=["center", "incident"])
    central_line(model, X_1, X_2, 1, 2, incident=True)
    X_3 = circumcenter_of(model, A, B, C, ID="X(3)", classes=["center", "incident"])
    X_9 = mittenpunkt_of(model, A, B, C, ID="X(9)", classes=["center", "incident"])
    central_line(model, X_3, X_9, 3, 9, incident=True)
    X_57 = eval_trilinear_point(model, A, B, C, '1/(b + c - a)', ID="X(57)", classes=["center", "incident"])
    X_72 = eval_trilinear_point(model, A, B, C, '(b + c)*cot(A)', ID="X(72)", classes=["center", "incident"])
    central_line(model, X_57, X_72, 57, 72, incident=True)
    return promote_point_to_top(model, X_936)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(936) on the given reference triangle."""
    model = create_model('X(936) = INTERSECTION OF LINES X(1)X(2) AND X(3)X(9)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00936(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00936.json"))
    write_center_svg(
        model_acute,
        here / "x-00936.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
