"""GEOMETOR construction model for X(617) = ANTICOMPLEMENT OF X(14)."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    anticomplement,
    central_line,
    centroid_of,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00617(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(617) = ANTICOMPLEMENT OF X(14) on reference triangle ABC."""
    X_14 = eval_trilinear_point(model, A, B, C, 'csc(A - pi /3)', ID="X(14)", classes=["center"])
    X_617 = anticomplement(model, A, B, C, X_14, ID="X(617)", classes=["selected", "target"])
    X_2 = centroid_of(model, A, B, C, ID="X(2)", classes=["center", "incident"])
    central_line(model, X_2, X_14, 2, 14, incident=True)
    X_69 = eval_trilinear_point(model, A, B, C, '(cos(A))/a**(2)', ID="X(69)", classes=["center", "incident"])
    X_74 = eval_trilinear_point(model, A, B, C, '1/(cos(A) - 2*cos(B)*cos(C))', ID="X(74)", classes=["center", "incident"])
    central_line(model, X_69, X_74, 69, 74, incident=True)
    X_13 = eval_trilinear_point(model, A, B, C, 'csc(A + pi /3)', ID="X(13)", classes=["center", "incident"])
    X_148 = eval_trilinear_point(model, A, B, C, 'b*c*(a**(4) - (b**(2) - c**(2))**(2) + b**(2)*c**(2) - a**(2)*b**(2) - a**(2)*c**(2))', ID="X(148)", classes=["center", "incident"])
    central_line(model, X_13, X_148, 13, 148, incident=True)
    return promote_point_to_top(model, X_617)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(617) on the given reference triangle."""
    model = create_model('X(617) = ANTICOMPLEMENT OF X(14)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00617(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00617.json"))
    write_center_svg(
        model_acute,
        here / "x-00617.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
