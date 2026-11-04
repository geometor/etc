"""GEOMETOR construction model for X_1431 = X_256-BETH CONJUGATE OF X_256."""

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
    intersect_lines,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_01431(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1431 = X_256-BETH CONJUGATE OF X_256 on reference triangle ABC."""
    X_57 = eval_trilinear_point(model, A, B, C, '1/(b + c - a)', ID="X_57", classes=["center"])
    X_87 = eval_trilinear_point(model, A, B, C, '1/(a*b + a*c - b*c)', ID="X_87", classes=["center"])
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center"])
    X_256 = eval_trilinear_point(model, A, B, C, '1/(a**(2) + b*c)', ID="X_256", classes=["center"])
    central_line(model, X_57, X_87, 57, 87)
    central_line(model, X_1, X_256, 1, 256)
    X_1431 = intersect_lines(model, X_57, X_87, X_1, X_256, ID="X_1431", classes=["selected", "target"])
    X_65 = eval_trilinear_point(model, A, B, C, 'cos(B) + cos(C)', ID="X_65", classes=["center", "incident"])
    X_257 = eval_trilinear_point(model, A, B, C, '1/(a**(3) + a*b*c)', ID="X_257", classes=["center", "incident"])
    central_line(model, X_65, X_257, 65, 257, incident=True)
    return promote_point_to_top(model, X_1431)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1431 on the given reference triangle."""
    model = create_model('X_1431 = X_256-BETH CONJUGATE OF X_256')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01431(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01431.json"))
    write_center_svg(
        model_acute,
        here / "x-01431.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
