"""GEOMETOR construction model for X(625) = MIDPOINT OF X(623) AND X(624)."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    centroid_of,
    complement,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    nine_point_center_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00625(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(625) = MIDPOINT OF X(623) AND X(624) on reference triangle ABC."""
    X_187 = eval_trilinear_point(model, A, B, C, 'a*(2*a**(2) - b**(2) - c**(2))', ID="X(187)", classes=["center"])
    X_625 = complement(model, A, B, C, X_187, ID="X(625)", classes=["selected", "target"])
    X_5 = nine_point_center_of(model, A, B, C, ID="X(5)", classes=["center", "incident"])
    X_141 = eval_trilinear_point(model, A, B, C, 'b*c*(b**(2) + c**(2))', ID="X(141)", classes=["center", "incident"])
    central_line(model, X_5, X_141, 5, 141, incident=True)
    X_2 = centroid_of(model, A, B, C, ID="X(2)", classes=["center", "incident"])
    central_line(model, X_2, X_187, 2, 187, incident=True)
    X_115 = eval_trilinear_point(model, A, B, C, 'b*c*(b**(2) - c**(2))**(2)', ID="X(115)", classes=["center", "incident"])
    X_325 = eval_trilinear_point(model, A, B, C, 'b*c*(b**(4) + c**(4) - a**(2)*b**(2) - a**(2)*c**(2))', ID="X(325)", classes=["center", "incident"])
    central_line(model, X_115, X_325, 115, 325, incident=True)
    return promote_point_to_top(model, X_625)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(625) on the given reference triangle."""
    model = create_model('X(625) = MIDPOINT OF X(623) AND X(624)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00625(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00625.json"))
    write_center_svg(
        model_acute,
        here / "x-00625.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
