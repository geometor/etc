"""GEOMETOR construction model for X_2608 = TRILINEAR POLE OF PU(70)."""

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
    isogonal_conjugate,
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_02608(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2608 = TRILINEAR POLE OF PU(70) on reference triangle ABC."""
    X_2607 = eval_trilinear_point(model, A, B, C, 'sin(A - B)*sin(A - C) + (sin(B - C))**(2)', ID="X_2607", classes=["center"])
    X_2608 = isogonal_conjugate(model, A, B, C, X_2607, ID="X_2608", classes=["selected", "target"])
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center", "incident"])
    X_2614 = eval_trilinear_point(model, A, B, C, '(1/(csc(A - B)*csc(A - C) + (csc(B - C))**(2)))', ID="X_2614", classes=["center", "incident"])
    central_line(model, X_1, X_2614, 1, 2614, incident=True)
    X_2606 = eval_trilinear_point(model, A, B, C, 'sin(A - B)*sin(A - C) - (sin(B - C))**(2)', ID="X_2606", classes=["center", "incident"])
    X_2611 = point_from_barycentrics(model, A, B, C, 0.21464646, 0.68065268, 0.10470085, ID="X_2611", classes=["center", "incident"])
    central_line(model, X_2606, X_2611, 2606, 2611, incident=True)
    return promote_point_to_top(model, X_2608)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2608 on the given reference triangle."""
    model = create_model('X_2608 = TRILINEAR POLE OF PU(70)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02608(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02608.json"))
    write_center_svg(
        model_acute,
        here / "x-02608.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
