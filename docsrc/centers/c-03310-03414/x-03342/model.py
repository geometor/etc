"""GEOMETOR construction model for X_3342 = ISOGONAL CONJUGATE OF X_3341."""

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
    isogonal_conjugate,
    mittenpunkt_of,
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_03342(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3342 = ISOGONAL CONJUGATE OF X_3341 on reference triangle ABC."""
    X_3341 = point_from_barycentrics(model, A, B, C, 0.05793173, 0.086051457, 0.85601681, ID="X_3341", classes=["center"])
    X_3342 = isogonal_conjugate(model, A, B, C, X_3341, ID="X_3342", classes=["selected", "target"])
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center", "incident"])
    X_223 = eval_trilinear_point(model, A, B, C, '(tan(A/2))*(cos(B) + cos(C) - cos(A) - 1)', ID="X_223", classes=["center", "incident"])
    central_line(model, X_3, X_223, 3, 223, incident=True)
    X_2 = centroid_of(model, A, B, C, ID="X_2", classes=["center", "incident"])
    X_271 = eval_trilinear_point(model, A, B, C, '((cot(A)*cot(A/2))/(-1 - cos(A) + cos(B) + cos(C)))', ID="X_271", classes=["center", "incident"])
    central_line(model, X_2, X_271, 2, 271, incident=True)
    X_9 = mittenpunkt_of(model, A, B, C, ID="X_9", classes=["center", "incident"])
    X_1249 = eval_trilinear_point(model, A, B, C, '(tan(A))*(cos(A) - cos(B)*cos(C))', ID="X_1249", classes=["center", "incident"])
    central_line(model, X_9, X_1249, 9, 1249, incident=True)
    return promote_point_to_top(model, X_3342)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3342 on the given reference triangle."""
    model = create_model('X_3342 = ISOGONAL CONJUGATE OF X_3341')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03342(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03342.json"))
    write_center_svg(
        model_acute,
        here / "x-03342.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
