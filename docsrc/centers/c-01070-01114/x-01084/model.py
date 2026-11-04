"""GEOMETOR construction model for X_1084 = CROSSPOINT OF X_2 AND X_512."""

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
    promote_point_to_top,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_01084(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1084 = CROSSPOINT OF X_2 AND X_512 on reference triangle ABC."""
    X_670 = eval_trilinear_point(model, A, B, C, '1/(a**(3)*(b**(2) - c**(2)))', ID="X_670", classes=["center"])
    X_1084 = complement(model, A, B, C, X_670, ID="X_1084", classes=["selected", "target"])
    X_39 = eval_trilinear_point(model, A, B, C, 'a*(b**(2) + c**(2))', ID="X_39", classes=["center", "incident"])
    X_597 = eval_trilinear_point(model, A, B, C, '(4*a**(2) + b**(2) + c**(2))/a', ID="X_597", classes=["center", "incident"])
    central_line(model, X_39, X_597, 39, 597, incident=True)
    X_2 = centroid_of(model, A, B, C, ID="X_2", classes=["center", "incident"])
    central_line(model, X_2, X_670, 2, 670, incident=True)
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center", "incident"])
    X_694 = eval_trilinear_point(model, A, B, C, 'a/(a**(4) - b**(2)*c**(2))', ID="X_694", classes=["center", "incident"])
    central_line(model, X_6, X_694, 6, 694, incident=True)
    return promote_point_to_top(model, X_1084)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1084 on the given reference triangle."""
    model = create_model('X_1084 = CROSSPOINT OF X_2 AND X_512')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01084(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01084.json"))
    write_center_svg(
        model_acute,
        here / "x-01084.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
