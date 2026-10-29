"""GEOMETOR construction model for X(560) = 4th POWER POINT."""

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
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00560(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(560) = 4th POWER POINT on reference triangle ABC."""
    X_560 = eval_trilinear_point(model, A, B, C, 'a**(4)', ID="X(560)", classes=["selected", "target"])
    X_31 = eval_trilinear_point(model, A, B, C, 'a**(2)', ID="X(31)", classes=["center", "incident"])
    X_48 = eval_trilinear_point(model, A, B, C, 'tan(B) + tan(C)', ID="X(48)", classes=["center", "incident"])
    central_line(model, X_31, X_48, 31, 48, incident=True)
    X_1 = incenter_of(model, A, B, C, ID="X(1)", classes=["center", "incident"])
    X_82 = eval_trilinear_point(model, A, B, C, '1/(b**(2) + c**(2))', ID="X(82)", classes=["center", "incident"])
    central_line(model, X_1, X_82, 1, 82, incident=True)
    X_42 = eval_trilinear_point(model, A, B, C, 'a*(b + c)', ID="X(42)", classes=["center", "incident"])
    X_584 = point_from_barycentrics(model, A, B, C, 0.28522764, 0.34649075, 0.3682816, ID="X(584)", classes=["center", "incident"])
    central_line(model, X_42, X_584, 42, 584, incident=True)
    return promote_point_to_top(model, X_560)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(560) on the given reference triangle."""
    model = create_model('X(560) = 4th POWER POINT')
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
