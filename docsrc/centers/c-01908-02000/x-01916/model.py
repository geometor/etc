"""GEOMETOR construction model for X_1916 = TRILINEAR POLE OF PU(11)."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    midpoint,
    orthocenter_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_01916(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1916 = TRILINEAR POLE OF PU(11) on reference triangle ABC."""
    X_148 = eval_trilinear_point(model, A, B, C, 'b*c*(a**(4) - (b**(2) - c**(2))**(2) + b**(2)*c**(2) - a**(2)*b**(2) - a**(2)*c**(2))', ID="X_148", classes=["center"])
    X_194 = eval_trilinear_point(model, A, B, C, 'b*c*(a**(2)*b**(2) + a**(2)*c**(2) - b**(2)*c**(2))', ID="X_194", classes=["center"])
    X_1916 = midpoint(model, X_148, X_194, ID="X_1916", classes=["selected", "target"], guide=False)
    X_39 = eval_trilinear_point(model, A, B, C, 'a*(b**(2) + c**(2))', ID="X_39", classes=["center", "incident"])
    X_83 = eval_trilinear_point(model, A, B, C, 'b*c/(b**(2) + c**(2))', ID="X_83", classes=["center", "incident"])
    central_line(model, X_39, X_83, 39, 83, incident=True)
    X_4 = orthocenter_of(model, A, B, C, ID="X_4", classes=["center", "incident"])
    X_147 = eval_trilinear_point(model, A, B, C, 'b*c*(a**(8) + (b**(2) + c**(2))*a**(6) - (2*b**(4) + 3*b**(2)*c**(2) + 2*c**(4))*a**(4) + (b**(6) + b**(4)*c**(2) + b**(2)*c**(4) + c**(6))*a**(2) - b**(8) + b**(6)*c**(2) + b**(2)*c**(6) - c**(8))', ID="X_147", classes=["center", "incident"])
    central_line(model, X_4, X_147, 4, 147, incident=True)
    X_76 = eval_trilinear_point(model, A, B, C, '1/a**(3)', ID="X_76", classes=["center", "incident"])
    X_115 = eval_trilinear_point(model, A, B, C, 'b*c*(b**(2) - c**(2))**(2)', ID="X_115", classes=["center", "incident"])
    central_line(model, X_76, X_115, 76, 115, incident=True)
    return promote_point_to_top(model, X_1916)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1916 on the given reference triangle."""
    model = create_model('X_1916 = TRILINEAR POLE OF PU(11)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01916(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01916.json"))
    write_center_svg(
        model_acute,
        here / "x-01916.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
