"""GEOMETOR construction model for X(698) = EVEN (- 4, - 2) INFINITY POINT."""

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
    promote_point_to_top,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_00698(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(698) = EVEN (- 4, - 2) INFINITY POINT on reference triangle ABC."""
    X_698 = eval_barycentric_point(model, A, B, C, 'a**(2)*b**(4) + a**(2)*c**(4) - b**(4)*c**(2) - b**(2)*c**(4)', ID="X(698)", classes=["selected", "target"])
    X_6 = symmedian_point_of(model, A, B, C, ID="X(6)", classes=["center", "incident"])
    X_194 = eval_trilinear_point(model, A, B, C, 'b*c*(a**(2)*b**(2) + a**(2)*c**(2) - b**(2)*c**(2))', ID="X(194)", classes=["center", "incident"])
    central_line(model, X_6, X_194, 6, 194, incident=True)
    X_76 = eval_trilinear_point(model, A, B, C, '1/a**(3)', ID="X(76)", classes=["center", "incident"])
    X_141 = eval_trilinear_point(model, A, B, C, 'b*c*(b**(2) + c**(2))', ID="X(141)", classes=["center", "incident"])
    central_line(model, X_76, X_141, 76, 141, incident=True)
    X_75 = eval_trilinear_point(model, A, B, C, '1/a**(2)', ID="X(75)", classes=["center", "incident"])
    X_257 = eval_trilinear_point(model, A, B, C, '1/(a**(3) + a*b*c)', ID="X(257)", classes=["center", "incident"])
    central_line(model, X_75, X_257, 75, 257, incident=True)
    return promote_point_to_top(model, X_698)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(698) on the given reference triangle."""
    model = create_model('X(698) = EVEN (- 4, - 2) INFINITY POINT')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00698(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00698.json"))
    write_center_svg(
        model_acute,
        here / "x-00698.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
