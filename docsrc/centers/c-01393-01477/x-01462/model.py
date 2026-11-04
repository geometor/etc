"""GEOMETOR construction model for X_1462 = X_673-BETH CONJUGATE OF X_673."""

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
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_01462(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1462 = X_673-BETH CONJUGATE OF X_673 on reference triangle ABC."""
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center"])
    X_7 = gergonne_point_of(model, A, B, C, ID="X_7", classes=["center"])
    X_31 = eval_trilinear_point(model, A, B, C, 'a**(2)', ID="X_31", classes=["center"])
    X_57 = eval_trilinear_point(model, A, B, C, '1/(b + c - a)', ID="X_57", classes=["center"])
    central_line(model, X_6, X_7, 6, 7)
    central_line(model, X_31, X_57, 31, 57)
    X_1462 = intersect_lines(model, X_6, X_7, X_31, X_57, ID="X_1462", classes=["selected", "target"])
    X_269 = eval_trilinear_point(model, A, B, C, '(tan(A/2))**(2)', ID="X_269", classes=["center", "incident"])
    X_604 = eval_trilinear_point(model, A, B, C, 'a*(1 - cos(A))', ID="X_604", classes=["center", "incident"])
    central_line(model, X_269, X_604, 269, 604, incident=True)
    return promote_point_to_top(model, X_1462)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1462 on the given reference triangle."""
    model = create_model('X_1462 = X_673-BETH CONJUGATE OF X_673')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01462(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01462.json"))
    write_center_svg(
        model_acute,
        here / "x-01462.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
