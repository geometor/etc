"""GEOMETOR construction model for X_214 = X_2-CEVA CONJUGATE OF X_44."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    centroid_of,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    incenter_of,
    midpoint,
    mittenpunkt_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00214(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_214 = X_2-CEVA CONJUGATE OF X_44 on reference triangle ABC."""
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center"])
    X_100 = eval_trilinear_point(model, A, B, C, '1/(b - c)', ID="X_100", classes=["center"])
    X_214 = midpoint(model, X_1, X_100, ID="X_214", classes=["selected", "target"], guide=False)
    X_9 = mittenpunkt_of(model, A, B, C, ID="X_9", classes=["center", "incident"])
    X_48 = eval_trilinear_point(model, A, B, C, 'tan(B) + tan(C)', ID="X_48", classes=["center", "incident"])
    central_line(model, X_9, X_48, 9, 48, incident=True)
    X_2 = centroid_of(model, A, B, C, ID="X_2", classes=["center", "incident"])
    X_80 = eval_trilinear_point(model, A, B, C, '1/(1 - 2*cos(A))', ID="X_80", classes=["center", "incident"])
    central_line(model, X_2, X_80, 2, 80, incident=True)
    X_88 = eval_trilinear_point(model, A, B, C, '1/(b + c - 2*a)', ID="X_88", classes=["center", "incident"])
    central_line(model, X_1, X_88, 1, 88, incident=True)
    return promote_point_to_top(model, X_214)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_214 on the given reference triangle."""
    model = create_model('X_214 = X_2-CEVA CONJUGATE OF X_44')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00214(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00214.json"))
    write_center_svg(
        model_acute,
        here / "x-00214.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
