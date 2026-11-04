"""GEOMETOR construction model for X_1223 = ISOGONAL CONJUGATE OF X_1202."""

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
    gergonne_point_of,
    isogonal_conjugate,
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_01223(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1223 = ISOGONAL CONJUGATE OF X_1202 on reference triangle ABC."""
    X_1202 = point_from_barycentrics(model, A, B, C, 0.21636624, 0.32445983, 0.45917393, ID="X_1202", classes=["center"])
    X_1223 = isogonal_conjugate(model, A, B, C, X_1202, ID="X_1223", classes=["selected", "target"])
    X_7 = gergonne_point_of(model, A, B, C, ID="X_7", classes=["center", "incident"])
    X_220 = eval_trilinear_point(model, A, B, C, 'a*(b + c - a)**(2)', ID="X_220", classes=["center", "incident"])
    central_line(model, X_7, X_220, 7, 220, incident=True)
    X_2 = centroid_of(model, A, B, C, ID="X_2", classes=["center", "incident"])
    X_480 = eval_trilinear_point(model, A, B, C, '(cot(A/2)*cos(A/2))**(2)', ID="X_480", classes=["center", "incident"])
    central_line(model, X_2, X_480, 2, 480, incident=True)
    X_75 = eval_trilinear_point(model, A, B, C, '1/a**(2)', ID="X_75", classes=["center", "incident"])
    X_728 = eval_trilinear_point(model, A, B, C, '((b + c - a)**(3))', ID="X_728", classes=["center", "incident"])
    central_line(model, X_75, X_728, 75, 728, incident=True)
    return promote_point_to_top(model, X_1223)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1223 on the given reference triangle."""
    model = create_model('X_1223 = ISOGONAL CONJUGATE OF X_1202')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01223(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01223.json"))
    write_center_svg(
        model_acute,
        here / "x-01223.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
