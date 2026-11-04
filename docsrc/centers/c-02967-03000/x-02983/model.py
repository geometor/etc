"""GEOMETOR construction model for X_2983 = DC(X_27)."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    intersect_lines,
    mittenpunkt_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_02983(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2983 = DC(X_27) on reference triangle ABC."""
    X_9 = mittenpunkt_of(model, A, B, C, ID="X_9", classes=["center"])
    X_34 = eval_trilinear_point(model, A, B, C, '1 - sec(A)', ID="X_34", classes=["center"])
    X_56 = eval_trilinear_point(model, A, B, C, 'a/(b + c - a)', ID="X_56", classes=["center"])
    X_219 = eval_trilinear_point(model, A, B, C, 'cos(A)*cot(A/2)', ID="X_219", classes=["center"])
    central_line(model, X_9, X_34, 9, 34)
    central_line(model, X_56, X_219, 56, 219)
    X_2983 = intersect_lines(model, X_9, X_34, X_56, X_219, ID="X_2983", classes=["selected", "target"])
    X_63 = eval_trilinear_point(model, A, B, C, 'cot(A)', ID="X_63", classes=["center", "incident"])
    X_269 = eval_trilinear_point(model, A, B, C, '(tan(A/2))**(2)', ID="X_269", classes=["center", "incident"])
    central_line(model, X_63, X_269, 63, 269, incident=True)
    return promote_point_to_top(model, X_2983)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2983 on the given reference triangle."""
    model = create_model('X_2983 = DC(X_27)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02983(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02983.json"))
    write_center_svg(
        model_acute,
        here / "x-02983.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
