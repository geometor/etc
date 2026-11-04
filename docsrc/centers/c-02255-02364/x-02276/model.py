"""GEOMETOR construction model for X_2276 = X_2-ISOCONJUGATE OF X_985."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    centroid_of,
    construct_baseline_triangle,
    create_model,
    crosspoint,
    eval_trilinear_point,
    incenter_of,
    promote_point_to_top,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_02276(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2276 = X_2-ISOCONJUGATE OF X_985 on reference triangle ABC."""
    X_2 = centroid_of(model, A, B, C, ID="X_2", classes=["center"])
    X_1002 = eval_trilinear_point(model, A, B, C, '(1/(a**(2) - a*(b + c) - 2*b*c))', ID="X_1002", classes=["center"])
    X_2276 = crosspoint(model, A, B, C, X_2, X_1002, ID="X_2276", classes=["selected", "target"])
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center", "incident"])
    X_31 = eval_trilinear_point(model, A, B, C, 'a**(2)', ID="X_31", classes=["center", "incident"])
    central_line(model, X_6, X_31, 6, 31, incident=True)
    X_37 = eval_trilinear_point(model, A, B, C, 'b + c', ID="X_37", classes=["center", "incident"])
    central_line(model, X_2, X_37, 2, 37, incident=True)
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center", "incident"])
    X_39 = eval_trilinear_point(model, A, B, C, 'a*(b**(2) + c**(2))', ID="X_39", classes=["center", "incident"])
    central_line(model, X_1, X_39, 1, 39, incident=True)
    return promote_point_to_top(model, X_2276)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2276 on the given reference triangle."""
    model = create_model('X_2276 = X_2-ISOCONJUGATE OF X_985')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02276(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02276.json"))
    write_center_svg(
        model_acute,
        here / "x-02276.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
