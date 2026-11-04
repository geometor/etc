"""GEOMETOR construction model for X_2053 = X_2-ISOCONJUGATE OF X_1423."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_02053(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2053 = X_2-ISOCONJUGATE OF X_1423 on reference triangle ABC."""
    X_2053 = eval_trilinear_point(model, A, B, C, '(a*(b + c - a)/(a*b + a*c - b*c))', ID="X_2053", classes=["selected", "target"])
    X_56 = eval_trilinear_point(model, A, B, C, 'a/(b + c - a)', ID="X_56", classes=["center", "incident"])
    X_87 = eval_trilinear_point(model, A, B, C, '1/(a*b + a*c - b*c)', ID="X_87", classes=["center", "incident"])
    central_line(model, X_56, X_87, 56, 87, incident=True)
    X_31 = eval_trilinear_point(model, A, B, C, 'a**(2)', ID="X_31", classes=["center", "incident"])
    X_172 = eval_trilinear_point(model, A, B, C, 'a**(3) + a*b*c', ID="X_172", classes=["center", "incident"])
    central_line(model, X_31, X_172, 31, 172, incident=True)
    X_105 = eval_trilinear_point(model, A, B, C, '1/(b**(2) + c**(2) - a*(b + c))', ID="X_105", classes=["center", "incident"])
    X_330 = eval_trilinear_point(model, A, B, C, 'b*c/(a*b + a*c - b*c)', ID="X_330", classes=["center", "incident"])
    central_line(model, X_105, X_330, 105, 330, incident=True)
    return promote_point_to_top(model, X_2053)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2053 on the given reference triangle."""
    model = create_model('X_2053 = X_2-ISOCONJUGATE OF X_1423')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02053(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02053.json"))
    write_center_svg(
        model_acute,
        here / "x-02053.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
