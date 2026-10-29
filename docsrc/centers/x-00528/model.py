"""GEOMETOR construction model for X(528) = DIRECTION OF VECTOR AX + BX + CX, where X = X(11)."""

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
    feuerbach_point_of,
    intersect_lines,
    mittenpunkt_of,
    nagel_point_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00528(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(528) = DIRECTION OF VECTOR AX + BX + CX, where X = X(11) on reference triangle ABC."""
    X_2 = centroid_of(model, A, B, C, ID="X(2)", classes=["center"])
    X_11 = feuerbach_point_of(model, A, B, C, ID="X(11)", classes=["center"])
    X_9 = mittenpunkt_of(model, A, B, C, ID="X(9)", classes=["center"])
    X_80 = eval_trilinear_point(model, A, B, C, '1/(1 - 2*cos(A))', ID="X(80)", classes=["center"])
    central_line(model, X_2, X_11, 2, 11)
    central_line(model, X_9, X_80, 9, 80)
    X_528 = intersect_lines(model, X_2, X_11, X_9, X_80, ID="X(528)", classes=["selected", "target"])
    X_8 = nagel_point_of(model, A, B, C, ID="X(8)", classes=["center", "incident"])
    X_190 = eval_trilinear_point(model, A, B, C, 'b*c/(b - c)', ID="X(190)", classes=["center", "incident"])
    central_line(model, X_8, X_190, 8, 190, incident=True)
    return promote_point_to_top(model, X_528)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(528) on the given reference triangle."""
    model = create_model('X(528) = DIRECTION OF VECTOR AX + BX + CX, where X = X(11)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00528(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00528.json"))
    write_center_svg(
        model_acute,
        here / "x-00528.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
