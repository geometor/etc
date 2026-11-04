"""GEOMETOR construction model for X_1064 = INTERSECTION OF LINES X_1X_4 AND X_3X_31."""

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
    incenter_of,
    orthocenter_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_01064(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1064 = INTERSECTION OF LINES X_1X_4 AND X_3X_31 on reference triangle ABC."""
    X_1064 = eval_trilinear_point(model, A, B, C, '(1 + cos(A)*(cos(B) + cos(C)))', ID="X_1064", classes=["selected", "target"])
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center", "incident"])
    X_4 = orthocenter_of(model, A, B, C, ID="X_4", classes=["center", "incident"])
    central_line(model, X_1, X_4, 1, 4, incident=True)
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center", "incident"])
    X_31 = eval_trilinear_point(model, A, B, C, 'a**(2)', ID="X_31", classes=["center", "incident"])
    central_line(model, X_3, X_31, 3, 31, incident=True)
    X_102 = eval_trilinear_point(model, A, B, C, '1/(sin(B)*(sec(A) - sec(B)) + sin(C)*(sec(A) - sec(C)))', ID="X_102", classes=["center", "incident"])
    X_112 = eval_trilinear_point(model, A, B, C, 'a/(sin(2*B) - sin(2*C))', ID="X_112", classes=["center", "incident"])
    central_line(model, X_102, X_112, 102, 112, incident=True)
    return promote_point_to_top(model, X_1064)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1064 on the given reference triangle."""
    model = create_model('X_1064 = INTERSECTION OF LINES X_1X_4 AND X_3X_31')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01064(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01064.json"))
    write_center_svg(
        model_acute,
        here / "x-01064.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
