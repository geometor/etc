"""GEOMETOR construction model for X(443) = COMPLEMENT OF X(452)."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    centroid_of,
    circumcenter_of,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    gergonne_point_of,
    intersect_lines,
    promote_point_to_top,
    spieker_center_of,
)
from geometor.etc.render import write_center_svg


def construct_x_00443(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(443) = COMPLEMENT OF X(452) on reference triangle ABC."""
    X_2 = centroid_of(model, A, B, C, ID="X(2)", classes=["center"])
    X_3 = circumcenter_of(model, A, B, C, ID="X(3)", classes=["center"])
    X_10 = spieker_center_of(model, A, B, C, ID="X(10)", classes=["center"])
    X_57 = eval_trilinear_point(model, A, B, C, '1/(b + c - a)', ID="X(57)", classes=["center"])
    central_line(model, X_2, X_3, 2, 3)
    central_line(model, X_10, X_57, 10, 57)
    X_443 = intersect_lines(model, X_2, X_3, X_10, X_57, ID="X(443)", classes=["selected", "target"])
    X_7 = gergonne_point_of(model, A, B, C, ID="X(7)", classes=["center", "incident"])
    X_72 = eval_trilinear_point(model, A, B, C, '(b + c)*cot(A)', ID="X(72)", classes=["center", "incident"])
    central_line(model, X_7, X_72, 7, 72, incident=True)
    return promote_point_to_top(model, X_443)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(443) on the given reference triangle."""
    model = create_model('X(443) = COMPLEMENT OF X(452)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00443(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00443.json"))
    write_center_svg(
        model_acute,
        here / "x-00443.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
