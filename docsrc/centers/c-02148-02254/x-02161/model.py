"""GEOMETOR construction model for X_2161 = X_2-ISOCONJUGATE OF X_36."""

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
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_02161(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2161 = X_2-ISOCONJUGATE OF X_36 on reference triangle ABC."""
    X_2006 = eval_trilinear_point(model, A, B, C, 'sin(A/2)*sec(3*A/2)', ID="X_2006", classes=["center"])
    X_1411 = eval_trilinear_point(model, A, B, C, '(1 - cos(A))/(1 - 2*cos(A))', ID="X_1411", classes=["center"])
    X_2161 = ceva_conjugate(model, A, B, C, X_2006, X_1411, ID="X_2161", classes=["selected", "target"])
    X_19 = eval_trilinear_point(model, A, B, C, 'tan(A)', ID="X_19", classes=["center", "incident"])
    X_53 = eval_trilinear_point(model, A, B, C, 'tan(A)*cos(B - C)', ID="X_53", classes=["center", "incident"])
    central_line(model, X_19, X_53, 19, 53, incident=True)
    X_9 = mittenpunkt_of(model, A, B, C, ID="X_9", classes=["center", "incident"])
    X_80 = eval_trilinear_point(model, A, B, C, '1/(1 - 2*cos(A))', ID="X_80", classes=["center", "incident"])
    central_line(model, X_9, X_80, 9, 80, incident=True)
    X_45 = eval_trilinear_point(model, A, B, C, '2*b + 2*c - a', ID="X_45", classes=["center", "incident"])
    X_55 = eval_trilinear_point(model, A, B, C, 'a*(b + c - a)', ID="X_55", classes=["center", "incident"])
    central_line(model, X_45, X_55, 45, 55, incident=True)
    return promote_point_to_top(model, X_2161)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2161 on the given reference triangle."""
    model = create_model('X_2161 = X_2-ISOCONJUGATE OF X_36')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02161(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02161.json"))
    write_center_svg(
        model_acute,
        here / "x-02161.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
