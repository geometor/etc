"""GEOMETOR construction model for X_3340 = INTERSECTION OF LINES X_1X_3 AND X_7X_145."""

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
    nagel_point_of,
    promote_point_to_top,
    reflection_in_point,
)
from geometor.etc.render import write_center_svg


def construct_x_03340(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3340 = INTERSECTION OF LINES X_1X_3 AND X_7X_145 on reference triangle ABC."""
    X_1697 = eval_trilinear_point(model, A, B, C, '-1 + sin(A/2)*cos(B/2)*cos(C/2)', ID="X_1697", classes=["center"])
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center"])
    X_3340 = reflection_in_point(model, X_1697, X_1, ID="X_3340", classes=["selected", "target"], guide=False)
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center", "incident"])
    central_line(model, X_1, X_3, 1, 3, incident=True)
    X_7 = gergonne_point_of(model, A, B, C, ID="X_7", classes=["center", "incident"])
    X_145 = eval_trilinear_point(model, A, B, C, 'b*c*(3*a - b - c)', ID="X_145", classes=["center", "incident"])
    central_line(model, X_7, X_145, 7, 145, incident=True)
    X_8 = nagel_point_of(model, A, B, C, ID="X_8", classes=["center", "incident"])
    X_226 = eval_trilinear_point(model, A, B, C, '(csc(A))*(cos(B) + cos(C))', ID="X_226", classes=["center", "incident"])
    central_line(model, X_8, X_226, 8, 226, incident=True)
    return promote_point_to_top(model, X_3340)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3340 on the given reference triangle."""
    model = create_model('X_3340 = INTERSECTION OF LINES X_1X_3 AND X_7X_145')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03340(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03340.json"))
    write_center_svg(
        model_acute,
        here / "x-03340.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
