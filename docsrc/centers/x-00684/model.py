"""GEOMETOR construction model for X(684) = CROSSDIFFERENCE OF X(4) AND X(32)."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_barycentric_point,
    eval_trilinear_point,
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00684(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(684) = CROSSDIFFERENCE OF X(4) AND X(32) on reference triangle ABC."""
    X_684 = eval_trilinear_point(model, A, B, C, 'a*(b**(2) + c**(2) - a**(2))*(b**(2) - c**(2))*(a**(2)*b**(2) + a**(2)*c**(2) - b**(4) - c**(4))', ID="X(684)", classes=["selected", "target"])
    X_114 = eval_trilinear_point(model, A, B, C, 'b*c*(b*sec(B + omega ) + c*sec(C + omega ))', ID="X(114)", classes=["center", "incident"])
    X_132 = point_from_barycentrics(model, A, B, C, 0.11002416, 0.049913231, 0.84006261, ID="X(132)", classes=["center", "incident"])
    central_line(model, X_114, X_132, 114, 132, incident=True)
    X_122 = eval_barycentric_point(model, A, B, C, '(b**(2) - c**(2))**(2)*(a**(2) - b**(2) - c**(2))**(2)*(3*a**(4) - 2*a**(2)*(b**(2) + c**(2)) - (b**(2) - c**(2))**(2))', ID="X(122)", classes=["center", "incident"])
    X_125 = eval_trilinear_point(model, A, B, C, 'cos(A)*(sin(B - C))**(2)', ID="X(125)", classes=["center", "incident"])
    central_line(model, X_122, X_125, 122, 125, incident=True)
    X_110 = eval_trilinear_point(model, A, B, C, 'csc(B - C)', ID="X(110)", classes=["center", "incident"])
    X_351 = point_from_barycentrics(model, A, B, C, -1.104798, 0.16783217, 1.9369658, ID="X(351)", classes=["center", "incident"])
    central_line(model, X_110, X_351, 110, 351, incident=True)
    return promote_point_to_top(model, X_684)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(684) on the given reference triangle."""
    model = create_model('X(684) = CROSSDIFFERENCE OF X(4) AND X(32)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00684(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00684.json"))
    write_center_svg(
        model_acute,
        here / "x-00684.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
