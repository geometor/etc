"""GEOMETOR construction model for X(363) = EQUAL PERIMETERS ISOSCELIZER POINT."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    incenter_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00363(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(363) = EQUAL PERIMETERS ISOSCELIZER POINT on reference triangle ABC."""
    X_363 = eval_trilinear_point(model, A, B, C, 'b/(1 + sin(B/2)) + c/(1 + sin(C/2)) - a/(1 + sin(A/2))', ID="X(363)", classes=["selected", "target"])
    X_40 = eval_trilinear_point(model, A, B, C, 'cos(B) + cos(C) - cos(A) - 1', ID="X(40)", classes=["center", "incident"])
    X_164 = eval_trilinear_point(model, A, B, C, 'sin(B/2) + sin(C/2) - sin(A/2)', ID="X(164)", classes=["center", "incident"])
    central_line(model, X_40, X_164, 40, 164, incident=True)
    X_1 = incenter_of(model, A, B, C, ID="X(1)", classes=["center", "incident"])
    X_289 = eval_trilinear_point(model, A, B, C, '(sin(A/2))/(cos(B/2) + cos(C/2) - cos(A/2))', ID="X(289)", classes=["center", "incident"])
    central_line(model, X_1, X_289, 1, 289, incident=True)
    X_165 = eval_trilinear_point(model, A, B, C, 'tan(B/2) + tan(C/2) - tan(A/2)', ID="X(165)", classes=["center", "incident"])
    X_166 = eval_trilinear_point(model, A, B, C, '(tan(A/2))/(cos(B/2) + cos(C/2) - cos(A/2)) - (tan(B/2))/(cos(C/2) + cos(A/2) - cos(B/2)) - (tan(C/2))/(cos(A/2) + cos(B/2) - cos(C/2))', ID="X(166)", classes=["center", "incident"])
    central_line(model, X_165, X_166, 165, 166, incident=True)
    return promote_point_to_top(model, X_363)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(363) on the given reference triangle."""
    model = create_model('X(363) = EQUAL PERIMETERS ISOSCELIZER POINT')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00363(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00363.json"))
    write_center_svg(
        model_acute,
        here / "x-00363.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
