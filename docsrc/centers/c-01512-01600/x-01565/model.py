"""GEOMETOR construction model for X_1565 = ORTHOJOIN OF X_657."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    gergonne_point_of,
    midpoint,
    nine_point_center_of,
    orthocenter_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_01565(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1565 = ORTHOJOIN OF X_657 on reference triangle ABC."""
    X_150 = eval_trilinear_point(model, A, B, C, '(b*c*(b**(4) + c**(4) - a**(4) + a*(b*c**(2) +c*b**(2) - b**(3) - c**(3)) - b*c*(a**(2) + b**(2) + c**(2)) + (b + c)*a**(3)))', ID="X_150", classes=["center"])
    X_664 = eval_trilinear_point(model, A, B, C, '1/(a*(b - c)*(b + c - a))', ID="X_664", classes=["center"])
    X_1565 = midpoint(model, X_150, X_664, ID="X_1565", classes=["selected", "target"], guide=False)
    X_5 = nine_point_center_of(model, A, B, C, ID="X_5", classes=["center", "incident"])
    X_85 = eval_trilinear_point(model, A, B, C, 'b**(2)*c**(2)/(b + c - a)', ID="X_85", classes=["center", "incident"])
    central_line(model, X_5, X_85, 5, 85, incident=True)
    X_7 = gergonne_point_of(model, A, B, C, ID="X_7", classes=["center", "incident"])
    X_104 = eval_trilinear_point(model, A, B, C, '1/(-1 + cos(B) + cos(C))', ID="X_104", classes=["center", "incident"])
    central_line(model, X_7, X_104, 7, 104, incident=True)
    X_4 = orthocenter_of(model, A, B, C, ID="X_4", classes=["center", "incident"])
    X_279 = eval_trilinear_point(model, A, B, C, 'csc(A)*(tan(A/2))**(2)', ID="X_279", classes=["center", "incident"])
    central_line(model, X_4, X_279, 4, 279, incident=True)
    return promote_point_to_top(model, X_1565)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1565 on the given reference triangle."""
    model = create_model('X_1565 = ORTHOJOIN OF X_657')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01565(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01565.json"))
    write_center_svg(
        model_acute,
        here / "x-01565.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
