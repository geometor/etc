"""GEOMETOR construction model for X_2307 = X_2-ISOCONJUGATE OF X_1251."""

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
    incenter_of,
    promote_point_to_top,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_02307(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2307 = X_2-ISOCONJUGATE OF X_1251 on reference triangle ABC."""
    X_1082 = eval_trilinear_point(model, A, B, C, '(sec(A/2))*sin(A/2 -  pi  /3)', ID="X_1082", classes=["center"])
    X_1250 = eval_trilinear_point(model, A, B, C, '(cos(A/2)*cos(A/2 +  pi  /6))', ID="X_1250", classes=["center"])
    X_2307 = ceva_conjugate(model, A, B, C, X_1082, X_1250, ID="X_2307", classes=["selected", "target"])
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center", "incident"])
    X_41 = eval_trilinear_point(model, A, B, C, 'a**(2)*(b + c - a)', ID="X_41", classes=["center", "incident"])
    central_line(model, X_6, X_41, 6, 41, incident=True)
    X_15 = eval_trilinear_point(model, A, B, C, 'sin(A +  pi  /3)', ID="X_15", classes=["center", "incident"])
    X_35 = eval_trilinear_point(model, A, B, C, '1 + 2*cos(A)', ID="X_35", classes=["center", "incident"])
    central_line(model, X_15, X_35, 15, 35, incident=True)
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center", "incident"])
    X_61 = eval_trilinear_point(model, A, B, C, 'sin(A +  pi  /6)', ID="X_61", classes=["center", "incident"])
    central_line(model, X_1, X_61, 1, 61, incident=True)
    return promote_point_to_top(model, X_2307)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2307 on the given reference triangle."""
    model = create_model('X_2307 = X_2-ISOCONJUGATE OF X_1251')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02307(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02307.json"))
    write_center_svg(
        model_acute,
        here / "x-02307.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
