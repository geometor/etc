"""GEOMETOR construction model for X_2606 = CROSSSUM OF PU(70)."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_barycentric_point,
    eval_trilinear_point,
    incenter_of,
    nine_point_center_of,
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_02606(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2606 = CROSSSUM OF PU(70) on reference triangle ABC."""
    X_2606 = eval_trilinear_point(model, A, B, C, 'sin(A - B)*sin(A - C) - (sin(B - C))**(2)', ID="X_2606", classes=["selected", "target"])
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center", "incident"])
    X_5 = nine_point_center_of(model, A, B, C, ID="X_5", classes=["center", "incident"])
    central_line(model, X_1, X_5, 1, 5, incident=True)
    X_110 = eval_trilinear_point(model, A, B, C, 'csc(B - C)', ID="X_110", classes=["center", "incident"])
    X_1109 = eval_trilinear_point(model, A, B, C, '(sin(B - C))**(2)', ID="X_1109", classes=["center", "incident"])
    central_line(model, X_110, X_1109, 110, 1109, incident=True)
    X_542 = eval_barycentric_point(model, A, B, C, '2*a**(6) - 2*a**(4)*(b**(2) + c**(2)) + a**(2)*(b**(4) + c**(4)) - (b**(2) - c**(2))**(2)*(b**(2) + c**(2))', ID="X_542", classes=["center", "incident"])
    X_1365 = point_from_barycentrics(model, A, B, C, 0.14334182, 0.65139949, 0.20525869, ID="X_1365", classes=["center", "incident"])
    central_line(model, X_542, X_1365, 542, 1365, incident=True)
    return promote_point_to_top(model, X_2606)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2606 on the given reference triangle."""
    model = create_model('X_2606 = CROSSSUM OF PU(70)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02606(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02606.json"))
    write_center_svg(
        model_acute,
        here / "x-02606.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
