"""GEOMETOR construction model for X_1945 = TRILINEAR POLE OF PU(18)."""

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


def construct_x_01945(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1945 = TRILINEAR POLE OF PU(18) on reference triangle ABC."""
    X_1944 = eval_trilinear_point(model, A, B, C, '(b*c*((cos(A))**(2) - cos(B)*cos(C)))', ID="X_1944", classes=["center"])
    X_1945 = isogonal_conjugate(model, A, B, C, X_1944, ID="X_1945", classes=["selected", "target"])
    X_109 = eval_trilinear_point(model, A, B, C, 'a/(cos(B) - cos(C))', ID="X_109", classes=["center", "incident"])
    X_284 = eval_trilinear_point(model, A, B, C, '(sin(A))/(cos(B) + cos(C))', ID="X_284", classes=["center", "incident"])
    central_line(model, X_109, X_284, 109, 284, incident=True)
    X_19 = eval_trilinear_point(model, A, B, C, 'tan(A)', ID="X_19", classes=["center", "incident"])
    X_800 = eval_trilinear_point(model, A, B, C, 'sin(A)*((cos(B))**(2) + (cos(C))**(2))', ID="X_800", classes=["center", "incident"])
    central_line(model, X_19, X_800, 19, 800, incident=True)
    X_333 = eval_trilinear_point(model, A, B, C, 'b*c*(b + c - a)/(b + c)', ID="X_333", classes=["center", "incident"])
    X_664 = eval_trilinear_point(model, A, B, C, '1/(a*(b - c)*(b + c - a))', ID="X_664", classes=["center", "incident"])
    central_line(model, X_333, X_664, 333, 664, incident=True)
    return promote_point_to_top(model, X_1945)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1945 on the given reference triangle."""
    model = create_model('X_1945 = TRILINEAR POLE OF PU(18)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01945(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01945.json"))
    write_center_svg(
        model_acute,
        here / "x-01945.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
