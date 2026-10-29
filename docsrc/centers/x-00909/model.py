"""GEOMETOR construction model for X(909) = POINT ADHAFERA."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_barycentric_point,
    eval_trilinear_point,
    isogonal_conjugate,
    mittenpunkt_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00909(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(909) = POINT ADHAFERA on reference triangle ABC."""
    X_908 = eval_barycentric_point(model, A, B, C, 'cos(B) + cos(C) - 1', ID="X(908)", classes=["center"])
    X_909 = isogonal_conjugate(model, A, B, C, X_908, ID="X(909)", classes=["selected", "target"])
    X_9 = mittenpunkt_of(model, A, B, C, ID="X(9)", classes=["center", "incident"])
    X_48 = eval_trilinear_point(model, A, B, C, 'tan(B) + tan(C)', ID="X(48)", classes=["center", "incident"])
    central_line(model, X_9, X_48, 9, 48, incident=True)
    X_55 = eval_trilinear_point(model, A, B, C, 'a*(b + c - a)', ID="X(55)", classes=["center", "incident"])
    X_184 = eval_trilinear_point(model, A, B, C, 'a**(2)*cos(A)', ID="X(184)", classes=["center", "incident"])
    central_line(model, X_55, X_184, 55, 184, incident=True)
    X_163 = eval_trilinear_point(model, A, B, C, '(sin(2*A))/(sin(2*B) - sin(2*C))', ID="X(163)", classes=["center", "incident"])
    X_284 = eval_trilinear_point(model, A, B, C, '(sin(A))/(cos(B) + cos(C))', ID="X(284)", classes=["center", "incident"])
    central_line(model, X_163, X_284, 163, 284, incident=True)
    return promote_point_to_top(model, X_909)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(909) on the given reference triangle."""
    model = create_model('X(909) = POINT ADHAFERA')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00909(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00909.json"))
    write_center_svg(
        model_acute,
        here / "x-00909.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
