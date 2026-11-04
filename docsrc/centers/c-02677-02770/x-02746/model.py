"""GEOMETOR construction model for X_2746 = SR(X_104, X_111)."""

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
    point_from_barycentrics,
    promote_point_to_top,
    reflection_in_point,
)
from geometor.etc.render import write_center_svg


def construct_x_02746(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2746 = SR(X_104, X_111) on reference triangle ABC."""
    X_2721 = point_from_barycentrics(model, A, B, C, 0.60995165, -0.33022499, 0.72027334, ID="X_2721", classes=["center"])
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center"])
    X_2746 = reflection_in_point(model, X_2721, X_3, ID="X_2746", classes=["selected", "target"], guide=False)
    X_111 = eval_trilinear_point(model, A, B, C, 'a/(2*a**(2) - b**(2) - c**(2))', ID="X_111", classes=["center", "incident"])
    X_517 = eval_trilinear_point(model, A, B, C, '-1 + cos(B) + cos(C)', ID="X_517", classes=["center", "incident"])
    central_line(model, X_111, X_517, 111, 517, incident=True)
    X_104 = eval_trilinear_point(model, A, B, C, '1/(-1 + cos(B) + cos(C))', ID="X_104", classes=["center", "incident"])
    X_525 = eval_trilinear_point(model, A, B, C, '(b*cos(B) - c*cos(C))/a', ID="X_525", classes=["center", "incident"])
    central_line(model, X_104, X_525, 104, 525, incident=True)
    X_100 = eval_trilinear_point(model, A, B, C, '1/(b - c)', ID="X_100", classes=["center", "incident"])
    X_1499 = eval_trilinear_point(model, A, B, C, 'b*c*(b**(2) - c**(2))*(b**(2) + c**(2) - 5*a**(2))', ID="X_1499", classes=["center", "incident"])
    central_line(model, X_100, X_1499, 100, 1499, incident=True)
    return promote_point_to_top(model, X_2746)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2746 on the given reference triangle."""
    model = create_model('X_2746 = SR(X_104, X_111)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02746(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02746.json"))
    write_center_svg(
        model_acute,
        here / "x-02746.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
