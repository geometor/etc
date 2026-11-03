"""GEOMETOR construction model for X_649 = CROSSDIFFERENCE OF X_1 and X_2."""

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


def construct_x_00649(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_649 = CROSSDIFFERENCE OF X_1 and X_2 on reference triangle ABC."""
    X_190 = eval_trilinear_point(model, A, B, C, 'b*c/(b - c)', ID="X_190", classes=["center"])
    X_649 = isogonal_conjugate(model, A, B, C, X_190, ID="X_649", classes=["selected", "target"])
    X_187 = eval_trilinear_point(model, A, B, C, 'a*(2*a**(2) - b**(2) - c**(2))', ID="X_187", classes=["center", "incident"])
    X_237 = eval_trilinear_point(model, A, B, C, 'a**(2)*cos(A + omega )', ID="X_237", classes=["center", "incident"])
    central_line(model, X_187, X_237, 187, 237, incident=True)
    X_44 = eval_trilinear_point(model, A, B, C, 'b + c - 2*a', ID="X_44", classes=["center", "incident"])
    X_513 = eval_trilinear_point(model, A, B, C, 'b - c', ID="X_513", classes=["center", "incident"])
    central_line(model, X_44, X_513, 44, 513, incident=True)
    X_239 = eval_trilinear_point(model, A, B, C, 'b*c*(a**(2) - b*c)', ID="X_239", classes=["center", "incident"])
    X_514 = eval_trilinear_point(model, A, B, C, '(b - c)/a', ID="X_514", classes=["center", "incident"])
    central_line(model, X_239, X_514, 239, 514, incident=True)
    return promote_point_to_top(model, X_649)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_649 on the given reference triangle."""
    model = create_model('X_649 = CROSSDIFFERENCE OF X_1 and X_2')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00649(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00649.json"))
    write_center_svg(
        model_acute,
        here / "x-00649.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
