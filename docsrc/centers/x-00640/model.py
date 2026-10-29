"""GEOMETOR construction model for X(640) = COMPLEMENT OF X(372)."""

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
    nine_point_center_of,
    point_from_barycentrics,
    promote_point_to_top,
    reflection_in_point,
)
from geometor.etc.render import write_center_svg


def construct_x_00640(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(640) = COMPLEMENT OF X(372) on reference triangle ABC."""
    X_639 = point_from_barycentrics(model, A, B, C, 0.35035787, 0.32442401, 0.32521812, ID="X(639)", classes=["center"])
    X_626 = eval_trilinear_point(model, A, B, C, '(b**(4) + c**(4))/a', ID="X(626)", classes=["center"])
    X_640 = reflection_in_point(model, X_639, X_626, ID="X(640)", classes=["selected", "target"], guide=False)
    X_5 = nine_point_center_of(model, A, B, C, ID="X(5)", classes=["center", "incident"])
    X_141 = eval_trilinear_point(model, A, B, C, 'b*c*(b**(2) + c**(2))', ID="X(141)", classes=["center", "incident"])
    central_line(model, X_5, X_141, 5, 141, incident=True)
    X_2 = centroid_of(model, A, B, C, ID="X(2)", classes=["center", "incident"])
    X_372 = eval_trilinear_point(model, A, B, C, 'cos(A + pi /4)', ID="X(372)", classes=["center", "incident"])
    central_line(model, X_2, X_372, 2, 372, incident=True)
    X_69 = eval_trilinear_point(model, A, B, C, '(cos(A))/a**(2)', ID="X(69)", classes=["center", "incident"])
    X_486 = eval_trilinear_point(model, A, B, C, 'sec(A + pi /4)', ID="X(486)", classes=["center", "incident"])
    central_line(model, X_69, X_486, 69, 486, incident=True)
    return promote_point_to_top(model, X_640)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(640) on the given reference triangle."""
    model = create_model('X(640) = COMPLEMENT OF X(372)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00640(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00640.json"))
    write_center_svg(
        model_acute,
        here / "x-00640.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
