"""GEOMETOR construction model for X_3500 = INTERSECTION OF LINES X_1X_295 AND X_3X_238."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    circumcenter_of,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    incenter_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_03500(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3500 = INTERSECTION OF LINES X_1X_295 AND X_3X_238 on reference triangle ABC."""
    X_3500 = eval_trilinear_point(model, A, B, C, '(1/(a**(2)*b + a**(2)*c - a*(b**(2) + b*c + c**(2)) + b*c*( b + c)))', ID="X_3500", classes=["selected", "target"])
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center", "incident"])
    X_238 = eval_trilinear_point(model, A, B, C, 'a**(2) - b*c', ID="X_238", classes=["center", "incident"])
    central_line(model, X_3, X_238, 3, 238, incident=True)
    X_63 = eval_trilinear_point(model, A, B, C, 'cot(A)', ID="X_63", classes=["center", "incident"])
    X_194 = eval_trilinear_point(model, A, B, C, 'b*c*(a**(2)*b**(2) + a**(2)*c**(2) - b**(2)*c**(2))', ID="X_194", classes=["center", "incident"])
    central_line(model, X_63, X_194, 63, 194, incident=True)
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center", "incident"])
    X_295 = eval_trilinear_point(model, A, B, C, '(cos(A))/(a**(2) - b*c)', ID="X_295", classes=["center", "incident"])
    central_line(model, X_1, X_295, 1, 295, incident=True)
    return promote_point_to_top(model, X_3500)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3500 on the given reference triangle."""
    model = create_model('X_3500 = INTERSECTION OF LINES X_1X_295 AND X_3X_238')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03500(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03500.json"))
    write_center_svg(
        model_acute,
        here / "x-03500.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
