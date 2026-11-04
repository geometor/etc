"""GEOMETOR construction model for X_2280 = X_2-ISOCONJUGATE OF X_1002."""

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


def construct_x_02280(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2280 = X_2-ISOCONJUGATE OF X_1002 on reference triangle ABC."""
    X_985 = eval_trilinear_point(model, A, B, C, '(1/(b**(2) + b*c + c**(2)))', ID="X_985", classes=["center"])
    X_31 = eval_trilinear_point(model, A, B, C, 'a**(2)', ID="X_31", classes=["center"])
    X_2280 = ceva_conjugate(model, A, B, C, X_985, X_31, ID="X_2280", classes=["selected", "target"])
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center", "incident"])
    central_line(model, X_6, X_31, 6, 31, incident=True)
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center", "incident"])
    X_41 = eval_trilinear_point(model, A, B, C, 'a**(2)*(b + c - a)', ID="X_41", classes=["center", "incident"])
    central_line(model, X_1, X_41, 1, 41, incident=True)
    X_57 = eval_trilinear_point(model, A, B, C, '1/(b + c - a)', ID="X_57", classes=["center", "incident"])
    X_77 = eval_trilinear_point(model, A, B, C, '1/(1 + sec(A))', ID="X_77", classes=["center", "incident"])
    central_line(model, X_57, X_77, 57, 77, incident=True)
    return promote_point_to_top(model, X_2280)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2280 on the given reference triangle."""
    model = create_model('X_2280 = X_2-ISOCONJUGATE OF X_1002')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02280(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02280.json"))
    write_center_svg(
        model_acute,
        here / "x-02280.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
