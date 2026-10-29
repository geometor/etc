"""GEOMETOR construction model for X(480) = X(200)-CEVA CONJUGATE OF X(220)."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    isogonal_conjugate,
    mittenpunkt_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00480(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(480) = X(200)-CEVA CONJUGATE OF X(220) on reference triangle ABC."""
    X_479 = eval_trilinear_point(model, A, B, C, '(tan(A/2)*sec(A/2))**(2)', ID="X(479)", classes=["center"])
    X_480 = isogonal_conjugate(model, A, B, C, X_479, ID="X(480)", classes=["selected", "target"])
    X_9 = mittenpunkt_of(model, A, B, C, ID="X(9)", classes=["center", "incident"])
    X_55 = eval_trilinear_point(model, A, B, C, 'a*(b + c - a)', ID="X(55)", classes=["center", "incident"])
    central_line(model, X_9, X_55, 9, 55, incident=True)
    X_56 = eval_trilinear_point(model, A, B, C, 'a/(b + c - a)', ID="X(56)", classes=["center", "incident"])
    X_78 = eval_trilinear_point(model, A, B, C, '1/(1 - sec(A))', ID="X(78)", classes=["center", "incident"])
    central_line(model, X_56, X_78, 56, 78, incident=True)
    X_100 = eval_trilinear_point(model, A, B, C, '1/(b - c)', ID="X(100)", classes=["center", "incident"])
    X_144 = eval_trilinear_point(model, A, B, C, '(csc(A))*(tan(B/2) + tan(C/2) - tan(A/2))', ID="X(144)", classes=["center", "incident"])
    central_line(model, X_100, X_144, 100, 144, incident=True)
    return promote_point_to_top(model, X_480)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(480) on the given reference triangle."""
    model = create_model('X(480) = X(200)-CEVA CONJUGATE OF X(220)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00480(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00480.json"))
    write_center_svg(
        model_acute,
        here / "x-00480.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
