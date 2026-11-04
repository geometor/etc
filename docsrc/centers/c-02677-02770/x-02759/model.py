"""GEOMETOR construction model for X_2759 = SR(X_106, X_111)."""

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


def construct_x_02759(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2759 = SR(X_106, X_111) on reference triangle ABC."""
    X_106 = eval_trilinear_point(model, A, B, C, 'a/(2*a - b - c)', ID="X_106", classes=["center"])
    X_524 = eval_trilinear_point(model, A, B, C, '(2*a**(2) - b**(2) - c**(2))/a', ID="X_524", classes=["center"])
    X_111 = eval_trilinear_point(model, A, B, C, 'a/(2*a**(2) - b**(2) - c**(2))', ID="X_111", classes=["center"])
    X_519 = eval_trilinear_point(model, A, B, C, '(2*a - b - c)/a', ID="X_519", classes=["center"])
    central_line(model, X_106, X_524, 106, 524)
    central_line(model, X_111, X_519, 111, 519)
    X_2759 = intersect_lines(model, X_106, X_524, X_111, X_519, ID="X_2759", classes=["selected", "target"])
    X_1293 = eval_trilinear_point(model, A, B, C, '(a/((b - c)*(3*a - b - c)))', ID="X_1293", classes=["center", "incident"])
    X_1499 = eval_trilinear_point(model, A, B, C, 'b*c*(b**(2) - c**(2))*(b**(2) + c**(2) - 5*a**(2))', ID="X_1499", classes=["center", "incident"])
    central_line(model, X_1293, X_1499, 1293, 1499, incident=True)
    return promote_point_to_top(model, X_2759)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2759 on the given reference triangle."""
    model = create_model('X_2759 = SR(X_106, X_111)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02759(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02759.json"))
    write_center_svg(
        model_acute,
        here / "x-02759.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
