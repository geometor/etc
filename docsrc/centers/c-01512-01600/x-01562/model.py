"""GEOMETOR construction model for X_1562 = ORTHOJOIN OF X_520."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    ceva_conjugate,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_01562(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1562 = ORTHOJOIN OF X_520 on reference triangle ABC."""
    X_393 = eval_trilinear_point(model, A, B, C, 'b*c*(tan(A))**(2)', ID="X_393", classes=["center"])
    X_647 = eval_trilinear_point(model, A, B, C, 'a*(b**(2) - c**(2))*(b**(2) + c**(2) - a**(2))', ID="X_647", classes=["center"])
    X_1562 = ceva_conjugate(model, A, B, C, X_393, X_647, ID="X_1562", classes=["selected", "target"])
    X_115 = eval_trilinear_point(model, A, B, C, 'b*c*(b**(2) - c**(2))**(2)', ID="X_115", classes=["center", "incident"])
    X_125 = eval_trilinear_point(model, A, B, C, 'cos(A)*(sin(B - C))**(2)', ID="X_125", classes=["center", "incident"])
    central_line(model, X_115, X_125, 115, 125, incident=True)
    X_148 = eval_trilinear_point(model, A, B, C, 'b*c*(a**(4) - (b**(2) - c**(2))**(2) + b**(2)*c**(2) - a**(2)*b**(2) - a**(2)*c**(2))', ID="X_148", classes=["center", "incident"])
    X_287 = eval_trilinear_point(model, A, B, C, 'cot(A)*sec(A +  omega  )', ID="X_287", classes=["center", "incident"])
    central_line(model, X_148, X_287, 148, 287, incident=True)
    X_127 = eval_trilinear_point(model, A, B, C, 'b*c*(sin(2*B) - sin(2*C))*((b**(2) - c**(2))*sin(2*A) - b**(2)*sin(2*B) + c**(2)*sin(2*C))', ID="X_127", classes=["center", "incident"])
    X_525 = eval_trilinear_point(model, A, B, C, '(b*cos(B) - c*cos(C))/a', ID="X_525", classes=["center", "incident"])
    central_line(model, X_127, X_525, 127, 525, incident=True)
    return promote_point_to_top(model, X_1562)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1562 on the given reference triangle."""
    model = create_model('X_1562 = ORTHOJOIN OF X_520')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01562(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01562.json"))
    write_center_svg(
        model_acute,
        here / "x-01562.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
