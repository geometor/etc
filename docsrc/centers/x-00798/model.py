"""GEOMETOR construction model for X(798) = CROSSDIFFERENCE OF X(1) AND X(75)."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00798(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(798) = CROSSDIFFERENCE OF X(1) AND X(75) on reference triangle ABC."""
    X_798 = eval_trilinear_point(model, A, B, C, 'a**(2)*(b**(2) - c**(2))', ID="X(798)", classes=["selected", "target"])
    X_44 = eval_trilinear_point(model, A, B, C, 'b + c - 2*a', ID="X(44)", classes=["center", "incident"])
    X_513 = eval_trilinear_point(model, A, B, C, 'b - c', ID="X(513)", classes=["center", "incident"])
    central_line(model, X_44, X_513, 44, 513, incident=True)
    X_667 = eval_trilinear_point(model, A, B, C, 'a**(2)*(b - c)', ID="X(667)", classes=["center", "incident"])
    X_788 = eval_trilinear_point(model, A, B, C, 'a**(2)*(b**(3) - c**(3))', ID="X(788)", classes=["center", "incident"])
    central_line(model, X_667, X_788, 667, 788, incident=True)
    X_688 = point_from_barycentrics(model, A, B, C, 0.2387104, -0.79556745, 0.55685705, ID="X(688)", classes=["center", "incident"])
    X_872 = eval_trilinear_point(model, A, B, C, '(a*(b + c))**(2)', ID="X(872)", classes=["center", "incident"])
    central_line(model, X_688, X_872, 688, 872, incident=True)
    return promote_point_to_top(model, X_798)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(798) on the given reference triangle."""
    model = create_model('X(798) = CROSSDIFFERENCE OF X(1) AND X(75)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00798(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00798.json"))
    write_center_svg(
        model_acute,
        here / "x-00798.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
