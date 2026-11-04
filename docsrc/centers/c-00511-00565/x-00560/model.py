"""GEOMETOR construction model for X_560 = 4th POWER POINT."""

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


def construct_x_00560(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_560 = 4th POWER POINT on reference triangle ABC."""
    X_560 = eval_trilinear_point(model, A, B, C, 'a**(4)', ID="X_560", classes=["selected", "target"])
    X_31 = eval_trilinear_point(model, A, B, C, 'a**(2)', ID="X_31", classes=["center", "incident"])
    X_48 = eval_trilinear_point(model, A, B, C, 'tan(B) + tan(C)', ID="X_48", classes=["center", "incident"])
    central_line(model, X_31, X_48, 31, 48, incident=True)
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center", "incident"])
    X_82 = eval_trilinear_point(model, A, B, C, '1/(b**(2) + c**(2))', ID="X_82", classes=["center", "incident"])
    central_line(model, X_1, X_82, 1, 82, incident=True)
    X_42 = eval_trilinear_point(model, A, B, C, 'a*(b + c)', ID="X_42", classes=["center", "incident"])
    X_584 = eval_trilinear_point(model, A, B, C, '(a*(a*b**(2) + a*c**(2) + b*c**(2) + b**(2)*c + 2*a*b*c - a**(3)))', ID="X_584", classes=["center", "incident"])
    central_line(model, X_42, X_584, 42, 584, incident=True)
    return promote_point_to_top(model, X_560)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_560 on the given reference triangle."""
    model = create_model('X_560 = 4th POWER POINT')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00560(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00560.json"))
    write_center_svg(
        model_acute,
        here / "x-00560.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
