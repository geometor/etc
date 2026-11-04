"""GEOMETOR construction model for X_1743 = MIMOSA TRANSFORM OF X_222."""

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
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_01743(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1743 = MIMOSA TRANSFORM OF X_222 on reference triangle ABC."""
    X_1743 = eval_trilinear_point(model, A, B, C, '3*a - b - c', ID="X_1743", classes=["selected", "target"])
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center", "incident"])
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center", "incident"])
    central_line(model, X_1, X_6, 1, 6, incident=True)
    X_43 = eval_trilinear_point(model, A, B, C, 'a*b + a*c - b*c', ID="X_43", classes=["center", "incident"])
    X_165 = eval_trilinear_point(model, A, B, C, 'tan(B/2) + tan(C/2) - tan(A/2)', ID="X_165", classes=["center", "incident"])
    central_line(model, X_43, X_165, 43, 165, incident=True)
    X_31 = eval_trilinear_point(model, A, B, C, 'a**(2)', ID="X_31", classes=["center", "incident"])
    X_200 = eval_trilinear_point(model, A, B, C, '(cot(A/2))**(2)', ID="X_200", classes=["center", "incident"])
    central_line(model, X_31, X_200, 31, 200, incident=True)
    return promote_point_to_top(model, X_1743)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1743 on the given reference triangle."""
    model = create_model('X_1743 = MIMOSA TRANSFORM OF X_222')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01743(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01743.json"))
    write_center_svg(
        model_acute,
        here / "x-01743.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
