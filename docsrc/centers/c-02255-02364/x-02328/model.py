"""GEOMETOR construction model for X_2328 = X_2-ISOCONJUGATE OF X_1427."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    incenter_of,
    mittenpunkt_of,
    promote_point_to_top,
    spieker_center_of,
)
from geometor.etc.render import write_center_svg


def construct_x_02328(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2328 = X_2-ISOCONJUGATE OF X_1427 on reference triangle ABC."""
    X_2328 = eval_trilinear_point(model, A, B, C, '(1 + cos(A))/(cos(B) + cos(C))', ID="X_2328", classes=["selected", "target"])
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center", "incident"])
    X_21 = eval_trilinear_point(model, A, B, C, '1/(cos(B) + cos(C))', ID="X_21", classes=["center", "incident"])
    central_line(model, X_1, X_21, 1, 21, incident=True)
    X_10 = spieker_center_of(model, A, B, C, ID="X_10", classes=["center", "incident"])
    X_29 = eval_trilinear_point(model, A, B, C, '(sec(A))/(cos(B) + cos(C))', ID="X_29", classes=["center", "incident"])
    central_line(model, X_10, X_29, 10, 29, incident=True)
    X_9 = mittenpunkt_of(model, A, B, C, ID="X_9", classes=["center", "incident"])
    X_33 = eval_trilinear_point(model, A, B, C, '1 + sec(A)', ID="X_33", classes=["center", "incident"])
    central_line(model, X_9, X_33, 9, 33, incident=True)
    return promote_point_to_top(model, X_2328)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2328 on the given reference triangle."""
    model = create_model('X_2328 = X_2-ISOCONJUGATE OF X_1427')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02328(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02328.json"))
    write_center_svg(
        model_acute,
        here / "x-02328.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
