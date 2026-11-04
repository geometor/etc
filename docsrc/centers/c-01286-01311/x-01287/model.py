"""GEOMETOR construction model for X_1287 = COLLINGS TRANSFORM OF X_23."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_barycentric_point,
    eval_trilinear_point,
    intersect_lines,
    nine_point_center_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_01287(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1287 = COLLINGS TRANSFORM OF X_23 on reference triangle ABC."""
    X_5 = nine_point_center_of(model, A, B, C, ID="X_5", classes=["center"])
    X_842 = eval_barycentric_point(model, A, B, C, 'a**(2)/(2*a**(6) - 2*a**(4)*(b**(2) + c**(2)) + a**(2)*(b**(4) + c**(4)) - (b**(2) - c**(2))**(2)*(b**(2) + c**(2)))', ID="X_842", classes=["center"])
    X_110 = eval_trilinear_point(model, A, B, C, 'csc(B - C)', ID="X_110", classes=["center"])
    X_826 = eval_trilinear_point(model, A, B, C, 'a **(-1)*(b**(4) - c**(4)) + a**(3)*(b**(0) - c**(0))', ID="X_826", classes=["center"])
    central_line(model, X_5, X_842, 5, 842)
    central_line(model, X_110, X_826, 110, 826)
    X_1287 = intersect_lines(model, X_5, X_842, X_110, X_826, ID="X_1287", classes=["selected", "target"])
    X_523 = eval_trilinear_point(model, A, B, C, 'sin(B -C)', ID="X_523", classes=["center", "incident"])
    X_827 = eval_trilinear_point(model, A, B, C, '1/(a**(-1)*(b**(4) - c**(4)) + a**(3)*(b**(0) - c**(0)))', ID="X_827", classes=["center", "incident"])
    central_line(model, X_523, X_827, 523, 827, incident=True)
    return promote_point_to_top(model, X_1287)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1287 on the given reference triangle."""
    model = create_model('X_1287 = COLLINGS TRANSFORM OF X_23')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01287(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01287.json"))
    write_center_svg(
        model_acute,
        here / "x-01287.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
