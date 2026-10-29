"""GEOMETOR construction model for X(74) = ISOGONAL CONJUGATE OF EULER INFINITY POINT."""

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
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00074(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(74) = ISOGONAL CONJUGATE OF EULER INFINITY POINT on reference triangle ABC."""
    X_30 = eval_trilinear_point(model, A, B, C, 'cos(A) - 2*cos(B)*cos(C)', ID="X(30)", classes=["center"])
    X_74 = isogonal_conjugate(model, A, B, C, X_30, ID="X(74)", classes=["selected", "target"])
    X_20 = eval_trilinear_point(model, A, B, C, 'cos(A) - cos(B)*cos(C)', ID="X(20)", classes=["center", "incident"])
    X_68 = eval_trilinear_point(model, A, B, C, 'cos(A)*sec(2*A)', ID="X(68)", classes=["center", "incident"])
    central_line(model, X_20, X_68, 20, 68, incident=True)
    X_24 = eval_trilinear_point(model, A, B, C, 'sec(A)*cos(2*A)', ID="X(24)", classes=["center", "incident"])
    X_64 = eval_trilinear_point(model, A, B, C, '1/(cos(A) - cos(B)*cos(C))', ID="X(64)", classes=["center", "incident"])
    central_line(model, X_24, X_64, 24, 64, incident=True)
    X_35 = eval_trilinear_point(model, A, B, C, '1 + 2*cos(A)', ID="X(35)", classes=["center", "incident"])
    X_73 = eval_trilinear_point(model, A, B, C, 'sec(B) + sec(C)', ID="X(73)", classes=["center", "incident"])
    central_line(model, X_35, X_73, 35, 73, incident=True)
    return promote_point_to_top(model, X_74)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(74) on the given reference triangle."""
    model = create_model('X(74) = ISOGONAL CONJUGATE OF EULER INFINITY POINT')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00074(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00074.json"))
    write_center_svg(
        model_acute,
        here / "x-00074.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
