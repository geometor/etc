"""GEOMETOR construction model for X(678) = CROSSPOINT OF X(1) AND X(44)."""

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


def construct_x_00678(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(678) = CROSSPOINT OF X(1) AND X(44) on reference triangle ABC."""
    X_1 = incenter_of(model, A, B, C, ID="X(1)", classes=["center"])
    X_88 = eval_trilinear_point(model, A, B, C, '1/(b + c - 2*a)', ID="X(88)", classes=["center"])
    X_45 = eval_trilinear_point(model, A, B, C, '2*b + 2*c - a', ID="X(45)", classes=["center"])
    X_55 = eval_trilinear_point(model, A, B, C, 'a*(b + c - a)', ID="X(55)", classes=["center"])
    central_line(model, X_1, X_88, 1, 88)
    central_line(model, X_45, X_55, 45, 55)
    X_678 = intersect_lines(model, X_1, X_88, X_45, X_55, ID="X(678)", classes=["selected", "target"])
    X_44 = eval_trilinear_point(model, A, B, C, 'b + c - 2*a', ID="X(44)", classes=["center", "incident"])
    X_902 = eval_trilinear_point(model, A, B, C, 'a*(b + c - 2*a)', ID="X(902)", classes=["center", "incident"])
    central_line(model, X_44, X_902, 44, 902, incident=True)
    return promote_point_to_top(model, X_678)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(678) on the given reference triangle."""
    model = create_model('X(678) = CROSSPOINT OF X(1) AND X(44)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00678(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00678.json"))
    write_center_svg(
        model_acute,
        here / "x-00678.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
