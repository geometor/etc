"""GEOMETOR construction model for X(135) = INTERSECTION OF LINE X(4)X(131) AND X(25)X(114)."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    orthocenter_of,
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00135(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(135) = INTERSECTION OF LINE X(4)X(131) AND X(25)X(114) on reference triangle ABC."""
    X_135 = eval_trilinear_point(model, A, B, C, '(sec(A))*((sin(2*B))/(sec(2*C) - sec(2*A)) + (sin(2*C))/(sec(2*A) - sec(2*B)))', ID="X(135)", classes=["selected", "target"])
    X_4 = orthocenter_of(model, A, B, C, ID="X(4)", classes=["center", "incident"])
    X_131 = point_from_barycentrics(model, A, B, C, 0.57236082, 0.12379803, 0.30384114, ID="X(131)", classes=["center", "incident"])
    central_line(model, X_4, X_131, 4, 131, incident=True)
    X_25 = eval_trilinear_point(model, A, B, C, 'sin(A)*tan(A)', ID="X(25)", classes=["center", "incident"])
    X_114 = point_from_barycentrics(model, A, B, C, 0.37082211, -0.060960354, 0.69013825, ID="X(114)", classes=["center", "incident"])
    central_line(model, X_25, X_114, 25, 114, incident=True)
    X_52 = eval_trilinear_point(model, A, B, C, 'cos(2*A)*cos(B - C)', ID="X(52)", classes=["center", "incident"])
    X_113 = eval_trilinear_point(model, A, B, C, 'sin(B)*sin(C)*((sin(C))/(cos(C) - 2*cos(A)*cos(B)) + (sin(B))/(cos(B) - 2*cos(A)*cos(C)))', ID="X(113)", classes=["center", "incident"])
    central_line(model, X_52, X_113, 52, 113, incident=True)
    return promote_point_to_top(model, X_135)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(135) on the given reference triangle."""
    model = create_model('X(135) = INTERSECTION OF LINE X(4)X(131) AND X(25)X(114)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00135(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00135.json"))
    write_center_svg(
        model_acute,
        here / "x-00135.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
