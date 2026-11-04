"""GEOMETOR construction model for X_1971 = CROSSDIFFERENCE OF PU(38)."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    promote_point_to_top,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_01971(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1971 = CROSSDIFFERENCE OF PU(38) on reference triangle ABC."""
    X_1971 = eval_trilinear_point(model, A, B, C, 'a*((sin(2*A))**(2) - sin(2*B)*sin(2*C))', ID="X_1971", classes=["selected", "target"])
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center", "incident"])
    X_25 = eval_trilinear_point(model, A, B, C, 'sin(A)*tan(A)', ID="X_25", classes=["center", "incident"])
    central_line(model, X_6, X_25, 6, 25, incident=True)
    X_98 = eval_trilinear_point(model, A, B, C, 'sec(A + omega )', ID="X_98", classes=["center", "incident"])
    X_230 = eval_trilinear_point(model, A, B, C, 'b*c*(a**(2)*(2*a**(2) - b**(2) - c**(2)) + (b**(2) - c**(2))**(2))', ID="X_230", classes=["center", "incident"])
    central_line(model, X_98, X_230, 98, 230, incident=True)
    X_237 = eval_trilinear_point(model, A, B, C, 'a**(2)*cos(A + omega )', ID="X_237", classes=["center", "incident"])
    X_248 = eval_trilinear_point(model, A, B, C, 'sin(2*A)*sec(A + omega )', ID="X_248", classes=["center", "incident"])
    central_line(model, X_237, X_248, 237, 248, incident=True)
    return promote_point_to_top(model, X_1971)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1971 on the given reference triangle."""
    model = create_model('X_1971 = CROSSDIFFERENCE OF PU(38)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01971(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01971.json"))
    write_center_svg(
        model_acute,
        here / "x-01971.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
