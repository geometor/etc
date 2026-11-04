"""GEOMETOR construction model for X_2354 = X_2-ISOCONJUGATE OF X_1791."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    ceva_conjugate,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    mittenpunkt_of,
    orthocenter_of,
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_02354(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2354 = X_2-ISOCONJUGATE OF X_1791 on reference triangle ABC."""
    X_1848 = point_from_barycentrics(model, A, B, C, 0.14011799, 0.21533923, 0.64454277, ID="X_1848", classes=["center"])
    X_1193 = eval_trilinear_point(model, A, B, C, '(a*(b**(2) + c**(2) + a*b + a*c))', ID="X_1193", classes=["center"])
    X_2354 = ceva_conjugate(model, A, B, C, X_1848, X_1193, ID="X_2354", classes=["selected", "target"])
    X_4 = orthocenter_of(model, A, B, C, ID="X_4", classes=["center", "incident"])
    X_9 = mittenpunkt_of(model, A, B, C, ID="X_9", classes=["center", "incident"])
    central_line(model, X_4, X_9, 4, 9, incident=True)
    X_25 = eval_trilinear_point(model, A, B, C, 'sin(A)*tan(A)', ID="X_25", classes=["center", "incident"])
    X_31 = eval_trilinear_point(model, A, B, C, 'a**(2)', ID="X_31", classes=["center", "incident"])
    central_line(model, X_25, X_31, 25, 31, incident=True)
    X_28 = eval_trilinear_point(model, A, B, C, '(tan(A))/(b + c)', ID="X_28", classes=["center", "incident"])
    X_238 = eval_trilinear_point(model, A, B, C, 'a**(2) - b*c', ID="X_238", classes=["center", "incident"])
    central_line(model, X_28, X_238, 28, 238, incident=True)
    return promote_point_to_top(model, X_2354)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2354 on the given reference triangle."""
    model = create_model('X_2354 = X_2-ISOCONJUGATE OF X_1791')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02354(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02354.json"))
    write_center_svg(
        model_acute,
        here / "x-02354.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
