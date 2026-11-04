"""GEOMETOR construction model for X_2358 = X_2-ISOCONJUGATE OF X_1819."""

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
    intersect_lines,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_02358(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2358 = X_2-ISOCONJUGATE OF X_1819 on reference triangle ABC."""
    X_19 = eval_trilinear_point(model, A, B, C, 'tan(A)', ID="X_19", classes=["center"])
    X_56 = eval_trilinear_point(model, A, B, C, 'a/(b + c - a)', ID="X_56", classes=["center"])
    X_7 = gergonne_point_of(model, A, B, C, ID="X_7", classes=["center"])
    X_92 = eval_trilinear_point(model, A, B, C, 'csc(2*A)', ID="X_92", classes=["center"])
    central_line(model, X_19, X_56, 19, 56)
    central_line(model, X_7, X_92, 7, 92)
    X_2358 = intersect_lines(model, X_19, X_56, X_7, X_92, ID="X_2358", classes=["selected", "target"])
    X_608 = eval_trilinear_point(model, A, B, C, 'a*(1 - sec(A))', ID="X_608", classes=["center", "incident"])
    X_1096 = eval_trilinear_point(model, A, B, C, '((tan(A))**(2))', ID="X_1096", classes=["center", "incident"])
    central_line(model, X_608, X_1096, 608, 1096, incident=True)
    return promote_point_to_top(model, X_2358)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2358 on the given reference triangle."""
    model = create_model('X_2358 = X_2-ISOCONJUGATE OF X_1819')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02358(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02358.json"))
    write_center_svg(
        model_acute,
        here / "x-02358.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
