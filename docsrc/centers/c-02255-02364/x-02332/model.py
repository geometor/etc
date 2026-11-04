"""GEOMETOR construction model for X_2332 = X_2-ISOCONJUGATE OF X_1439."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    ceva_conjugate,
    construct_baseline_triangle,
    create_model,
    eval_barycentric_point,
    eval_trilinear_point,
    incenter_of,
    promote_point_to_top,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_02332(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2332 = X_2-ISOCONJUGATE OF X_1439 on reference triangle ABC."""
    X_2322 = eval_barycentric_point(model, A, B, C, '(b + c - a)**(2)/((b + c)*(b**(2) + c**(2) - a**(2)))', ID="X_2322", classes=["center"])
    X_2328 = eval_trilinear_point(model, A, B, C, '(1 + cos(A))/(cos(B) + cos(C))', ID="X_2328", classes=["center"])
    X_2332 = ceva_conjugate(model, A, B, C, X_2322, X_2328, ID="X_2332", classes=["selected", "target"])
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center", "incident"])
    X_19 = eval_trilinear_point(model, A, B, C, 'tan(A)', ID="X_19", classes=["center", "incident"])
    central_line(model, X_1, X_19, 1, 19, incident=True)
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center", "incident"])
    X_64 = eval_trilinear_point(model, A, B, C, '1/(cos(A) - cos(B)*cos(C))', ID="X_64", classes=["center", "incident"])
    central_line(model, X_6, X_64, 6, 64, incident=True)
    X_33 = eval_trilinear_point(model, A, B, C, '1 + sec(A)', ID="X_33", classes=["center", "incident"])
    X_41 = eval_trilinear_point(model, A, B, C, 'a**(2)*(b + c - a)', ID="X_41", classes=["center", "incident"])
    central_line(model, X_33, X_41, 33, 41, incident=True)
    return promote_point_to_top(model, X_2332)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2332 on the given reference triangle."""
    model = create_model('X_2332 = X_2-ISOCONJUGATE OF X_1439')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02332(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02332.json"))
    write_center_svg(
        model_acute,
        here / "x-02332.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
