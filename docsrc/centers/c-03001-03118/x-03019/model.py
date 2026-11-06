"""GEOMETOR construction model for X_3019 = (SODDY LINE)∩(FERMAT AXIS)."""

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
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_03019(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3019 = (SODDY LINE)∩(FERMAT AXIS) on reference triangle ABC."""
    X_3019 = eval_trilinear_point(model, A, B, C, '(sin(A - C)*(1 + 2*cos(2*B))*((sec(A/2))**(2) -(sec(B/2))**(2)) + sin(A - B)*(1 + 2*cos(2*C))*((sec(A/2))**(2) -(sec(C/2))**(2)))', ID="X_3019", classes=["selected", "target"])
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center", "incident"])
    X_7 = gergonne_point_of(model, A, B, C, ID="X_7", classes=["center", "incident"])
    central_line(model, X_1, X_7, 1, 7, incident=True)
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center", "incident"])
    X_13 = eval_trilinear_point(model, A, B, C, 'csc(A +  pi  /3)', ID="X_13", classes=["center", "incident"])
    central_line(model, X_6, X_13, 6, 13, incident=True)
    return promote_point_to_top(model, X_3019)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3019 on the given reference triangle."""
    model = create_model('X_3019 = (SODDY LINE)∩(FERMAT AXIS)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03019(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03019.json"))
    write_center_svg(
        model_acute,
        here / "x-03019.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
