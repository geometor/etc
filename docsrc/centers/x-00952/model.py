"""GEOMETOR construction model for X(952) = INTERSECTION OF X(1)X(5) AND X(3)X(8)."""

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
    orthocenter_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00952(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(952) = INTERSECTION OF X(1)X(5) AND X(3)X(8) on reference triangle ABC."""
    X_952 = eval_trilinear_point(model, A, B, C, 'b*c*(2*a**(4) - 2*a**(3)*(b + c) - a**(2)*(b**(2) - 4*b*c + c**(2)) + (2*a - b - c)*(b - c)*(b**(2) - c**(2)))', ID="X(952)", classes=["selected", "target"])
    X_1 = incenter_of(model, A, B, C, ID="X(1)", classes=["center", "incident"])
    X_5 = nine_point_center_of(model, A, B, C, ID="X(5)", classes=["center", "incident"])
    central_line(model, X_1, X_5, 1, 5, incident=True)
    X_3 = circumcenter_of(model, A, B, C, ID="X(3)", classes=["center", "incident"])
    X_8 = nagel_point_of(model, A, B, C, ID="X(8)", classes=["center", "incident"])
    central_line(model, X_3, X_8, 3, 8, incident=True)
    X_4 = orthocenter_of(model, A, B, C, ID="X(4)", classes=["center", "incident"])
    X_145 = eval_trilinear_point(model, A, B, C, 'b*c*(3*a - b - c)', ID="X(145)", classes=["center", "incident"])
    central_line(model, X_4, X_145, 4, 145, incident=True)
    return promote_point_to_top(model, X_952)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(952) on the given reference triangle."""
    model = create_model('X(952) = INTERSECTION OF X(1)X(5) AND X(3)X(8)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00952(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00952.json"))
    write_center_svg(
        model_acute,
        here / "x-00952.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
