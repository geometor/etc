"""GEOMETOR construction model for X(872) = INTERSECTION OF LINES X(37)X(42) AND X(43)X(75)."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    promote_point_to_top,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_00872(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(872) = INTERSECTION OF LINES X(37)X(42) AND X(43)X(75) on reference triangle ABC."""
    X_872 = eval_trilinear_point(model, A, B, C, '(a*(b + c))**(2)', ID="X(872)", classes=["selected", "target"])
    X_37 = eval_trilinear_point(model, A, B, C, 'b + c', ID="X(37)", classes=["center", "incident"])
    X_42 = eval_trilinear_point(model, A, B, C, 'a*(b + c)', ID="X(42)", classes=["center", "incident"])
    central_line(model, X_37, X_42, 37, 42, incident=True)
    X_43 = eval_trilinear_point(model, A, B, C, 'a*b + a*c - b*c', ID="X(43)", classes=["center", "incident"])
    X_75 = eval_trilinear_point(model, A, B, C, '1/a**(2)', ID="X(75)", classes=["center", "incident"])
    central_line(model, X_43, X_75, 43, 75, incident=True)
    X_6 = symmedian_point_of(model, A, B, C, ID="X(6)", classes=["center", "incident"])
    X_292 = eval_trilinear_point(model, A, B, C, 'a/(a**(2) - b*c)', ID="X(292)", classes=["center", "incident"])
    central_line(model, X_6, X_292, 6, 292, incident=True)
    return promote_point_to_top(model, X_872)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(872) on the given reference triangle."""
    model = create_model('X(872) = INTERSECTION OF LINES X(37)X(42) AND X(43)X(75)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00872(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00872.json"))
    write_center_svg(
        model_acute,
        here / "x-00872.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
