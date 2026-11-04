"""GEOMETOR construction model for X_1050 = POINT ALGOL."""

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
    intersect_lines,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_01050(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1050 = POINT ALGOL on reference triangle ABC."""
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center"])
    X_341 = eval_trilinear_point(model, A, B, C, 'b**(2)*c**(2)*(b + c - a)**(2)', ID="X_341", classes=["center"])
    X_40 = eval_trilinear_point(model, A, B, C, 'cos(B) + cos(C) - cos(A) - 1', ID="X_40", classes=["center"])
    X_978 = eval_trilinear_point(model, A, B, C, 'a**(2)*(b + c) + a*(b**(2) - b*c + c**(2)) - b*c*(b + c)', ID="X_978", classes=["center"])
    central_line(model, X_1, X_341, 1, 341)
    central_line(model, X_40, X_978, 40, 978)
    X_1050 = intersect_lines(model, X_1, X_341, X_40, X_978, ID="X_1050", classes=["selected", "target"])
    return promote_point_to_top(model, X_1050)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1050 on the given reference triangle."""
    model = create_model('X_1050 = POINT ALGOL')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01050(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01050.json"))
    write_center_svg(
        model_acute,
        here / "x-01050.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
