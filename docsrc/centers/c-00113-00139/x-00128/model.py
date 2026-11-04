"""GEOMETOR construction model for X_128 = X_74-OF-ORTHIC-TRIANGLE."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    nine_point_center_of,
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00128(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_128 = X_74-OF-ORTHIC-TRIANGLE on reference triangle ABC."""
    X_128 = eval_trilinear_point(model, A, B, C, '((sec(A))*(cos(2*B) + cos(2*C))*(1 + 2*cos(2*A))*(cos(2*A) + 2*cos(2*B)*cos(2*C)))', ID="X_128", classes=["selected", "target"])
    X_5 = nine_point_center_of(model, A, B, C, ID="X_5", classes=["center", "incident"])
    X_137 = point_from_barycentrics(model, A, B, C, 0.1354431, 0.64976082, 0.21479608, ID="X_137", classes=["center", "incident"])
    central_line(model, X_5, X_137, 5, 137, incident=True)
    X_52 = eval_trilinear_point(model, A, B, C, 'cos(2*A)*cos(B - C)', ID="X_52", classes=["center", "incident"])
    X_134 = point_from_barycentrics(model, A, B, C, -0.00015640921, 0.2405092, 0.75964721, ID="X_134", classes=["center", "incident"])
    central_line(model, X_52, X_134, 52, 134, incident=True)
    X_53 = eval_trilinear_point(model, A, B, C, 'tan(A)*cos(B - C)', ID="X_53", classes=["center", "incident"])
    X_139 = point_from_barycentrics(model, A, B, C, 0.0028749347, 0.23097013, 0.76615493, ID="X_139", classes=["center", "incident"])
    central_line(model, X_53, X_139, 53, 139, incident=True)
    return promote_point_to_top(model, X_128)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_128 on the given reference triangle."""
    model = create_model('X_128 = X_74-OF-ORTHIC-TRIANGLE')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00128(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00128.json"))
    write_center_svg(
        model_acute,
        here / "x-00128.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
