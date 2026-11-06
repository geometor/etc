"""GEOMETOR construction model for X_3238 = INTERSECTION OF LINES X_1X_256 and X_3X_1672."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    circumcenter_of,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    incenter_of,
    promote_point_to_top,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_03238(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3238 = INTERSECTION OF LINES X_1X_256 and X_3X_1672 on reference triangle ABC."""
    X_3238 = eval_trilinear_point(model, A, B, C, '(1 - cos(A +  omega  ))', ID="X_3238", classes=["selected", "target"])
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center", "incident"])
    X_256 = eval_trilinear_point(model, A, B, C, '1/(a**(2) + b*c)', ID="X_256", classes=["center", "incident"])
    central_line(model, X_1, X_256, 1, 256, incident=True)
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center", "incident"])
    X_1672 = eval_trilinear_point(model, A, B, C, '1 + cos(A -  omega  )', ID="X_1672", classes=["center", "incident"])
    central_line(model, X_3, X_1672, 3, 1672, incident=True)
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center", "incident"])
    X_1673 = eval_trilinear_point(model, A, B, C, '1 - cos(A -  omega  )', ID="X_1673", classes=["center", "incident"])
    central_line(model, X_6, X_1673, 6, 1673, incident=True)
    return promote_point_to_top(model, X_3238)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3238 on the given reference triangle."""
    model = create_model('X_3238 = INTERSECTION OF LINES X_1X_256 and X_3X_1672')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03238(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03238.json"))
    write_center_svg(
        model_acute,
        here / "x-03238.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
