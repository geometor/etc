"""GEOMETOR construction model for X_3501 = INTERSECTION OF LINES X_1X_39 AND X_4X_9."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    incenter_of,
    isogonal_conjugate,
    mittenpunkt_of,
    orthocenter_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_03501(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3501 = INTERSECTION OF LINES X_1X_39 AND X_4X_9 on reference triangle ABC."""
    X_3500 = eval_trilinear_point(model, A, B, C, '(1/(a**(2)*b + a**(2)*c - a*(b**(2) + b*c + c**(2)) + b*c*( b + c)))', ID="X_3500", classes=["center"])
    X_3501 = isogonal_conjugate(model, A, B, C, X_3500, ID="X_3501", classes=["selected", "target"])
    X_4 = orthocenter_of(model, A, B, C, ID="X_4", classes=["center", "incident"])
    X_9 = mittenpunkt_of(model, A, B, C, ID="X_9", classes=["center", "incident"])
    central_line(model, X_4, X_9, 4, 9, incident=True)
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center", "incident"])
    X_39 = eval_trilinear_point(model, A, B, C, 'a*(b**(2) + c**(2))', ID="X_39", classes=["center", "incident"])
    central_line(model, X_1, X_39, 1, 39, incident=True)
    X_41 = eval_trilinear_point(model, A, B, C, 'a**(2)*(b + c - a)', ID="X_41", classes=["center", "incident"])
    X_100 = eval_trilinear_point(model, A, B, C, '1/(b - c)', ID="X_100", classes=["center", "incident"])
    central_line(model, X_41, X_100, 41, 100, incident=True)
    return promote_point_to_top(model, X_3501)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3501 on the given reference triangle."""
    model = create_model('X_3501 = INTERSECTION OF LINES X_1X_39 AND X_4X_9')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03501(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03501.json"))
    write_center_svg(
        model_acute,
        here / "x-03501.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
