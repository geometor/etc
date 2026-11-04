"""GEOMETOR construction model for X_1640 = TRIPOLAR CENTROID OF X_98."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    centroid_of,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    promote_point_to_top,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_01640(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1640 = TRIPOLAR CENTROID OF X_98 on reference triangle ABC."""
    X_1640 = eval_trilinear_point(model, A, B, C, 'b*c*(b**(2) - c**(2))*(2*a**(6) - b**(6) - c**(6) - 2*a**(4)*b**(2) - 2*a**(4)*c**(2) + a**(2)*b**(4) + a**(2)*c**(4) + b**(4)*c**(2) + b**(2)*c**(4))', ID="X_1640", classes=["selected", "target"])
    X_115 = eval_trilinear_point(model, A, B, C, 'b*c*(b**(2) - c**(2))**(2)', ID="X_115", classes=["center", "incident"])
    X_125 = eval_trilinear_point(model, A, B, C, 'cos(A)*(sin(B - C))**(2)', ID="X_125", classes=["center", "incident"])
    central_line(model, X_115, X_125, 115, 125, incident=True)
    X_2 = centroid_of(model, A, B, C, ID="X_2", classes=["center", "incident"])
    X_525 = eval_trilinear_point(model, A, B, C, '(b*cos(B) - c*cos(C))/a', ID="X_525", classes=["center", "incident"])
    central_line(model, X_2, X_525, 2, 525, incident=True)
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center", "incident"])
    X_523 = eval_trilinear_point(model, A, B, C, 'sin(B -C)', ID="X_523", classes=["center", "incident"])
    central_line(model, X_6, X_523, 6, 523, incident=True)
    return promote_point_to_top(model, X_1640)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1640 on the given reference triangle."""
    model = create_model('X_1640 = TRIPOLAR CENTROID OF X_98')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01640(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01640.json"))
    write_center_svg(
        model_acute,
        here / "x-01640.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
