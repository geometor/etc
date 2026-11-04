"""GEOMETOR construction model for X_481 = 1st EPPSTEIN POINT."""

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
    incenter_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00481(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_481 = 1st EPPSTEIN POINT on reference triangle ABC."""
    X_481 = eval_trilinear_point(model, A, B, C, '1 - 2*sec(A/2)*cos(B/2)*cos(C/2)', ID="X_481", classes=["selected", "target"])
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center", "incident"])
    X_7 = gergonne_point_of(model, A, B, C, ID="X_7", classes=["center", "incident"])
    central_line(model, X_1, X_7, 1, 7, incident=True)
    X_226 = eval_trilinear_point(model, A, B, C, '(csc(A))*(cos(B) + cos(C))', ID="X_226", classes=["center", "incident"])
    X_485 = eval_trilinear_point(model, A, B, C, 'sec(A - pi /4)', ID="X_485", classes=["center", "incident"])
    central_line(model, X_226, X_485, 226, 485, incident=True)
    X_174 = eval_trilinear_point(model, A, B, C, 'sec(A/2)', ID="X_174", classes=["center", "incident"])
    X_1127 = eval_trilinear_point(model, A, B, C, '(sin(A/4))/sin(3*A/4)', ID="X_1127", classes=["center", "incident"])
    central_line(model, X_174, X_1127, 174, 1127, incident=True)
    return promote_point_to_top(model, X_481)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_481 on the given reference triangle."""
    model = create_model('X_481 = 1st EPPSTEIN POINT')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00481(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00481.json"))
    write_center_svg(
        model_acute,
        here / "x-00481.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
