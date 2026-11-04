"""GEOMETOR construction model for X_2640 = CROSSSUM OF PU(78)."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    circumcenter_of,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    incenter_of,
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_02640(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2640 = CROSSSUM OF PU(78) on reference triangle ABC."""
    X_2640 = eval_trilinear_point(model, A, B, C, '(cot(A) - cot(B))*(cot(A) - cot(C)) - (cot(B) - cot(C))**(2)', ID="X_2640", classes=["selected", "target"])
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center", "incident"])
    X_662 = eval_trilinear_point(model, A, B, C, '1/(cot(B) - cot(C))', ID="X_662", classes=["center", "incident"])
    central_line(model, X_1, X_662, 1, 662, incident=True)
    X_45 = eval_trilinear_point(model, A, B, C, '2*b + 2*c - a', ID="X_45", classes=["center", "incident"])
    X_846 = eval_trilinear_point(model, A, B, C, '(- a**(2) + b**(2) + c**(2) + b*c + c*a + a*b)', ID="X_846", classes=["center", "incident"])
    central_line(model, X_45, X_846, 45, 846, incident=True)
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center", "incident"])
    X_1247 = point_from_barycentrics(model, A, B, C, 0.47979502, 0.29838347, 0.22182151, ID="X_1247", classes=["center", "incident"])
    central_line(model, X_3, X_1247, 3, 1247, incident=True)
    return promote_point_to_top(model, X_2640)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2640 on the given reference triangle."""
    model = create_model('X_2640 = CROSSSUM OF PU(78)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02640(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02640.json"))
    write_center_svg(
        model_acute,
        here / "x-02640.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
