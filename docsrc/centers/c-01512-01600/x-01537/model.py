"""GEOMETOR construction model for X_1537 = ORTHOJOIN OF X_44."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    feuerbach_point_of,
    gergonne_point_of,
    intersect_lines,
    orthocenter_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_01537(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1537 = ORTHOJOIN OF X_44 on reference triangle ABC."""
    X_11 = feuerbach_point_of(model, A, B, C, ID="X_11", classes=["center"])
    X_65 = eval_trilinear_point(model, A, B, C, 'cos(B) + cos(C)', ID="X_65", classes=["center"])
    X_7 = gergonne_point_of(model, A, B, C, ID="X_7", classes=["center"])
    X_104 = eval_trilinear_point(model, A, B, C, '1/(-1 + cos(B) + cos(C))', ID="X_104", classes=["center"])
    central_line(model, X_11, X_65, 11, 65)
    central_line(model, X_7, X_104, 7, 104)
    X_1537 = intersect_lines(model, X_11, X_65, X_7, X_104, ID="X_1537", classes=["selected", "target"])
    X_4 = orthocenter_of(model, A, B, C, ID="X_4", classes=["center", "incident"])
    X_145 = eval_trilinear_point(model, A, B, C, 'b*c*(3*a - b - c)', ID="X_145", classes=["center", "incident"])
    central_line(model, X_4, X_145, 4, 145, incident=True)
    return promote_point_to_top(model, X_1537)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1537 on the given reference triangle."""
    model = create_model('X_1537 = ORTHOJOIN OF X_44')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01537(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01537.json"))
    write_center_svg(
        model_acute,
        here / "x-01537.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
