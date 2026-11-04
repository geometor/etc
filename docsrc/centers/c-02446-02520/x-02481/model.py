"""GEOMETOR construction model for X_2481 = INTERSECTION(FEUERBACH HYPERBOLA, STEINER CIRCUMELLIPSE)."""

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
    isogonal_conjugate,
    mittenpunkt_of,
    nagel_point_of,
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_02481(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2481 = INTERSECTION(FEUERBACH HYPERBOLA, STEINER CIRCUMELLIPSE) on reference triangle ABC."""
    X_2223 = point_from_barycentrics(model, A, B, C, -0.97809077, -0.16901408, 2.1471049, ID="X_2223", classes=["center"])
    X_2481 = isogonal_conjugate(model, A, B, C, X_2223, ID="X_2481", classes=["selected", "target"])
    X_8 = nagel_point_of(model, A, B, C, ID="X_8", classes=["center", "incident"])
    X_76 = eval_trilinear_point(model, A, B, C, '1/a**(3)', ID="X_76", classes=["center", "incident"])
    central_line(model, X_8, X_76, 8, 76, incident=True)
    X_9 = mittenpunkt_of(model, A, B, C, ID="X_9", classes=["center", "incident"])
    X_75 = eval_trilinear_point(model, A, B, C, '1/a**(2)', ID="X_75", classes=["center", "incident"])
    central_line(model, X_9, X_75, 9, 75, incident=True)
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center", "incident"])
    X_85 = eval_trilinear_point(model, A, B, C, 'b**(2)*c**(2)/(b + c - a)', ID="X_85", classes=["center", "incident"])
    central_line(model, X_1, X_85, 1, 85, incident=True)
    return promote_point_to_top(model, X_2481)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2481 on the given reference triangle."""
    model = create_model('X_2481 = INTERSECTION(FEUERBACH HYPERBOLA, STEINER CIRCUMELLIPSE)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02481(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02481.json"))
    write_center_svg(
        model_acute,
        here / "x-02481.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
