"""GEOMETOR construction model for X_3037 = COMPLEMENT OF X_1356."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    centroid_of,
    complement,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_03037(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3037 = COMPLEMENT OF X_1356 on reference triangle ABC."""
    X_1356 = point_from_barycentrics(model, A, B, C, 0.062797452, 0.59175443, 0.34544811, ID="X_1356", classes=["center"])
    X_3037 = complement(model, A, B, C, X_1356, ID="X_3037", classes=["selected", "target"])
    X_2 = centroid_of(model, A, B, C, ID="X_2", classes=["center", "incident"])
    central_line(model, X_2, X_1356, 2, 1356, incident=True)
    X_741 = eval_trilinear_point(model, A, B, C, '(1/(a **(-2)*(b**(1) + c**(1)) - a**(0)*(b **(-1) + c **(-1))))', ID="X_741", classes=["center", "incident"])
    X_958 = eval_trilinear_point(model, A, B, C, '(b + c - a)*(a**(2) + a*b + a*c + 2*b*c)', ID="X_958", classes=["center", "incident"])
    central_line(model, X_741, X_958, 741, 958, incident=True)
    return promote_point_to_top(model, X_3037)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3037 on the given reference triangle."""
    model = create_model('X_3037 = COMPLEMENT OF X_1356')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03037(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03037.json"))
    write_center_svg(
        model_acute,
        here / "x-03037.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
