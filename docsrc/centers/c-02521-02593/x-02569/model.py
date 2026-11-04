"""GEOMETOR construction model for X_2569 = EXSIMILICENTER(SPIEKER CIRCLE, 2nd BROCARD CIRCLE)."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    centroid_of,
    circumcenter_of,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    nagel_point_of,
    promote_point_to_top,
    spieker_center_of,
)
from geometor.etc.render import write_center_svg


def construct_x_02569(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2569 = EXSIMILICENTER(SPIEKER CIRCLE, 2nd BROCARD CIRCLE) on reference triangle ABC."""
    X_2569 = eval_trilinear_point(model, A, B, C, '(b*c*((b + c)*e - a*cos(A)))', ID="X_2569", classes=["selected", "target"])
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center", "incident"])
    X_10 = spieker_center_of(model, A, B, C, ID="X_10", classes=["center", "incident"])
    central_line(model, X_3, X_10, 3, 10, incident=True)
    X_2 = centroid_of(model, A, B, C, ID="X_2", classes=["center", "incident"])
    X_2564 = eval_trilinear_point(model, A, B, C, '(e + cos(A))', ID="X_2564", classes=["center", "incident"])
    central_line(model, X_2, X_2564, 2, 2564, incident=True)
    X_8 = nagel_point_of(model, A, B, C, ID="X_8", classes=["center", "incident"])
    X_2565 = eval_trilinear_point(model, A, B, C, '(e - cos(A))', ID="X_2565", classes=["center", "incident"])
    central_line(model, X_8, X_2565, 8, 2565, incident=True)
    return promote_point_to_top(model, X_2569)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2569 on the given reference triangle."""
    model = create_model('X_2569 = EXSIMILICENTER(SPIEKER CIRCLE, 2nd BROCARD CIRCLE)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02569(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02569.json"))
    write_center_svg(
        model_acute,
        here / "x-02569.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
