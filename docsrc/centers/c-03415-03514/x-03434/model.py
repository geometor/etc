"""GEOMETOR construction model for X_3434 = ISOGONAL CONJUGATE OF X_3433."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    centroid_of,
    construct_baseline_triangle,
    create_model,
    eval_barycentric_point,
    eval_trilinear_point,
    feuerbach_point_of,
    incenter_of,
    midpoint,
    nagel_point_of,
    orthocenter_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_03434(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3434 = ISOGONAL CONJUGATE OF X_3433 on reference triangle ABC."""
    X_8 = nagel_point_of(model, A, B, C, ID="X_8", classes=["center"])
    X_3419 = eval_barycentric_point(model, A, B, C, '(a**(4) - a**(3)*(b + c) + a*(b + c)*(b**(2) + c**(2)) - (b**(2) - c**(2))**(2))', ID="X_3419", classes=["center"])
    X_3434 = midpoint(model, X_8, X_3419, ID="X_3434", classes=["selected", "target"], guide=False)
    X_4 = orthocenter_of(model, A, B, C, ID="X_4", classes=["center", "incident"])
    central_line(model, X_4, X_8, 4, 8, incident=True)
    X_2 = centroid_of(model, A, B, C, ID="X_2", classes=["center", "incident"])
    X_11 = feuerbach_point_of(model, A, B, C, ID="X_11", classes=["center", "incident"])
    central_line(model, X_2, X_11, 2, 11, incident=True)
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center", "incident"])
    X_224 = eval_trilinear_point(model, A, B, C, '(cot(B)*(cos(B/2))**(2) + cot(C)*(cos(C/2))**(2) - cot(A)*(cos(A/2))**(2))*cot(A)', ID="X_224", classes=["center", "incident"])
    central_line(model, X_1, X_224, 1, 224, incident=True)
    return promote_point_to_top(model, X_3434)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3434 on the given reference triangle."""
    model = create_model('X_3434 = ISOGONAL CONJUGATE OF X_3433')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03434(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03434.json"))
    write_center_svg(
        model_acute,
        here / "x-03434.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
