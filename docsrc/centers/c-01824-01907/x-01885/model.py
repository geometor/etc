"""GEOMETOR construction model for X_1885 = ZOSMA TRANSFORM OF X_774."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    centroid_of,
    circumcenter_of,
    construct_baseline_triangle,
    create_model,
    crosspoint,
    eval_trilinear_point,
    orthocenter_of,
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_01885(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1885 = ZOSMA TRANSFORM OF X_774 on reference triangle ABC."""
    X_4 = orthocenter_of(model, A, B, C, ID="X_4", classes=["center"])
    X_1105 = eval_trilinear_point(model, A, B, C, '((sec(A))/((cos(B))**(2) + (cos(C))**(2)))', ID="X_1105", classes=["center"])
    X_1885 = crosspoint(model, A, B, C, X_4, X_1105, ID="X_1885", classes=["selected", "target"])
    X_2 = centroid_of(model, A, B, C, ID="X_2", classes=["center"])
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center"])
    central_line(model, X_2, X_3, 2, 3)
    X_389 = eval_trilinear_point(model, A, B, C, 'cos(A) - cos(2*A)*cos(B - C)', ID="X_389", classes=["center", "incident"])
    X_974 = eval_trilinear_point(model, A, B, C, '(s*a**(10) - a**(8)*(3*b**(4) - 2*b**(2)*c**(2) + 3*c**(4)) + a**(6)*s*(2*b**(4) - 3*b**(2)*c**(2) + 2*c**(4)) + a**(4)*(b**(2) - c**(2))**(2)*(2*b**(4) - 7*b**(2)*c**(2) + 2*c**(4)) - 3*a**(2)*s*(b**(2) - c**(2))**(2)*(b**(4) - 3*b**(2)*c**(2) + c**(4)) + (b**(2) - c**(2))**(4)*(b**(4) + b**(2)*c**(2) + c**(4)))*cos(A)', ID="X_974", classes=["center", "incident"])
    central_line(model, X_389, X_974, 389, 974, incident=True)
    X_497 = eval_trilinear_point(model, A, B, C, '1 - cos(B)*cos(C)', ID="X_497", classes=["center", "incident"])
    X_1398 = point_from_barycentrics(model, A, B, C, 0.022602903, 0.091363312, 0.88603379, ID="X_1398", classes=["center", "incident"])
    central_line(model, X_497, X_1398, 497, 1398, incident=True)
    return promote_point_to_top(model, X_1885)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1885 on the given reference triangle."""
    model = create_model('X_1885 = ZOSMA TRANSFORM OF X_774')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01885(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01885.json"))
    write_center_svg(
        model_acute,
        here / "x-01885.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
