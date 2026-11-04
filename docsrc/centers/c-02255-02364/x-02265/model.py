"""GEOMETOR construction model for X_2265 = X_2-ISOCONJUGATE OF X_953."""

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
    promote_point_to_top,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_02265(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2265 = X_2-ISOCONJUGATE OF X_953 on reference triangle ABC."""
    X_9 = mittenpunkt_of(model, A, B, C, ID="X_9", classes=["center"])
    X_48 = eval_trilinear_point(model, A, B, C, 'tan(B) + tan(C)', ID="X_48", classes=["center"])
    X_44 = eval_trilinear_point(model, A, B, C, 'b + c - 2*a', ID="X_44", classes=["center"])
    X_513 = eval_trilinear_point(model, A, B, C, 'b - c', ID="X_513", classes=["center"])
    central_line(model, X_9, X_48, 9, 48)
    central_line(model, X_44, X_513, 44, 513)
    X_2265 = intersect_lines(model, X_9, X_48, X_44, X_513, ID="X_2265", classes=["selected", "target"])
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center", "incident"])
    X_1411 = eval_trilinear_point(model, A, B, C, '(1 - cos(A))/(1 - 2*cos(A))', ID="X_1411", classes=["center", "incident"])
    central_line(model, X_6, X_1411, 6, 1411, incident=True)
    return promote_point_to_top(model, X_2265)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2265 on the given reference triangle."""
    model = create_model('X_2265 = X_2-ISOCONJUGATE OF X_953')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02265(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02265.json"))
    write_center_svg(
        model_acute,
        here / "x-02265.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
