"""GEOMETOR construction model for X_2313 = X_2-ISOCONJUGATE OF X_1298."""

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
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_02313(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2313 = X_2-ISOCONJUGATE OF X_1298 on reference triangle ABC."""
    X_48 = eval_trilinear_point(model, A, B, C, 'tan(B) + tan(C)', ID="X_48", classes=["center"])
    X_92 = eval_trilinear_point(model, A, B, C, 'csc(2*A)', ID="X_92", classes=["center"])
    X_44 = eval_trilinear_point(model, A, B, C, 'b + c - 2*a', ID="X_44", classes=["center"])
    X_513 = eval_trilinear_point(model, A, B, C, 'b - c', ID="X_513", classes=["center"])
    central_line(model, X_48, X_92, 48, 92)
    central_line(model, X_44, X_513, 44, 513)
    X_2313 = intersect_lines(model, X_48, X_92, X_44, X_513, ID="X_2313", classes=["selected", "target"])
    X_1953 = eval_trilinear_point(model, A, B, C, 'sin(2*B) + sin(2*C)', ID="X_1953", classes=["center", "incident"])
    X_2181 = point_from_barycentrics(model, A, B, C, 0.075264897, 0.15223097, 0.77250413, ID="X_2181", classes=["center", "incident"])
    central_line(model, X_1953, X_2181, 1953, 2181, incident=True)
    return promote_point_to_top(model, X_2313)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2313 on the given reference triangle."""
    model = create_model('X_2313 = X_2-ISOCONJUGATE OF X_1298')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02313(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02313.json"))
    write_center_svg(
        model_acute,
        here / "x-02313.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
