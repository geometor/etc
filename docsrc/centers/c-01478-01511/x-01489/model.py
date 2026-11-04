"""GEOMETOR construction model for X_1489 = 3rd STEVANOVIC POINT."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    complement,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    incenter_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_01489(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1489 = 3rd STEVANOVIC POINT on reference triangle ABC."""
    X_1143 = eval_trilinear_point(model, A, B, C, 'csc(A)*tan(A/4)', ID="X_1143", classes=["center"])
    X_1489 = complement(model, A, B, C, X_1143, ID="X_1489", classes=["selected", "target"])
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center", "incident"])
    X_188 = eval_trilinear_point(model, A, B, C, 'csc(A/2)', ID="X_188", classes=["center", "incident"])
    central_line(model, X_1, X_188, 1, 188, incident=True)
    X_174 = eval_trilinear_point(model, A, B, C, 'sec(A/2)', ID="X_174", classes=["center", "incident"])
    X_558 = eval_trilinear_point(model, A, B, C, 'sec(A/2)*tan(A/4)', ID="X_558", classes=["center", "incident"])
    central_line(model, X_174, X_558, 174, 558, incident=True)
    X_258 = eval_trilinear_point(model, A, B, C, '1/(cos(B/2) + cos(C/2) - cos(A/2))', ID="X_258", classes=["center", "incident"])
    X_483 = eval_trilinear_point(model, A, B, C, '(sec(A/4))**(2)', ID="X_483", classes=["center", "incident"])
    central_line(model, X_258, X_483, 258, 483, incident=True)
    return promote_point_to_top(model, X_1489)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1489 on the given reference triangle."""
    model = create_model('X_1489 = 3rd STEVANOVIC POINT')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01489(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01489.json"))
    write_center_svg(
        model_acute,
        here / "x-01489.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
