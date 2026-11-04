"""GEOMETOR construction model for X_2164 = X_2-ISOCONJUGATE OF X_46."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    intersect_lines,
    mittenpunkt_of,
    point_from_barycentrics,
    promote_point_to_top,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_02164(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2164 = X_2-ISOCONJUGATE OF X_46 on reference triangle ABC."""
    X_9 = mittenpunkt_of(model, A, B, C, ID="X_9", classes=["center"])
    X_35 = eval_trilinear_point(model, A, B, C, '1 + 2*cos(A)', ID="X_35", classes=["center"])
    X_571 = eval_trilinear_point(model, A, B, C, 'sin(A)*cos(2*A)', ID="X_571", classes=["center"])
    X_607 = eval_trilinear_point(model, A, B, C, 'a*(1 + sec(A))', ID="X_607", classes=["center"])
    central_line(model, X_9, X_35, 9, 35)
    central_line(model, X_571, X_607, 571, 607)
    X_2164 = intersect_lines(model, X_9, X_35, X_571, X_607, ID="X_2164", classes=["selected", "target"])
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center", "incident"])
    X_1195 = point_from_barycentrics(model, A, B, C, 0.19476988, 0.33920828, 0.46602184, ID="X_1195", classes=["center", "incident"])
    central_line(model, X_6, X_1195, 6, 1195, incident=True)
    return promote_point_to_top(model, X_2164)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2164 on the given reference triangle."""
    model = create_model('X_2164 = X_2-ISOCONJUGATE OF X_46')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02164(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02164.json"))
    write_center_svg(
        model_acute,
        here / "x-02164.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
