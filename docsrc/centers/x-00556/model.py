"""GEOMETOR construction model for X(556) = (X(1),X(75))-ANSWER TO QUESTION A."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    isotomic_conjugate,
    nagel_point_of,
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00556(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(556) = (X(1),X(75))-ANSWER TO QUESTION A on reference triangle ABC."""
    X_174 = eval_trilinear_point(model, A, B, C, 'sec(A/2)', ID="X(174)", classes=["center"])
    X_556 = isotomic_conjugate(model, A, B, C, X_174, ID="X(556)", classes=["selected", "target"])
    X_8 = nagel_point_of(model, A, B, C, ID="X(8)", classes=["center", "incident"])
    X_177 = eval_trilinear_point(model, A, B, C, '(cos(B/2) + cos(C/2))*sec(A/2)', ID="X(177)", classes=["center", "incident"])
    central_line(model, X_8, X_177, 8, 177, incident=True)
    X_75 = eval_trilinear_point(model, A, B, C, '1/a**(2)', ID="X(75)", classes=["center", "incident"])
    X_234 = point_from_barycentrics(model, A, B, C, 0.21955649, 0.30115636, 0.47928715, ID="X(234)", classes=["center", "incident"])
    central_line(model, X_75, X_234, 75, 234, incident=True)
    return promote_point_to_top(model, X_556)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(556) on the given reference triangle."""
    model = create_model('X(556) = (X(1),X(75))-ANSWER TO QUESTION A')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00556(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00556.json"))
    write_center_svg(
        model_acute,
        here / "x-00556.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
