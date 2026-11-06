"""GEOMETOR construction model for X_3587 = INTERSECTION OF LINES X_1X_3 AND X_9X_30."""

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
    mittenpunkt_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_03587(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3587 = INTERSECTION OF LINES X_1X_3 AND X_9X_30 on reference triangle ABC."""
    X_3587 = eval_trilinear_point(model, A, B, C, '(a**(6) - a**(4)*(3*b + c)*(b + 3*c) + a**(2)*(3*b**(4) + 3*c**(4) + 2*b**(2)*c**(2) + 8*b*c**(3) + 8*b**(3)*c) - (b - c)**(4)*(b + c)**(2))', ID="X_3587", classes=["selected", "target"])
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center", "incident"])
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center", "incident"])
    central_line(model, X_1, X_3, 1, 3, incident=True)
    X_9 = mittenpunkt_of(model, A, B, C, ID="X_9", classes=["center", "incident"])
    X_30 = eval_trilinear_point(model, A, B, C, 'cos(A) - 2*cos(B)*cos(C)', ID="X_30", classes=["center", "incident"])
    central_line(model, X_9, X_30, 9, 30, incident=True)
    X_63 = eval_trilinear_point(model, A, B, C, 'cot(A)', ID="X_63", classes=["center", "incident"])
    X_376 = eval_trilinear_point(model, A, B, C, '5*cos(A) - cos(B - C)', ID="X_376", classes=["center", "incident"])
    central_line(model, X_63, X_376, 63, 376, incident=True)
    return promote_point_to_top(model, X_3587)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3587 on the given reference triangle."""
    model = create_model('X_3587 = INTERSECTION OF LINES X_1X_3 AND X_9X_30')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03587(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03587.json"))
    write_center_svg(
        model_acute,
        here / "x-03587.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
