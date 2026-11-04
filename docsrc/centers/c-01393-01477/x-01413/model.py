"""GEOMETOR construction model for X_1413 = X_84-BETH CONJUGATE OF X_84."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    crosspoint,
    eval_trilinear_point,
    incenter_of,
    point_from_barycentrics,
    promote_point_to_top,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_01413(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1413 = X_84-BETH CONJUGATE OF X_84 on reference triangle ABC."""
    X_84 = eval_trilinear_point(model, A, B, C, '1/(cos(B) + cos(C) - cos(A) - 1)', ID="X_84", classes=["center"])
    X_1256 = point_from_barycentrics(model, A, B, C, 0.0024481835, 0.0070167771, 0.99053504, ID="X_1256", classes=["center"])
    X_1413 = crosspoint(model, A, B, C, X_84, X_1256, ID="X_1413", classes=["selected", "target"])
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center", "incident"])
    central_line(model, X_1, X_84, 1, 84, incident=True)
    X_86 = eval_trilinear_point(model, A, B, C, 'b*c/(b + c)', ID="X_86", classes=["center", "incident"])
    X_285 = eval_trilinear_point(model, A, B, C, '(1/((cos(B) + cos(C))*(-1 - cos(A) + cos(B) + cos(C))))', ID="X_285", classes=["center", "incident"])
    central_line(model, X_86, X_285, 86, 285, incident=True)
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center", "incident"])
    X_603 = eval_trilinear_point(model, A, B, C, '(cos(A))**(2) - cos(A)', ID="X_603", classes=["center", "incident"])
    central_line(model, X_6, X_603, 6, 603, incident=True)
    return promote_point_to_top(model, X_1413)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1413 on the given reference triangle."""
    model = create_model('X_1413 = X_84-BETH CONJUGATE OF X_84')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01413(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01413.json"))
    write_center_svg(
        model_acute,
        here / "x-01413.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
