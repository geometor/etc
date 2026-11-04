"""GEOMETOR construction model for X_2767 = SR(X_108, X_111)."""

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
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_02767(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2767 = SR(X_108, X_111) on reference triangle ABC."""
    X_108 = eval_trilinear_point(model, A, B, C, 'a/(sec(B) - sec(C))', ID="X_108", classes=["center"])
    X_524 = eval_trilinear_point(model, A, B, C, '(2*a**(2) - b**(2) - c**(2))/a', ID="X_524", classes=["center"])
    X_111 = eval_trilinear_point(model, A, B, C, 'a/(2*a**(2) - b**(2) - c**(2))', ID="X_111", classes=["center"])
    X_521 = eval_trilinear_point(model, A, B, C, '(sec(B) - sec(C))*(csc(A))', ID="X_521", classes=["center"])
    central_line(model, X_108, X_524, 108, 524)
    central_line(model, X_111, X_521, 111, 521)
    X_2767 = intersect_lines(model, X_108, X_524, X_111, X_521, ID="X_2767", classes=["selected", "target"])
    X_691 = eval_trilinear_point(model, A, B, C, 'a/((b**(2) - c**(2))*(2*a**(2) - b**(2) - c**(2)))', ID="X_691", classes=["center", "incident"])
    X_1812 = eval_trilinear_point(model, A, B, C, 'cot(A)*cot(A/2)/(b + c)', ID="X_1812", classes=["center", "incident"])
    central_line(model, X_691, X_1812, 691, 1812, incident=True)
    return promote_point_to_top(model, X_2767)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2767 on the given reference triangle."""
    model = create_model('X_2767 = SR(X_108, X_111)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02767(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02767.json"))
    write_center_svg(
        model_acute,
        here / "x-02767.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
