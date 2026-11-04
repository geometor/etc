"""GEOMETOR construction model for X_1505 = EXSIMILICENTER OF MOSES AND 2nd LEMOINE CIRCLES."""

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


def construct_x_01505(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1505 = EXSIMILICENTER OF MOSES AND 2nd LEMOINE CIRCLES on reference triangle ABC."""
    X_1307 = point_from_barycentrics(model, A, B, C, 0.10979819, 1.2426467, -0.35244492, ID="X_1307", classes=["center"])
    X_512 = eval_trilinear_point(model, A, B, C, 'a*(b**(2) - c**(2))', ID="X_512", classes=["center"])
    X_1505 = ceva_conjugate(model, A, B, C, X_1307, X_512, ID="X_1505", classes=["selected", "target"])
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center", "incident"])
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center", "incident"])
    central_line(model, X_3, X_6, 3, 6, incident=True)
    X_2 = centroid_of(model, A, B, C, ID="X_2", classes=["center", "incident"])
    X_589 = eval_trilinear_point(model, A, B, C, '(a/(a**(2) - 4*area ))', ID="X_589", classes=["center", "incident"])
    central_line(model, X_2, X_589, 2, 589, incident=True)
    X_115 = eval_trilinear_point(model, A, B, C, 'b*c*(b**(2) - c**(2))**(2)', ID="X_115", classes=["center", "incident"])
    X_486 = eval_trilinear_point(model, A, B, C, 'sec(A +  pi  /4)', ID="X_486", classes=["center", "incident"])
    central_line(model, X_115, X_486, 115, 486, incident=True)
    return promote_point_to_top(model, X_1505)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1505 on the given reference triangle."""
    model = create_model('X_1505 = EXSIMILICENTER OF MOSES AND 2nd LEMOINE CIRCLES')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01505(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01505.json"))
    write_center_svg(
        model_acute,
        here / "x-01505.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
