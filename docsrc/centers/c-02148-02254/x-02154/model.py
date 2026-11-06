"""GEOMETOR construction model for X_2154 = X_2-ISOCONJUGATE OF X_16."""

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


def construct_x_02154(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2154 = X_2-ISOCONJUGATE OF X_16 on reference triangle ABC."""
    X_2154 = eval_trilinear_point(model, A, B, C, '(sin(A)*csc(A -  pi  /3))', ID="X_2154", classes=["selected", "target"])
    X_10 = spieker_center_of(model, A, B, C, ID="X_10", classes=["center", "incident"])
    X_14 = eval_trilinear_point(model, A, B, C, 'csc(A -  pi  /3)', ID="X_14", classes=["center", "incident"])
    central_line(model, X_10, X_14, 10, 14, incident=True)
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center", "incident"])
    X_1095 = eval_trilinear_point(model, A, B, C, '((sin(A -  pi  /3))**(2))', ID="X_1095", classes=["center", "incident"])
    central_line(model, X_1, X_1095, 1, 1095, incident=True)
    X_31 = eval_trilinear_point(model, A, B, C, 'a**(2)', ID="X_31", classes=["center", "incident"])
    X_2153 = eval_trilinear_point(model, A, B, C, '(sin(A)*csc(A +  pi  /3))', ID="X_2153", classes=["center", "incident"])
    central_line(model, X_31, X_2153, 31, 2153, incident=True)
    return promote_point_to_top(model, X_2154)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2154 on the given reference triangle."""
    model = create_model('X_2154 = X_2-ISOCONJUGATE OF X_16')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02154(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02154.json"))
    write_center_svg(
        model_acute,
        here / "x-02154.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
