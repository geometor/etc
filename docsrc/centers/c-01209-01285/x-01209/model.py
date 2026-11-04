"""GEOMETOR construction model for X_1209 = ISOGONAL CONJUGATE OF X_1166."""

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
    nine_point_center_of,
    point_from_barycentrics,
    promote_point_to_top,
    reflection_in_point,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_01209(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1209 = ISOGONAL CONJUGATE OF X_1166 on reference triangle ABC."""
    X_52 = eval_trilinear_point(model, A, B, C, 'cos(2*A)*cos(B - C)', ID="X_52", classes=["center"])
    X_973 = point_from_barycentrics(model, A, B, C, 0.17639509, 0.28253921, 0.5410657, ID="X_973", classes=["center"])
    X_1209 = reflection_in_point(model, X_52, X_973, ID="X_1209", classes=["selected", "target"], guide=False)
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center", "incident"])
    X_17 = eval_trilinear_point(model, A, B, C, 'csc(A + pi /6)', ID="X_17", classes=["center", "incident"])
    central_line(model, X_6, X_17, 6, 17, incident=True)
    X_2 = centroid_of(model, A, B, C, ID="X_2", classes=["center", "incident"])
    X_54 = eval_trilinear_point(model, A, B, C, 'sec(B - C)', ID="X_54", classes=["center", "incident"])
    central_line(model, X_2, X_54, 2, 54, incident=True)
    X_5 = nine_point_center_of(model, A, B, C, ID="X_5", classes=["center", "incident"])
    X_51 = eval_trilinear_point(model, A, B, C, 'a**(2)*cos(B - C)', ID="X_51", classes=["center", "incident"])
    central_line(model, X_5, X_51, 5, 51, incident=True)
    return promote_point_to_top(model, X_1209)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1209 on the given reference triangle."""
    model = create_model('X_1209 = ISOGONAL CONJUGATE OF X_1166')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01209(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01209.json"))
    write_center_svg(
        model_acute,
        here / "x-01209.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
