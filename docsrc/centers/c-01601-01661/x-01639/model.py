"""GEOMETOR construction model for X_1639 = TRIPOLAR CENTROID OF X_8."""

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
    mittenpunkt_of,
    promote_point_to_top,
    reflection_in_point,
)
from geometor.etc.render import write_center_svg


def construct_x_01639(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1639 = TRIPOLAR CENTROID OF X_8 on reference triangle ABC."""
    X_1638 = eval_barycentric_point(model, A, B, C, '(b - c)*(2*a**(2) - b**(2) - c**(2) - a*b - a*c + 2*b*c)', ID="X_1638", classes=["center"])
    X_2 = centroid_of(model, A, B, C, ID="X_2", classes=["center"])
    X_1639 = reflection_in_point(model, X_1638, X_2, ID="X_1639", classes=["selected", "target"], guide=False)
    X_9 = mittenpunkt_of(model, A, B, C, ID="X_9", classes=["center", "incident"])
    X_654 = eval_trilinear_point(model, A, B, C, 'cos(A - B) - cos(C - A)', ID="X_654", classes=["center", "incident"])
    central_line(model, X_9, X_654, 9, 654, incident=True)
    X_918 = eval_barycentric_point(model, A, B, C, '((b - c)*(b**(2) + c**(2) -a*b - a*c))', ID="X_918", classes=["center", "incident"])
    central_line(model, X_2, X_918, 2, 918, incident=True)
    X_210 = eval_trilinear_point(model, A, B, C, '(b + c)*(b + c - a)', ID="X_210", classes=["center", "incident"])
    X_926 = eval_trilinear_point(model, A, B, C, 'a*(a - b - c)*(b - c)*(a*b + a*c - b**(2) - c**(2))', ID="X_926", classes=["center", "incident"])
    central_line(model, X_210, X_926, 210, 926, incident=True)
    return promote_point_to_top(model, X_1639)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1639 on the given reference triangle."""
    model = create_model('X_1639 = TRIPOLAR CENTROID OF X_8')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01639(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01639.json"))
    write_center_svg(
        model_acute,
        here / "x-01639.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
