"""GEOMETOR construction model for X_1756 = MIMOSA TRANSFORM OF X_293."""

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
    mittenpunkt_of,
    promote_point_to_top,
    reflection_in_point,
)
from geometor.etc.render import write_center_svg


def construct_x_01756(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1756 = MIMOSA TRANSFORM OF X_293 on reference triangle ABC."""
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center"])
    X_1284 = eval_trilinear_point(model, A, B, C, '((b + c)*(b*c - a**(2))/(b + c - a))', ID="X_1284", classes=["center"])
    X_1756 = reflection_in_point(model, X_1, X_1284, ID="X_1756", classes=["selected", "target"], guide=False)
    X_9 = mittenpunkt_of(model, A, B, C, ID="X_9", classes=["center", "incident"])
    X_46 = eval_trilinear_point(model, A, B, C, 'cos(B) + cos(C) - cos(A)', ID="X_46", classes=["center", "incident"])
    central_line(model, X_9, X_46, 9, 46, incident=True)
    X_256 = eval_trilinear_point(model, A, B, C, '1/(a**(2) + b*c)', ID="X_256", classes=["center", "incident"])
    central_line(model, X_1, X_256, 1, 256, incident=True)
    X_36 = eval_trilinear_point(model, A, B, C, '1 - 2*cos(A)', ID="X_36", classes=["center", "incident"])
    X_238 = eval_trilinear_point(model, A, B, C, 'a**(2) - b*c', ID="X_238", classes=["center", "incident"])
    central_line(model, X_36, X_238, 36, 238, incident=True)
    return promote_point_to_top(model, X_1756)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1756 on the given reference triangle."""
    model = create_model('X_1756 = MIMOSA TRANSFORM OF X_293')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01756(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01756.json"))
    write_center_svg(
        model_acute,
        here / "x-01756.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
