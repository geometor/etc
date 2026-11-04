"""GEOMETOR construction model for X_2663 = CROSSSUM OF PU(84)."""

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
    promote_point_to_top,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_02663(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2663 = CROSSSUM OF PU(84) on reference triangle ABC."""
    X_2663 = eval_trilinear_point(model, A, B, C, '((1/a + 1/b)*(1/a + 1/c) + (1/b + 1/c)**(2))', ID="X_2663", classes=["selected", "target"])
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center", "incident"])
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center", "incident"])
    central_line(model, X_1, X_6, 1, 6, incident=True)
    X_42 = eval_trilinear_point(model, A, B, C, 'a*(b + c)', ID="X_42", classes=["center", "incident"])
    X_894 = eval_trilinear_point(model, A, B, C, '(a**(2) + b*c)/a', ID="X_894", classes=["center", "incident"])
    central_line(model, X_42, X_894, 42, 894, incident=True)
    X_86 = eval_trilinear_point(model, A, B, C, 'b*c/(b + c)', ID="X_86", classes=["center", "incident"])
    X_872 = eval_trilinear_point(model, A, B, C, '(a*(b + c))**(2)', ID="X_872", classes=["center", "incident"])
    central_line(model, X_86, X_872, 86, 872, incident=True)
    return promote_point_to_top(model, X_2663)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2663 on the given reference triangle."""
    model = create_model('X_2663 = CROSSSUM OF PU(84)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02663(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02663.json"))
    write_center_svg(
        model_acute,
        here / "x-02663.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
