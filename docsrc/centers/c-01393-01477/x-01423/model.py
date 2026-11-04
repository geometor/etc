"""GEOMETOR construction model for X_1423 = X_192-BETH CONJUGATE OF X_192."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    centroid_of,
    ceva_conjugate,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    gergonne_point_of,
    incenter_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_01423(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1423 = X_192-BETH CONJUGATE OF X_192 on reference triangle ABC."""
    X_56 = eval_trilinear_point(model, A, B, C, 'a/(b + c - a)', ID="X_56", classes=["center"])
    X_57 = eval_trilinear_point(model, A, B, C, '1/(b + c - a)', ID="X_57", classes=["center"])
    X_1423 = ceva_conjugate(model, A, B, C, X_56, X_57, ID="X_1423", classes=["selected", "target"])
    X_2 = centroid_of(model, A, B, C, ID="X_2", classes=["center", "incident"])
    X_7 = gergonne_point_of(model, A, B, C, ID="X_7", classes=["center", "incident"])
    central_line(model, X_2, X_7, 2, 7, incident=True)
    X_87 = eval_trilinear_point(model, A, B, C, '1/(a*b + a*c - b*c)', ID="X_87", classes=["center", "incident"])
    central_line(model, X_56, X_87, 56, 87, incident=True)
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center", "incident"])
    X_256 = eval_trilinear_point(model, A, B, C, '1/(a**(2) + b*c)', ID="X_256", classes=["center", "incident"])
    central_line(model, X_1, X_256, 1, 256, incident=True)
    return promote_point_to_top(model, X_1423)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1423 on the given reference triangle."""
    model = create_model('X_1423 = X_192-BETH CONJUGATE OF X_192')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01423(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01423.json"))
    write_center_svg(
        model_acute,
        here / "x-01423.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
