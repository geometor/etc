"""GEOMETOR construction model for X_1504 = INSIMILICENTER OF MOSES AND 2nd LEMOINE CIRCLES."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    centroid_of,
    ceva_conjugate,
    circumcenter_of,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    point_from_barycentrics,
    promote_point_to_top,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_01504(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1504 = INSIMILICENTER OF MOSES AND 2nd LEMOINE CIRCLES on reference triangle ABC."""
    X_1306 = point_from_barycentrics(model, A, B, C, 0.5106151, -0.33128455, 0.82066945, ID="X_1306", classes=["center"])
    X_512 = eval_trilinear_point(model, A, B, C, 'a*(b**(2) - c**(2))', ID="X_512", classes=["center"])
    X_1504 = ceva_conjugate(model, A, B, C, X_1306, X_512, ID="X_1504", classes=["selected", "target"])
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center", "incident"])
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center", "incident"])
    central_line(model, X_3, X_6, 3, 6, incident=True)
    X_2 = centroid_of(model, A, B, C, ID="X_2", classes=["center", "incident"])
    X_588 = eval_trilinear_point(model, A, B, C, '(a/(a**(2) + 4*area ))', ID="X_588", classes=["center", "incident"])
    central_line(model, X_2, X_588, 2, 588, incident=True)
    X_115 = eval_trilinear_point(model, A, B, C, 'b*c*(b**(2) - c**(2))**(2)', ID="X_115", classes=["center", "incident"])
    X_485 = eval_trilinear_point(model, A, B, C, 'sec(A -  pi  /4)', ID="X_485", classes=["center", "incident"])
    central_line(model, X_115, X_485, 115, 485, incident=True)
    return promote_point_to_top(model, X_1504)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1504 on the given reference triangle."""
    model = create_model('X_1504 = INSIMILICENTER OF MOSES AND 2nd LEMOINE CIRCLES')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01504(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01504.json"))
    write_center_svg(
        model_acute,
        here / "x-01504.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
