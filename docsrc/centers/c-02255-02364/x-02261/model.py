"""GEOMETOR construction model for X_2261 = X_2-ISOCONJUGATE OF X_945."""

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


def construct_x_02261(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2261 = X_2-ISOCONJUGATE OF X_945 on reference triangle ABC."""
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center"])
    X_19 = eval_trilinear_point(model, A, B, C, 'tan(A)', ID="X_19", classes=["center"])
    X_9 = mittenpunkt_of(model, A, B, C, ID="X_9", classes=["center"])
    X_48 = eval_trilinear_point(model, A, B, C, 'tan(B) + tan(C)', ID="X_48", classes=["center"])
    central_line(model, X_6, X_19, 6, 19)
    central_line(model, X_9, X_48, 9, 48)
    X_2261 = intersect_lines(model, X_6, X_19, X_9, X_48, ID="X_2261", classes=["selected", "target"])
    X_33 = eval_trilinear_point(model, A, B, C, '1 + sec(A)', ID="X_33", classes=["center", "incident"])
    X_184 = eval_trilinear_point(model, A, B, C, 'a**(2)*cos(A)', ID="X_184", classes=["center", "incident"])
    central_line(model, X_33, X_184, 33, 184, incident=True)
    return promote_point_to_top(model, X_2261)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2261 on the given reference triangle."""
    model = create_model('X_2261 = X_2-ISOCONJUGATE OF X_945')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02261(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02261.json"))
    write_center_svg(
        model_acute,
        here / "x-02261.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
