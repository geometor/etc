"""GEOMETOR construction model for X_1211 = ISOGONAL CONJUGATE OF X_1169."""

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
    isogonal_conjugate,
    point_from_barycentrics,
    promote_point_to_top,
    spieker_center_of,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_01211(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1211 = ISOGONAL CONJUGATE OF X_1169 on reference triangle ABC."""
    X_1169 = point_from_barycentrics(model, A, B, C, 0.19529243, 0.31300293, 0.49170465, ID="X_1169", classes=["center"])
    X_1211 = isogonal_conjugate(model, A, B, C, X_1169, ID="X_1211", classes=["selected", "target"])
    X_2 = centroid_of(model, A, B, C, ID="X_2", classes=["center", "incident"])
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center", "incident"])
    central_line(model, X_2, X_6, 2, 6, incident=True)
    X_10 = spieker_center_of(model, A, B, C, ID="X_10", classes=["center", "incident"])
    X_12 = eval_trilinear_point(model, A, B, C, '1 + cos(B - C)', ID="X_12", classes=["center", "incident"])
    central_line(model, X_10, X_12, 10, 12, incident=True)
    X_120 = eval_trilinear_point(model, A, B, C, 'b*c*(2*a*b*c - (b + c)*(a**(2) + (b - c)**(2)))*(b**(2) + c**(2) - a*b -a*c)', ID="X_120", classes=["center", "incident"])
    X_125 = eval_trilinear_point(model, A, B, C, 'cos(A)*(sin(B - C))**(2)', ID="X_125", classes=["center", "incident"])
    central_line(model, X_120, X_125, 120, 125, incident=True)
    return promote_point_to_top(model, X_1211)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1211 on the given reference triangle."""
    model = create_model('X_1211 = ISOGONAL CONJUGATE OF X_1169')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01211(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01211.json"))
    write_center_svg(
        model_acute,
        here / "x-01211.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
