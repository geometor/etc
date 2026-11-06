"""GEOMETOR construction model for X_3249 = SS(a → bc) OF X_764."""

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
)
from geometor.etc.render import write_center_svg


def construct_x_03249(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3249 = SS(a → bc) OF X_764 on reference triangle ABC."""
    X_3249 = eval_trilinear_point(model, A, B, C, '((a*b - a*c)**(3))', ID="X_3249", classes=["selected", "target"])
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center", "incident"])
    X_649 = eval_trilinear_point(model, A, B, C, 'a*(b - c)', ID="X_649", classes=["center", "incident"])
    central_line(model, X_1, X_649, 1, 649, incident=True)
    X_330 = eval_trilinear_point(model, A, B, C, 'b*c/(a*b + a*c - b*c)', ID="X_330", classes=["center", "incident"])
    X_514 = eval_trilinear_point(model, A, B, C, '(b - c)/a', ID="X_514", classes=["center", "incident"])
    central_line(model, X_330, X_514, 330, 514, incident=True)
    X_213 = eval_trilinear_point(model, A, B, C, '(b + c)*a**(2)', ID="X_213", classes=["center", "incident"])
    X_667 = eval_trilinear_point(model, A, B, C, 'a**(2)*(b - c)', ID="X_667", classes=["center", "incident"])
    central_line(model, X_213, X_667, 213, 667, incident=True)
    return promote_point_to_top(model, X_3249)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3249 on the given reference triangle."""
    model = create_model('X_3249 = SS(a → bc) OF X_764')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03249(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03249.json"))
    write_center_svg(
        model_acute,
        here / "x-03249.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
