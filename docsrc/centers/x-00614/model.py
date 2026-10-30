"""GEOMETOR construction model for X(614) = INTERSECTION OF LINES X(1)X(2) AND X(11)X(33)."""

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
    incenter_of,
    mittenpunkt_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00614(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(614) = INTERSECTION OF LINES X(1)X(2) AND X(11)X(33) on reference triangle ABC."""
    X_614 = eval_trilinear_point(model, A, B, C, 'a**(2) + b**(2) + c**(2) - 2*b*c', ID="X(614)", classes=["selected", "target"])
    X_1 = incenter_of(model, A, B, C, ID="X(1)", classes=["center", "incident"])
    X_2 = centroid_of(model, A, B, C, ID="X(2)", classes=["center", "incident"])
    central_line(model, X_1, X_2, 1, 2, incident=True)
    X_11 = feuerbach_point_of(model, A, B, C, ID="X(11)", classes=["center", "incident"])
    X_33 = eval_trilinear_point(model, A, B, C, '1 + sec(A)', ID="X(33)", classes=["center", "incident"])
    central_line(model, X_11, X_33, 11, 33, incident=True)
    X_9 = mittenpunkt_of(model, A, B, C, ID="X(9)", classes=["center", "incident"])
    X_38 = eval_trilinear_point(model, A, B, C, 'b**(2) + c**(2)', ID="X(38)", classes=["center", "incident"])
    central_line(model, X_9, X_38, 9, 38, incident=True)
    return promote_point_to_top(model, X_614)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(614) on the given reference triangle."""
    model = create_model('X(614) = INTERSECTION OF LINES X(1)X(2) AND X(11)X(33)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00614(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00614.json"))
    write_center_svg(
        model_acute,
        here / "x-00614.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
