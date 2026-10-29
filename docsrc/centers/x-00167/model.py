"""GEOMETOR construction model for X(167) = NAGEL POINT OF EXCENTRAL TRIANGLE."""

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
    intersect_lines,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00167(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(167) = NAGEL POINT OF EXCENTRAL TRIANGLE on reference triangle ABC."""
    X_164 = eval_trilinear_point(model, A, B, C, 'sin(B/2) + sin(C/2) - sin(A/2)', ID="X(164)", classes=["center"])
    X_165 = eval_trilinear_point(model, A, B, C, 'tan(B/2) + tan(C/2) - tan(A/2)', ID="X(165)", classes=["center"])
    X_1 = incenter_of(model, A, B, C, ID="X(1)", classes=["center"])
    X_174 = eval_trilinear_point(model, A, B, C, 'sec(A/2)', ID="X(174)", classes=["center"])
    central_line(model, X_164, X_165, 164, 165)
    central_line(model, X_1, X_174, 1, 174)
    X_167 = intersect_lines(model, X_164, X_165, X_1, X_174, ID="X(167)", classes=["selected", "target"])
    X_166 = eval_trilinear_point(model, A, B, C, '(tan(A/2))/(cos(B/2) + cos(C/2) - cos(A/2)) - (tan(B/2))/(cos(C/2) + cos(A/2) - cos(B/2)) - (tan(C/2))/(cos(A/2) + cos(B/2) - cos(C/2))', ID="X(166)", classes=["center", "incident"])
    X_188 = eval_trilinear_point(model, A, B, C, 'csc(A/2)', ID="X(188)", classes=["center", "incident"])
    central_line(model, X_166, X_188, 166, 188, incident=True)
    return promote_point_to_top(model, X_167)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(167) on the given reference triangle."""
    model = create_model('X(167) = NAGEL POINT OF EXCENTRAL TRIANGLE')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00167(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00167.json"))
    write_center_svg(
        model_acute,
        here / "x-00167.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
