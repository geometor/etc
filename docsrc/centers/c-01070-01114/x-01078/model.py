"""GEOMETOR construction model for X_1078 = INTERSECTION OF LINES X_2X_32 AND X_3X_76."""

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
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_01078(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1078 = INTERSECTION OF LINES X_2X_32 AND X_3X_76 on reference triangle ABC."""
    X_1078 = eval_trilinear_point(model, A, B, C, '(b*c*(b**(2)*c**(2) + c**(2)*a**(2) + a**(2)*b**(2) - a**(4)))', ID="X_1078", classes=["selected", "target"])
    X_2 = centroid_of(model, A, B, C, ID="X_2", classes=["center", "incident"])
    X_32 = eval_trilinear_point(model, A, B, C, 'a**(3)', ID="X_32", classes=["center", "incident"])
    central_line(model, X_2, X_32, 2, 32, incident=True)
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center", "incident"])
    X_76 = eval_trilinear_point(model, A, B, C, '1/a**(3)', ID="X_76", classes=["center", "incident"])
    central_line(model, X_3, X_76, 3, 76, incident=True)
    X_54 = eval_trilinear_point(model, A, B, C, 'sec(B - C)', ID="X_54", classes=["center", "incident"])
    X_69 = eval_trilinear_point(model, A, B, C, '(cos(A))/a**(2)', ID="X_69", classes=["center", "incident"])
    central_line(model, X_54, X_69, 54, 69, incident=True)
    return promote_point_to_top(model, X_1078)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1078 on the given reference triangle."""
    model = create_model('X_1078 = INTERSECTION OF LINES X_2X_32 AND X_3X_76')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01078(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01078.json"))
    write_center_svg(
        model_acute,
        here / "x-01078.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
