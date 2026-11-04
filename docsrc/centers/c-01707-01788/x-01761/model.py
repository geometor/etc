"""GEOMETOR construction model for X_1761 = MIMOSA TRANSFORM OF X_306."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    ceva_conjugate,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    incenter_of,
    mittenpunkt_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_01761(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1761 = MIMOSA TRANSFORM OF X_306 on reference triangle ABC."""
    X_321 = eval_trilinear_point(model, A, B, C, '(b + c)*b**(2)*c**(2)', ID="X_321", classes=["center"])
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center"])
    X_1761 = ceva_conjugate(model, A, B, C, X_321, X_1, ID="X_1761", classes=["selected", "target"])
    X_19 = eval_trilinear_point(model, A, B, C, 'tan(A)', ID="X_19", classes=["center", "incident"])
    X_27 = eval_trilinear_point(model, A, B, C, '(sec(A))/(b + c)', ID="X_27", classes=["center", "incident"])
    central_line(model, X_19, X_27, 19, 27, incident=True)
    X_9 = mittenpunkt_of(model, A, B, C, ID="X_9", classes=["center", "incident"])
    X_46 = eval_trilinear_point(model, A, B, C, 'cos(B) + cos(C) - cos(A)', ID="X_46", classes=["center", "incident"])
    central_line(model, X_9, X_46, 9, 46, incident=True)
    X_37 = eval_trilinear_point(model, A, B, C, 'b + c', ID="X_37", classes=["center", "incident"])
    X_171 = eval_trilinear_point(model, A, B, C, 'a**(2) + b*c', ID="X_171", classes=["center", "incident"])
    central_line(model, X_37, X_171, 37, 171, incident=True)
    return promote_point_to_top(model, X_1761)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1761 on the given reference triangle."""
    model = create_model('X_1761 = MIMOSA TRANSFORM OF X_306')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01761(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01761.json"))
    write_center_svg(
        model_acute,
        here / "x-01761.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
