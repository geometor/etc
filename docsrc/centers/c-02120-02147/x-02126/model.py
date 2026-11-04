"""GEOMETOR construction model for X_2126 = EIGENTRANSFORM OF X_10."""

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
    intersect_lines,
    nine_point_center_of,
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_02126(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2126 = EIGENTRANSFORM OF X_10 on reference triangle ABC."""
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center"])
    X_229 = point_from_barycentrics(model, A, B, C, 0.21061481, 0.29086323, 0.49852195, ID="X_229", classes=["center"])
    X_5 = nine_point_center_of(model, A, B, C, ID="X_5", classes=["center"])
    X_572 = eval_trilinear_point(model, A, B, C, '(cos(A - U))', ID="X_572", classes=["center"])
    central_line(model, X_1, X_229, 1, 229)
    central_line(model, X_5, X_572, 5, 572)
    X_2126 = intersect_lines(model, X_1, X_229, X_5, X_572, ID="X_2126", classes=["selected", "target"])
    X_49 = eval_trilinear_point(model, A, B, C, 'cos(3*A)', ID="X_49", classes=["center", "incident"])
    X_970 = eval_trilinear_point(model, A, B, C, 'a*(a**(3)*(b + c)**(2) + a*(a*b + a*c - 2*b*c)*(b**(2) + c**(2)) - b*c*(b**(3) + c**(3)) - a*(b**(4) + c**(4)) - (b**(5) + c**(5)))', ID="X_970", classes=["center", "incident"])
    central_line(model, X_49, X_970, 49, 970, incident=True)
    return promote_point_to_top(model, X_2126)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2126 on the given reference triangle."""
    model = create_model('X_2126 = EIGENTRANSFORM OF X_10')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02126(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02126.json"))
    write_center_svg(
        model_acute,
        here / "x-02126.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
