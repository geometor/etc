"""GEOMETOR construction model for X_2153 = X_2-ISOCONJUGATE OF X_15."""

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
    promote_point_to_top,
    spieker_center_of,
)
from geometor.etc.render import write_center_svg


def construct_x_02153(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2153 = X_2-ISOCONJUGATE OF X_15 on reference triangle ABC."""
    X_2153 = eval_trilinear_point(model, A, B, C, '(sin(A)*csc(A +  pi  /3))', ID="X_2153", classes=["selected", "target"])
    X_10 = spieker_center_of(model, A, B, C, ID="X_10", classes=["center", "incident"])
    X_13 = eval_trilinear_point(model, A, B, C, 'csc(A +  pi  /3)', ID="X_13", classes=["center", "incident"])
    central_line(model, X_10, X_13, 10, 13, incident=True)
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center", "incident"])
    X_1094 = eval_trilinear_point(model, A, B, C, '((sin(A +  pi  /3))**(2))', ID="X_1094", classes=["center", "incident"])
    central_line(model, X_1, X_1094, 1, 1094, incident=True)
    X_37 = eval_trilinear_point(model, A, B, C, 'b + c', ID="X_37", classes=["center", "incident"])
    X_1250 = eval_trilinear_point(model, A, B, C, '(cos(A/2)*cos(A/2 +  pi  /6))', ID="X_1250", classes=["center", "incident"])
    central_line(model, X_37, X_1250, 37, 1250, incident=True)
    return promote_point_to_top(model, X_2153)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2153 on the given reference triangle."""
    model = create_model('X_2153 = X_2-ISOCONJUGATE OF X_15')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02153(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02153.json"))
    write_center_svg(
        model_acute,
        here / "x-02153.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
