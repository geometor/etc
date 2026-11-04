"""GEOMETOR construction model for X_1361 = BRISSE TRANSFORM OF X_104."""

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
    intersect_lines,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_01361(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1361 = BRISSE TRANSFORM OF X_104 on reference triangle ABC."""
    X_11 = feuerbach_point_of(model, A, B, C, ID="X_11", classes=["center"])
    X_65 = eval_trilinear_point(model, A, B, C, 'cos(B) + cos(C)', ID="X_65", classes=["center"])
    X_12 = eval_trilinear_point(model, A, B, C, '1 + cos(B - C)', ID="X_12", classes=["center"])
    X_124 = eval_trilinear_point(model, A, B, C, '(b*c*(b + c - a)*(b - c)**(2)*((b + c)*(b**(2) + c**(2) - a**(2) - b*c) + a*b*c))', ID="X_124", classes=["center"])
    central_line(model, X_11, X_65, 11, 65)
    central_line(model, X_12, X_124, 12, 124)
    X_1361 = intersect_lines(model, X_11, X_65, X_12, X_124, ID="X_1361", classes=["selected", "target"])
    X_55 = eval_trilinear_point(model, A, B, C, 'a*(b + c - a)', ID="X_55", classes=["center", "incident"])
    X_102 = eval_trilinear_point(model, A, B, C, '1/(sin(B)*(sec(A) - sec(B)) + sin(C)*(sec(A) - sec(C)))', ID="X_102", classes=["center", "incident"])
    central_line(model, X_55, X_102, 55, 102, incident=True)
    return promote_point_to_top(model, X_1361)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1361 on the given reference triangle."""
    model = create_model('X_1361 = BRISSE TRANSFORM OF X_104')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01361(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01361.json"))
    write_center_svg(
        model_acute,
        here / "x-01361.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
