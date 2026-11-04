"""GEOMETOR construction model for X_1689 = INVERSE-IN-BROCARD-CIRCLE OF X_1687."""

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
    eval_trilinear_point,
    orthocenter_of,
    promote_point_to_top,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_01689(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1689 = INVERSE-IN-BROCARD-CIRCLE OF X_1687 on reference triangle ABC."""
    X_1689 = eval_trilinear_point(model, A, B, C, 'cos(A +  omega  /2 +  pi  /4)', ID="X_1689", classes=["selected", "target"])
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center", "incident"])
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center", "incident"])
    central_line(model, X_3, X_6, 3, 6, incident=True)
    X_2 = centroid_of(model, A, B, C, ID="X_2", classes=["center", "incident"])
    X_2009 = eval_trilinear_point(model, A, B, C, '(cos(B - C) + sin(A +  omega  ))', ID="X_2009", classes=["center", "incident"])
    central_line(model, X_2, X_2009, 2, 2009, incident=True)
    X_4 = orthocenter_of(model, A, B, C, ID="X_4", classes=["center", "incident"])
    X_2010 = eval_trilinear_point(model, A, B, C, '(cos(B - C) - sin(A +  omega  ))', ID="X_2010", classes=["center", "incident"])
    central_line(model, X_4, X_2010, 4, 2010, incident=True)
    return promote_point_to_top(model, X_1689)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1689 on the given reference triangle."""
    model = create_model('X_1689 = INVERSE-IN-BROCARD-CIRCLE OF X_1687')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01689(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01689.json"))
    write_center_svg(
        model_acute,
        here / "x-01689.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
