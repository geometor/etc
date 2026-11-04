"""GEOMETOR construction model for X_1950 = CROSSSUM OF PU(20)."""

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
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_01950(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1950 = CROSSSUM OF PU(20) on reference triangle ABC."""
    X_1950 = eval_trilinear_point(model, A, B, C, 'a*((cos(A))**(2) + cos(B)*cos(C))', ID="X_1950", classes=["selected", "target"])
    X_109 = eval_trilinear_point(model, A, B, C, 'a/(cos(B) - cos(C))', ID="X_109", classes=["center", "incident"])
    X_284 = eval_trilinear_point(model, A, B, C, '(sin(A))/(cos(B) + cos(C))', ID="X_284", classes=["center", "incident"])
    central_line(model, X_109, X_284, 109, 284, incident=True)
    X_19 = eval_trilinear_point(model, A, B, C, 'tan(A)', ID="X_19", classes=["center", "incident"])
    X_577 = eval_trilinear_point(model, A, B, C, 'sin(A)*(cos(A))**(2)', ID="X_577", classes=["center", "incident"])
    central_line(model, X_19, X_577, 19, 577, incident=True)
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center", "incident"])
    X_608 = eval_trilinear_point(model, A, B, C, 'a*(1 - sec(A))', ID="X_608", classes=["center", "incident"])
    central_line(model, X_3, X_608, 3, 608, incident=True)
    return promote_point_to_top(model, X_1950)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1950 on the given reference triangle."""
    model = create_model('X_1950 = CROSSSUM OF PU(20)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01950(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01950.json"))
    write_center_svg(
        model_acute,
        here / "x-01950.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
