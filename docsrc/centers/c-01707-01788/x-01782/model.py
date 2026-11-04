"""GEOMETOR construction model for X_1782 = MIMOSA TRANSFORM OF X_1257."""

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
    nagel_point_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_01782(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1782 = MIMOSA TRANSFORM OF X_1257 on reference triangle ABC."""
    X_8 = nagel_point_of(model, A, B, C, ID="X_8", classes=["center"])
    X_20 = eval_trilinear_point(model, A, B, C, 'cos(A) - cos(B)*cos(C)', ID="X_20", classes=["center"])
    X_19 = eval_trilinear_point(model, A, B, C, 'tan(A)', ID="X_19", classes=["center"])
    X_46 = eval_trilinear_point(model, A, B, C, 'cos(B) + cos(C) - cos(A)', ID="X_46", classes=["center"])
    central_line(model, X_8, X_20, 8, 20)
    central_line(model, X_19, X_46, 19, 46)
    X_1782 = intersect_lines(model, X_8, X_20, X_19, X_46, ID="X_1782", classes=["selected", "target"])
    X_58 = eval_trilinear_point(model, A, B, C, 'a/(b + c)', ID="X_58", classes=["center", "incident"])
    X_65 = eval_trilinear_point(model, A, B, C, 'cos(B) + cos(C)', ID="X_65", classes=["center", "incident"])
    central_line(model, X_58, X_65, 58, 65, incident=True)
    return promote_point_to_top(model, X_1782)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1782 on the given reference triangle."""
    model = create_model('X_1782 = MIMOSA TRANSFORM OF X_1257')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01782(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01782.json"))
    write_center_svg(
        model_acute,
        here / "x-01782.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
