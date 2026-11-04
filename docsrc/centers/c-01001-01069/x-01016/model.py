"""GEOMETOR construction model for X_1016 = X_1-CROSS CONJUGATE OF X_99."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    isogonal_conjugate,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_01016(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1016 = X_1-CROSS CONJUGATE OF X_99 on reference triangle ABC."""
    X_1015 = eval_trilinear_point(model, A, B, C, 'a*(b - c)**(2)', ID="X_1015", classes=["center"])
    X_1016 = isogonal_conjugate(model, A, B, C, X_1015, ID="X_1016", classes=["selected", "target"])
    X_190 = eval_trilinear_point(model, A, B, C, 'b*c/(b - c)', ID="X_190", classes=["center", "incident"])
    X_514 = eval_trilinear_point(model, A, B, C, '(b - c)/a', ID="X_514", classes=["center", "incident"])
    central_line(model, X_190, X_514, 190, 514, incident=True)
    X_238 = eval_trilinear_point(model, A, B, C, 'a**(2) - b*c', ID="X_238", classes=["center", "incident"])
    X_519 = eval_trilinear_point(model, A, B, C, '(2*a - b - c)/a', ID="X_519", classes=["center", "incident"])
    central_line(model, X_238, X_519, 238, 519, incident=True)
    X_100 = eval_trilinear_point(model, A, B, C, '1/(b - c)', ID="X_100", classes=["center", "incident"])
    X_667 = eval_trilinear_point(model, A, B, C, 'a**(2)*(b - c)', ID="X_667", classes=["center", "incident"])
    central_line(model, X_100, X_667, 100, 667, incident=True)
    return promote_point_to_top(model, X_1016)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1016 on the given reference triangle."""
    model = create_model('X_1016 = X_1-CROSS CONJUGATE OF X_99')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01016(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01016.json"))
    write_center_svg(
        model_acute,
        here / "x-01016.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
