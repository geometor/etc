"""GEOMETOR construction model for X_2748 = SR(X_105, X_106)."""

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


def construct_x_02748(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2748 = SR(X_105, X_106) on reference triangle ABC."""
    X_2748 = eval_trilinear_point(model, A, B, C, '(1/((b - c)*(a**(2) + b**(2) + c**(2) - 3*b*c)))', ID="X_2748", classes=["selected", "target"])
    X_105 = eval_trilinear_point(model, A, B, C, '1/(b**(2) + c**(2) - a*(b + c))', ID="X_105", classes=["center", "incident"])
    X_519 = eval_trilinear_point(model, A, B, C, '(2*a - b - c)/a', ID="X_519", classes=["center", "incident"])
    central_line(model, X_105, X_519, 105, 519, incident=True)
    X_106 = eval_trilinear_point(model, A, B, C, 'a/(2*a - b - c)', ID="X_106", classes=["center", "incident"])
    X_518 = eval_trilinear_point(model, A, B, C, '(a*b + a*c - b**(2) - c**(2))', ID="X_518", classes=["center", "incident"])
    central_line(model, X_106, X_518, 106, 518, incident=True)
    X_901 = eval_trilinear_point(model, A, B, C, 'a/((b - c)*(b + c - 2*a))', ID="X_901", classes=["center", "incident"])
    X_1026 = eval_trilinear_point(model, A, B, C, '((b**(2) + c**(2) - a*(b + c))/(b - c))', ID="X_1026", classes=["center", "incident"])
    central_line(model, X_901, X_1026, 901, 1026, incident=True)
    return promote_point_to_top(model, X_2748)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2748 on the given reference triangle."""
    model = create_model('X_2748 = SR(X_105, X_106)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02748(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02748.json"))
    write_center_svg(
        model_acute,
        here / "x-02748.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
