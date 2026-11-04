"""GEOMETOR construction model for X_1483 = REFLECTION OF X_5 IN X_1."""

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
    nagel_point_of,
    nine_point_center_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_01483(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1483 = REFLECTION OF X_5 IN X_1 on reference triangle ABC."""
    X_1483 = eval_trilinear_point(model, A, B, C, '(4*r - R*cos(B - C))', ID="X_1483", classes=["selected", "target"])
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center", "incident"])
    X_5 = nine_point_center_of(model, A, B, C, ID="X_5", classes=["center", "incident"])
    central_line(model, X_1, X_5, 1, 5, incident=True)
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center", "incident"])
    X_145 = eval_trilinear_point(model, A, B, C, 'b*c*(3*a - b - c)', ID="X_145", classes=["center", "incident"])
    central_line(model, X_3, X_145, 3, 145, incident=True)
    X_8 = nagel_point_of(model, A, B, C, ID="X_8", classes=["center", "incident"])
    X_140 = eval_trilinear_point(model, A, B, C, '2*cos(A) + cos(B - C)', ID="X_140", classes=["center", "incident"])
    central_line(model, X_8, X_140, 8, 140, incident=True)
    return promote_point_to_top(model, X_1483)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1483 on the given reference triangle."""
    model = create_model('X_1483 = REFLECTION OF X_5 IN X_1')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01483(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01483.json"))
    write_center_svg(
        model_acute,
        here / "x-01483.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
