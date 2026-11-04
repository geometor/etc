"""GEOMETOR construction model for X_2709 = SR(X_98, X_111)."""

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


def construct_x_02709(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2709 = SR(X_98, X_111) on reference triangle ABC."""
    X_843 = point_from_barycentrics(model, A, B, C, 0.47728091, -0.17542584, 0.69814493, ID="X_843", classes=["center"])
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center"])
    X_2709 = reflection_in_point(model, X_843, X_3, ID="X_2709", classes=["selected", "target"], guide=False)
    X_111 = eval_trilinear_point(model, A, B, C, 'a/(2*a**(2) - b**(2) - c**(2))', ID="X_111", classes=["center", "incident"])
    X_352 = eval_trilinear_point(model, A, B, C, '(a*(-a**(4) - b**(4) - c**(4) - 5*b**(2)*c**(2) + 4*a**(2)*b**(2) + 4*a**(2)*c**(2)))', ID="X_352", classes=["center", "incident"])
    central_line(model, X_111, X_352, 111, 352, incident=True)
    X_98 = eval_trilinear_point(model, A, B, C, 'sec(A +  omega  )', ID="X_98", classes=["center", "incident"])
    X_524 = eval_trilinear_point(model, A, B, C, '(2*a**(2) - b**(2) - c**(2))/a', ID="X_524", classes=["center", "incident"])
    central_line(model, X_98, X_524, 98, 524, incident=True)
    central_line(model, X_3, X_843, 3, 843, incident=True)
    return promote_point_to_top(model, X_2709)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2709 on the given reference triangle."""
    model = create_model('X_2709 = SR(X_98, X_111)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02709(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02709.json"))
    write_center_svg(
        model_acute,
        here / "x-02709.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
