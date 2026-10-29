"""GEOMETOR construction model for X(555) = (X(1),X(158))-ANSWER TO QUESTION A."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    gergonne_point_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00555(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(555) = (X(1),X(158))-ANSWER TO QUESTION A on reference triangle ABC."""
    X_555 = eval_trilinear_point(model, A, B, C, '(sec(A/2))**(3)', ID="X(555)", classes=["selected", "target"])
    X_7 = gergonne_point_of(model, A, B, C, ID="X(7)", classes=["center", "incident"])
    X_177 = eval_trilinear_point(model, A, B, C, '(cos(B/2) + cos(C/2))*sec(A/2)', ID="X(177)", classes=["center", "incident"])
    central_line(model, X_7, X_177, 7, 177, incident=True)
    return promote_point_to_top(model, X_555)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(555) on the given reference triangle."""
    model = create_model('X(555) = (X(1),X(158))-ANSWER TO QUESTION A')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00555(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00555.json"))
    write_center_svg(
        model_acute,
        here / "x-00555.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
