"""GEOMETOR construction model for X_2768 = SR(X_109, X_111)."""

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


def construct_x_02768(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2768 = SR(X_109, X_111) on reference triangle ABC."""
    X_2735 = point_from_barycentrics(model, A, B, C, -0.0011942247, 0.99884951, 0.0023447172, ID="X_2735", classes=["center"])
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center"])
    X_2768 = reflection_in_point(model, X_2735, X_3, ID="X_2768", classes=["selected", "target"], guide=False)
    X_109 = eval_trilinear_point(model, A, B, C, 'a/(cos(B) - cos(C))', ID="X_109", classes=["center", "incident"])
    X_524 = eval_trilinear_point(model, A, B, C, '(2*a**(2) - b**(2) - c**(2))/a', ID="X_524", classes=["center", "incident"])
    central_line(model, X_109, X_524, 109, 524, incident=True)
    X_111 = eval_trilinear_point(model, A, B, C, 'a/(2*a**(2) - b**(2) - c**(2))', ID="X_111", classes=["center", "incident"])
    X_522 = eval_trilinear_point(model, A, B, C, '(cos(B) - cos(C))*(csc(A))', ID="X_522", classes=["center", "incident"])
    central_line(model, X_111, X_522, 111, 522, incident=True)
    X_333 = eval_trilinear_point(model, A, B, C, 'b*c*(b + c - a)/(b + c)', ID="X_333", classes=["center", "incident"])
    X_691 = eval_trilinear_point(model, A, B, C, 'a/((b**(2) - c**(2))*(2*a**(2) - b**(2) - c**(2)))', ID="X_691", classes=["center", "incident"])
    central_line(model, X_333, X_691, 333, 691, incident=True)
    return promote_point_to_top(model, X_2768)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2768 on the given reference triangle."""
    model = create_model('X_2768 = SR(X_109, X_111)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02768(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02768.json"))
    write_center_svg(
        model_acute,
        here / "x-02768.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
