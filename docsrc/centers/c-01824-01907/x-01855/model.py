"""GEOMETOR construction model for X_1855 = ZOSMA TRANSFORM OF X_218."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    isogonal_conjugate,
    mittenpunkt_of,
    orthocenter_of,
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_01855(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1855 = ZOSMA TRANSFORM OF X_218 on reference triangle ABC."""
    X_1803 = point_from_barycentrics(model, A, B, C, 0.35654677, 0.40805729, 0.23539593, ID="X_1803", classes=["center"])
    X_1855 = isogonal_conjugate(model, A, B, C, X_1803, ID="X_1855", classes=["selected", "target"])
    X_4 = orthocenter_of(model, A, B, C, ID="X_4", classes=["center", "incident"])
    X_9 = mittenpunkt_of(model, A, B, C, ID="X_9", classes=["center", "incident"])
    central_line(model, X_4, X_9, 4, 9, incident=True)
    X_85 = eval_trilinear_point(model, A, B, C, 'b**(2)*c**(2)/(b + c - a)', ID="X_85", classes=["center", "incident"])
    X_92 = eval_trilinear_point(model, A, B, C, 'csc(2*A)', ID="X_92", classes=["center", "incident"])
    central_line(model, X_85, X_92, 85, 92, incident=True)
    X_65 = eval_trilinear_point(model, A, B, C, 'cos(B) + cos(C)', ID="X_65", classes=["center", "incident"])
    X_1146 = eval_trilinear_point(model, A, B, C, 'b*c*((b - c)*(b + c - a))**(2)', ID="X_1146", classes=["center", "incident"])
    central_line(model, X_65, X_1146, 65, 1146, incident=True)
    return promote_point_to_top(model, X_1855)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1855 on the given reference triangle."""
    model = create_model('X_1855 = ZOSMA TRANSFORM OF X_218')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01855(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01855.json"))
    write_center_svg(
        model_acute,
        here / "x-01855.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
