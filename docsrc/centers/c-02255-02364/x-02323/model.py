"""GEOMETOR construction model for X_2323 = X_2-ISOCONJUGATE OF X_1411."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    incenter_of,
    isogonal_conjugate,
    promote_point_to_top,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_02323(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2323 = X_2-ISOCONJUGATE OF X_1411 on reference triangle ABC."""
    X_2006 = eval_trilinear_point(model, A, B, C, 'sin(A/2)*sec(3*A/2)', ID="X_2006", classes=["center"])
    X_2323 = isogonal_conjugate(model, A, B, C, X_2006, ID="X_2323", classes=["selected", "target"])
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center", "incident"])
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center", "incident"])
    central_line(model, X_1, X_6, 1, 6, incident=True)
    X_54 = eval_trilinear_point(model, A, B, C, 'sec(B - C)', ID="X_54", classes=["center", "incident"])
    X_71 = eval_trilinear_point(model, A, B, C, '(b + c)*cos(A)', ID="X_71", classes=["center", "incident"])
    central_line(model, X_54, X_71, 54, 71, incident=True)
    X_60 = eval_trilinear_point(model, A, B, C, '1/(1 + cos(B - C))', ID="X_60", classes=["center", "incident"])
    X_283 = eval_trilinear_point(model, A, B, C, '(cos(A))/(cos(B) + cos(C))', ID="X_283", classes=["center", "incident"])
    central_line(model, X_60, X_283, 60, 283, incident=True)
    return promote_point_to_top(model, X_2323)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2323 on the given reference triangle."""
    model = create_model('X_2323 = X_2-ISOCONJUGATE OF X_1411')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02323(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02323.json"))
    write_center_svg(
        model_acute,
        here / "x-02323.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
